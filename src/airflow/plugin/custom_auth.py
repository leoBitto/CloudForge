from airflow.www.security import AirflowSecurityManager
from flask_login import login_user
from flask import request, redirect
import requests
from functools import wraps

class DjangoSessionAuthBackend:
    def __init__(self):
        self.django_verify_url = "http://django-app:8000/auth/api/verify-session/"

    def get_or_create_airflow_user(self, user_data):
        """
        Crea o recupera un utente Airflow basato sui dati dell'utente Django
        """
        from airflow.www.security import User
        from airflow import models
        from airflow.utils.db import provide_session

        @provide_session
        def get_user(username, session=None):
            user = session.query(User).filter(
                User.username == username
            ).first()

            if not user:
                user = User(
                    username=username,
                    is_active=True,
                    is_authenticated=True
                )
                session.add(user)
                session.commit()

            return user

        return get_user(user_data['username'])

    def authenticate(self, request):
        """
        Autentica l'utente verificando la sessione Django
        """
        session_id = request.cookies.get('sessionid')

        if not session_id:
            return None

        try:
            # Verifica la sessione con Django
            response = requests.post(
                self.django_verify_url,
                json={'sessionid': session_id},
                timeout=5
            )

            if response.status_code == 200:
                user_data = response.json().get('user')
                if not user_data:
                    return None

                # Crea o recupera l'utente Airflow
                airflow_user = self.get_or_create_airflow_user(user_data)
                if airflow_user:
                    login_user(airflow_user)
                    return airflow_user

        except requests.ConnectionError:
            print("Errore di connessione con il server Django")
        except requests.Timeout:
            print("Timeout durante la connessione con il server Django")
        except Exception as e:
            print(f"Errore durante l'autenticazione: {e}")

        return None

class CustomSecurityManager(AirflowSecurityManager):
    def get_authentication_backend(self):
        return DjangoSessionAuthBackend()

    def authenticate(self, *args, **kwargs):
        """
        Override del metodo di autenticazione predefinito
        """
        backend = self.get_authentication_backend()
        return backend.authenticate(request)

def requires_authentication(f):
    """
    Decorator per proteggere le views di Airflow
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        backend = DjangoSessionAuthBackend()
        user = backend.authenticate(request)
        if user is None:
            return redirect('/login/')
        return f(*args, **kwargs)
    return decorated
