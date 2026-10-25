from django import template

register = template.Library()

# Vérification de l'appartenance à un groupe donné (Point 6)
@register.filter
def has_group(user, group_name):
    if user.is_authenticated:
        return user.groups.filter(name=group_name).exists()
    else:
        return False