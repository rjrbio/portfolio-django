from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = '🔒 EMERGENCIA: Elimina usuarios inseguros de la base de datos'

    def add_arguments(self, parser):
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Confirmar eliminación de usuarios inseguros',
        )

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Lista de usuarios inseguros conocidos
        insecure_usernames = ['admin', 'administrator', 'root', 'test', 'demo']
        insecure_passwords = ['admin123', 'admin', 'password', '123456', 'test']
        
        self.stdout.write(self.style.WARNING(''))
        self.stdout.write(self.style.WARNING('🔍 Buscando usuarios inseguros en la base de datos...'))
        self.stdout.write(self.style.WARNING(''))
        
        users_to_remove = []
        
        # Verificar usuarios inseguros
        for username in insecure_usernames:
            user = User.objects.filter(username=username).first()
            if user:
                # Verificar si tiene password inseguro
                has_insecure_password = False
                for insecure_pass in insecure_passwords:
                    if user.check_password(insecure_pass):
                        has_insecure_password = True
                        break
                
                if has_insecure_password:
                    users_to_remove.append({
                        'username': user.username,
                        'email': user.email,
                        'is_superuser': user.is_superuser,
                        'date_joined': user.date_joined
                    })
                    self.stdout.write(
                        self.style.ERROR(f'❌ INSEGURO: {user.username} ({user.email})')
                    )
        
        if not users_to_remove:
            self.stdout.write(self.style.SUCCESS('✅ No se encontraron usuarios inseguros'))
            return
        
        # Mostrar resumen
        self.stdout.write(self.style.WARNING(''))
        self.stdout.write(self.style.WARNING(f'Se encontraron {len(users_to_remove)} usuario(s) inseguro(s):'))
        for user_info in users_to_remove:
            self.stdout.write(f'  - {user_info["username"]} ({user_info["email"]})')
        
        # Confirmar eliminación
        if not options['confirm']:
            self.stdout.write(self.style.WARNING(''))
            self.stdout.write(self.style.WARNING('⚠️  Para eliminar estos usuarios, ejecuta:'))
            self.stdout.write(self.style.WARNING(''))
            self.stdout.write(self.style.WARNING('    python manage.py remove_insecure_users --confirm'))
            self.stdout.write(self.style.WARNING(''))
            return
        
        # Eliminar usuarios
        self.stdout.write(self.style.WARNING(''))
        self.stdout.write(self.style.WARNING('🔒 Eliminando usuarios inseguros...'))
        
        for user_info in users_to_remove:
            try:
                user = User.objects.get(username=user_info['username'])
                user.delete()
                self.stdout.write(
                    self.style.SUCCESS(f'✓ Eliminado: {user_info["username"]}')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'✗ Error al eliminar {user_info["username"]}: {e}')
                )
        
        self.stdout.write(self.style.SUCCESS(''))
        self.stdout.write(self.style.SUCCESS('✅ Limpieza completada'))
        self.stdout.write(self.style.SUCCESS(''))
        self.stdout.write(self.style.WARNING('📌 Verifica que tu usuario seguro esté configurado en .env:'))
        self.stdout.write(self.style.WARNING('    DJANGO_SUPERUSER_USERNAME=tu_usuario'))
        self.stdout.write(self.style.WARNING('    DJANGO_SUPERUSER_PASSWORD=tu_password_seguro'))
        self.stdout.write(self.style.WARNING(''))
