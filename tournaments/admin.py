from django.contrib import admin
from .models import Tournament, Team, Player
from django.utils.html import format_html

class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'location']
    list_filter = ['date', 'location',]
    ordering = ['name',]
    search_fields = ['name',]
    readonly_fields = ['image_preview',]

    def product_name_with_image(self, obj):
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
    product_name_with_image.short_description = "Nom"
    product_name_with_image.admin_order_field = 'name'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width:200px" />', obj.image.url)
        return ""
    image_preview.short_description = "Prévisualisation"

    def get_readonly_fields(self, request, obj=None):
        # Permet de ne pas afficher "Image Preview" lors de l'ajout
        if obj:  # si c'est lors de la modification
            return self.readonly_fields
        return []

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'tournament', 'paid']

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'team']
    ordering = ['lastname', 'firstname',]
    search_fields = ['lastname', 'firstname',]
    readonly_fields = ['team',]

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)