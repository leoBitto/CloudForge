# backoffice/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class BackofficeView(LoginRequiredMixin, TemplateView):
    template_name = 'backoffice/backoffice.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        # Passiamo i gruppi a cui l'utente appartiene
        context['user_groups'] = user.groups.values_list('name', flat=True)
        # Recupera il session ID
        context['sessionid'] = self.request.session.session_key
        return context
