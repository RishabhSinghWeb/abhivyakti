from django.contrib import admin
from .models import Volunteer,CellName,CompetitionName,Registration,TeamPost,TeamMemberName,ContactUs,EventName,EventResult,Update,RulesOfEvent,PerformingEvent,TechnicalTeam

# Register your models here.
admin.site.register(Volunteer)
admin.site.register(CellName)
admin.site.register(CompetitionName)
admin.site.register(Registration)
admin.site.register(TeamPost)
admin.site.register(TeamMemberName)
admin.site.register(ContactUs)
admin.site.register(EventName)
admin.site.register(EventResult)
admin.site.register(Update)
admin.site.register(RulesOfEvent)
admin.site.register(PerformingEvent)
admin.site.register(TechnicalTeam)


