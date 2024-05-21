from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    su_email = 'first_admin@sky.pro'

    def handle(self, *args, **options):
        if not User.objects.filter(email=self.su_email).exists():
            user = User.objects.create(
                email=self.su_email,
                is_staff=True,
                is_superuser=True,
            )
            user.set_password('1qaz2wsx')
            user.save()
