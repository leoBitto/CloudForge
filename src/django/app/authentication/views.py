from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model
from rest_framework import status

# View per il login
class LoginView(LoginView):
    """
    Gestisce il login degli utenti e genera il token JWT dopo un login riuscito.
    """
    template_name = 'authentication/login.html'  # Percorso del template di login

    def form_valid(self, form):
        """
        Dopo il login, genera il token JWT e lo salva nella sessione.
        """
        # Autenticazione manuale: prova a ottenere l'utente tramite le credenziali fornite
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            # Se l'utente è autenticato con successo, accedi manualmente
            login(self.request, user)

            # Genera il token JWT
            token = AccessToken.for_user(user)

            # Salva il token nella sessione
            self.request.session['token'] = str(token)

            # Reindirizza alla pagina di successo
            return redirect('backoffice:backoffice')
        else:
            
            # Se l'autenticazione fallisce, mostra un messaggio di errore
            return self.form_invalid(form)

    def form_invalid(self, form):
        """
        Gestisce gli errori di login mostrando un messaggio di errore nel template.
        """
            
        messages.error(self.request, 'Credenziali errate. Riprova.')
        return super().form_invalid(form)


# View per il logout
class LogoutView(LogoutView):
    """
    Gestisce il logout degli utenti eliminando il token dalla sessione.
    """
    template_name = 'authentication/logout.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Elimina il token dalla sessione prima di effettuare il logout.
        """
        request.session.pop('token', None)  # Rimuove il token dalla sessione
        return super().dispatch(request, *args, **kwargs)


class VerifySessionView(APIView):
    permission_classes = [AllowAny]  # Aggiungi questa riga
    
    def post(self, request, *args, **kwargs):
        session_id = request.data.get('sessionid')
        
        if not session_id:
            return Response(
                {'error': 'Session ID non fornito'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            session = Session.objects.get(session_key=session_id)
            session_data = session.get_decoded()
            user_id = session_data.get('_auth_user_id')
            
            if not user_id:
                return Response(
                    {'error': 'Sessione non valida'}, 
                    status=status.HTTP_401_UNAUTHORIZED
                )
            
            user = get_user_model().objects.get(id=user_id)
            
            return Response({
                'valid': True,
                'user': {
                    'username': user.username,
                    'groups': list(user.groups.values_list('name', flat=True))
                }
            })
            
        except Session.DoesNotExist:
            return Response(
                {'error': 'Sessione non trovata'}, 
                status=status.HTTP_404_NOT_FOUND
            )
        except get_user_model().DoesNotExist:
            return Response(
                {'error': 'Utente non trovato'}, 
                status=status.HTTP_404_NOT_FOUND
            )


class TokenStatusView(View):
    def get(self, request):
        token = request.session.get('token')
        if not token:
            return JsonResponse({
                "status": "no_token",
                "message": "No token in session"
            }, status=404)
        
        return JsonResponse({
            "status": "valid",
            "token": token
        })

# View protetta per test API
class ProtectedView(APIView):
    """
    Una semplice API protetta che verifica se l'utente è autenticato.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Restituisce una risposta solo se l'utente è autenticato.
        """
        return Response({"message": "Accesso autorizzato!"})
