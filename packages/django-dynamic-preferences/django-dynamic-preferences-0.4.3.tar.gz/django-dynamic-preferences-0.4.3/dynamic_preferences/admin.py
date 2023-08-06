from django.contrib import admin
from django import forms

from . import global_preferences_registry
from .models import GlobalPreferenceModel, UserPreferenceModel
from .forms import GlobalSinglePreferenceForm, UserSinglePreferenceForm, SinglePerInstancePreferenceForm


class DynamicPreferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'raw_value')
    list_editable = ('raw_value',)
    search_fields = ['name', 'section', 'raw_value']
    list_filter = ('section',)

    def get_changelist_form(self, request, **kwargs):
        return self.changelist_form


class GlobalPreferenceAdmin(DynamicPreferenceAdmin):
    form = GlobalSinglePreferenceForm
    changelist_form = GlobalSinglePreferenceForm

    def get_queryset(self, *args, **kwargs):
        # Instanciate default prefs
        manager = global_preferences_registry.manager()
        manager.all()
        return super(GlobalPreferenceAdmin, self).get_queryset(*args, **kwargs)
        
admin.site.register(GlobalPreferenceModel, GlobalPreferenceAdmin)


class PerInstancePreferenceAdmin(DynamicPreferenceAdmin):
    list_display = ('instance',) + DynamicPreferenceAdmin.list_display
    raw_id_fields = ('instance',)
    form = SinglePerInstancePreferenceForm

class UserPreferenceAdmin(PerInstancePreferenceAdmin):
    search_fields = ['instance__username'] + DynamicPreferenceAdmin.search_fields
    form = UserSinglePreferenceForm
    changelist_form = UserSinglePreferenceForm

admin.site.register(UserPreferenceModel, UserPreferenceAdmin)
