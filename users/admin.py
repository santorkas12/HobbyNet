from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile, Interests
from .forms import CustomUserCreationForm, CustomUserChangeForm

from events.models import Event, Participant

# Register your models here.

#Show events related to user
class EventsInLine(admin.TabularInline):
    model = Event
    verbose_name = "Event Organized"
    verbose_name_plural = "Events Organized"

class ParticipantsInLine(admin.TabularInline):
    model = Participant
    verbose_name = "Event Participated"
    verbose_name_plural = "Events Participating In"

class InterestsInLine(admin.TabularInline):
    model = Interests
    verbose_name = "Interest"
    verbose_name_plural = "Interests"

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'date_of_birth', 'is_active', 'is_staff')
    list_filter = ('email', 'first_name', 'last_name', 'date_of_birth', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name','last_name', 'date_of_birth' ,'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )

    inlines = [InterestsInLine, EventsInLine, ParticipantsInLine]

    search_fields = ('email',)
    ordering = ('email',)





admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
