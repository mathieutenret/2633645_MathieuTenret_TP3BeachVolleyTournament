from django.contrib import admin
from .models import Tournament, Team, Player
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

# TranslationAdmin affiche les différentes langues dans l'admin (Point 7)
class TournamentAdmin(TranslationAdmin):
    list_display = ['name_with_image', 'date', 'location']
    list_filter = ['date', 'location',]
    ordering = ['name',]
    search_fields = ['name',]
    readonly_fields = ['image_preview',]

    # Renommage de la méthode pour éviter un conflit avec le champ name du modèle Tournament
    def name_with_image(self, obj):
        if obj.image:
            return format_html(
                '<span style="display:flex; align-items:center;">'
                '<img src="{}" style="max-width:32px; margin-right:6px;" />'
                '{}'
                '</span>',
                obj.image.url,
                obj.name,
            )
        return obj.name
        
    name_with_image.short_description = "Nom"
    name_with_image.admin_order_field = 'name'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:200px" />', obj.image.url)
        return ""
    image_preview.short_description = "Prévisualisation"

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return []

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'tournament', 'paid']
    # Filtrage, recherche et triage des équipes dans l'admin (Point 1)
    list_filter = ['tournament', 'paid']
    ordering = ['name',]
    search_fields = ['name', 'tournament_name']

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'team']
    ordering = ['lastname', 'firstname',]
    search_fields = ['lastname', 'firstname',]
    list_filter = ['team',]

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)