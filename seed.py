import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doctors.settings")
django.setup()

from api.models import Arzt

# создаём объект врача без сохранения пароля
artz = Arzt(
    username='muller88',
    first_name='Max',
    last_name='Muller',
    email='muller88@example.com',
    fachrichtung='Therapeut',
    berufserfahrung='5 Jahre'
)

# безопасно хэшируем пароль
artz.set_password('hsdbfhsdbfg')

# сохраняем объект
artz.save()

print("Arzt erfolgreich erstellt:", artz)
