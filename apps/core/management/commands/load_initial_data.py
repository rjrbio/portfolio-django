from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Carga datos iniciales desde fixtures'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('📦 Cargando datos iniciales...'))
        
        fixtures_dir = 'fixtures'
        
        if not os.path.exists(fixtures_dir):
            self.stdout.write(self.style.ERROR(f'❌ La carpeta {fixtures_dir}/ no existe'))
            return
        
        # Lista de fixtures en orden
        fixtures = [
            'about.json',
            'techs.json',
            'services.json',
            'projects.json',
            'blog.json',
            'testimonials.json',
            'resume.json',
        ]
        
        for fixture in fixtures:
            fixture_path = os.path.join(fixtures_dir, fixture)
            if os.path.exists(fixture_path):
                self.stdout.write(f'  ⏳ Cargando {fixture}...')
                try:
                    call_command('loaddata', fixture_path, verbosity=0)
                    self.stdout.write(self.style.SUCCESS(f'  ✓ {fixture} cargado'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'  ✗ Error en {fixture}: {e}'))
            else:
                self.stdout.write(self.style.WARNING(f'  ⚠ {fixture} no encontrado'))
        
        self.stdout.write(self.style.SUCCESS('\n✅ Datos iniciales cargados correctamente'))
