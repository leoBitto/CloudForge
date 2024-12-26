import os
import django
from django.contrib.auth import get_user_model

# Configura l'ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')  # Assicurati che sia il percorso corretto
django.setup()

User = get_user_model()

username = os.getenv('DJANGO_SUPERUSER_USER', 'admin')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created successfully!")
else:
    print("Superuser already exists.")
