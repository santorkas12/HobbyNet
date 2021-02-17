from django.contrib import admin
from .models import Event, Participant
from users.admin import EventsInLine


class ParticipantsInline(admin.TabularInline):
    model = Participant

class EventsAdmin(admin.ModelAdmin):
    model = Event
    list_display = ('id','title', 'organizer', 'category')
    inlines = [ParticipantsInline,]

#class EventsInLine(admin.TabularInline):
#    model = Event

class ParticipantsAdmin(admin.ModelAdmin):
    model = Participant
    list_display = ('participant', 'event')




admin.site.register(Event, EventsAdmin)
admin.site.register(Participant, ParticipantsAdmin)
