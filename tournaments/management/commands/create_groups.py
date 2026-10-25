from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Création des groupes et de leurs permissions"

    def handle(self, *args, **kwargs):
        # Création des différents groupes (Point 6)
        organizers, created = Group.objects.get_or_create(name='Organisateurs')
        employees, created = Group.objects.get_or_create(name='Employés')
        participants, created = Group.objects.get_or_create(name='Participants')

        # Permissions accordées aux organisateurs => admin (Point 6)
        organizer_permissions = Permission.objects.filter(
            content_type__app_label='tournaments',
            content_type__model__in=['team', 'player']
        )
        organizers.permissions.set(organizer_permissions)

        # Permissions accordées aux employés (Point 6)
        employee_permissions = Permission.objects.filter(
            content_type__app_label='tournaments',
            content_type__model__in=['team', 'player'],
        )
        employees.permissions.set(employee_permissions)

        # Permissions accordées aux participants (Point 6)
        participant_permissions = Permission.objects.filter(
            content_type__app_label='tournaments',
            content_type__model__in=['team', 'player'],
            codename__in=['view_team', 'add_team', 'view_player', 'add_player']
        )
        participants.permissions.set(participant_permissions)

        self.stdout.write(self.style.SUCCESS("Groups created successfully!"))

