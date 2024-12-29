from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

def create_default_groups(sender, **kwargs):
    groups_permissions = {
        "Developer": ["add_user", "change_user", "view_user", "delete_user"],  # Esempio di permessi
        "Business": ["view_user"],  # Solo permessi di visualizzazione
    }

    for group_name, permissions in groups_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for codename in permissions:
            try:
                # Trova il permesso specifico
                perm = Permission.objects.get(codename=codename)
                group.permissions.add(perm)
            except Permission.DoesNotExist:
                print(f"Permesso {codename} non trovato, ignorato.")

# Collega il segnale
post_migrate.connect(create_default_groups)
