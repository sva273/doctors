from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Arzt, Patient, Gruppen


@admin.register(Arzt)
class ArztAdmin(UserAdmin):
    list_display = ('username', 'email', 'last_name', 'fachrichtung', 'berufserfahrung', 'last_login')
    ordering = ('last_name',)

    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('fachrichtung', 'berufserfahrung')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('fachrichtung', 'berufserfahrung')}),)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('login', 'benachrichtigung_wiederherstellung', 'alter', 'adhs_stadium', 'arzt_nachname')
    list_filter = ('adhs_stadium', 'alter', 'arzt__last_name', 'arzt__email')
    search_fields = ('login',)


    def arzt_nachname(self, obj):
        return obj.arzt.last_name if obj.arzt else "-"
    arzt_nachname.short_description = "Nachname des Arztes"


@admin.register(Gruppen)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'arzt_nachname')
    ordering = ('name',)
    list_filter = ('arzt__last_name',)
    search_fields = ('arzt__last_name',)

    def arzt_nachname(self, obj):
        return obj.arzt.last_name if obj.arzt else "-"
    arzt_nachname.short_description = "Nachname des Arztes"
