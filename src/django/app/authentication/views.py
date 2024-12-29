from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib import messages
from django.contrib.auth import authenticate, login

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


class TokenStatusView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        token = request.session.get('token')
        if not token:
            return Response({
                "status": "no_token",
                "message": "No token in session"
            }, status=404)
            
        try:
            # Decodifica il token per ottenere le informazioni
            token_obj = AccessToken(token)
            return Response({
                "status": "valid",
                "expires": token_obj.payload.get('exp'),
                "user": token_obj.payload.get('user_id')
            })
        except Exception as e:
            return Response({
                "status": "invalid",
                "message": str(e)
            }, status=400)


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
