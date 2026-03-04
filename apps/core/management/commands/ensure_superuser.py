from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Crea un superusuario si no existe. Requiere variables de entorno configuradas.'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Obtener credenciales desde variables de entorno (SIN defaults inseguros)
        username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
        
        # Validar que todas las variables estén configuradas
        if not username or not email or not password:
            self.stdout.write(self.style.ERROR('❌ ERROR DE SEGURIDAD: Credenciales no configuradas'))
            self.stdout.write(self.style.WARNING(''))
            self.stdout.write(self.style.WARNING('Debes configurar las siguientes variables de entorno:'))
            self.stdout.write(self.style.WARNING('  - DJANGO_SUPERUSER_USERNAME'))
            self.stdout.write(self.style.WARNING('  - DJANGO_SUPERUSER_EMAIL'))
            self.stdout.write(self.style.WARNING('  - DJANGO_SUPERUSER_PASSWORD'))
            self.stdout.write(self.style.WARNING(''))
            self.stdout.write(self.style.WARNING('👉 Ejecuta: python setup_env.py'))
            self.stdout.write(self.style.WARNING('O crea manualmente el archivo .env con credenciales seguras'))
            raise CommandError('Configuración de superusuario incompleta')
        
        # Validar seguridad de la contraseña
        if len(password) < 8:
            self.stdout.write(self.style.ERROR('❌ ERROR: La contraseña debe tener al menos 8 caracteres'))
            raise CommandError('Contraseña insegura')
        
        # Advertencia si se usan credenciales por defecto conocidas
        if username == 'admin' or password == 'admin123' or password == 'admin':
            self.stdout.write(self.style.ERROR('❌ ERROR DE SEGURIDAD CRÍTICO'))
            self.stdout.write(self.style.ERROR('NO puedes usar credenciales por defecto (admin/admin123)'))
            self.stdout.write(self.style.ERROR('Configura credenciales únicas y seguras en el archivo .env'))
            raise CommandError('Credenciales inseguras detectadas')
        
        # SEGURIDAD: Eliminar usuarios inseguros conocidos de la base de datos
        insecure_usernames = ['admin', 'administrator', 'root', 'test', 'demo']
        for insecure_username in insecure_usernames:
            try:
                insecure_user = User.objects.filter(username=insecure_username).first()
                if insecure_user and insecure_username != username:
                    # Verificar si el password es el inseguro por defecto
                    if insecure_user.check_password('admin123') or insecure_user.check_password('admin'):
                        self.stdout.write(self.style.WARNING(f'🔒 Eliminando usuario inseguro: "{insecure_username}"'))
                        insecure_user.delete()
                        self.stdout.write(self.style.SUCCESS(f'✓ Usuario inseguro "{insecure_username}" eliminado'))
                    else:
                        # Si tiene otro password, solo advertir
                        self.stdout.write(self.style.WARNING(f'⚠️  Usuario "{insecure_username}" existe con password diferente'))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f'⚠️  Error al verificar usuario "{insecure_username}": {e}'))
        
        # Crear o reparar superusuario seguro
        existing_user = User.objects.filter(username=username).first()
        if not existing_user:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'✓ Superusuario "{username}" creado exitosamente'))
        else:
            updated_fields = []

            if existing_user.email != email:
                existing_user.email = email
                updated_fields.append('email')

            if not existing_user.is_staff:
                existing_user.is_staff = True
                updated_fields.append('is_staff')

            if not existing_user.is_superuser:
                existing_user.is_superuser = True
                updated_fields.append('is_superuser')

            if not existing_user.is_active:
                existing_user.is_active = True
                updated_fields.append('is_active')

            existing_user.set_password(password)
            updated_fields.append('password')

            existing_user.save()

            self.stdout.write(self.style.SUCCESS(
                f'✓ Superusuario "{username}" actualizado ({", ".join(updated_fields)})'
            ))
