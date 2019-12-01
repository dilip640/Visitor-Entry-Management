from django.contrib import admin
from entryapp.models import Host,Visitor, PastVisitor

class HostAdminView(admin.ModelAdmin):
    list_display = [field.name for field in Host._meta.fields]

admin.site.register(Host, HostAdminView)

class VisitorAdminView(admin.ModelAdmin):
    list_display = [field.name for field in Visitor._meta.fields]

admin.site.register(Visitor, VisitorAdminView)

class PastVisitorAdminView(admin.ModelAdmin):
    list_display = [field.name for field in PastVisitor._meta.fields]

admin.site.register(PastVisitor, PastVisitorAdminView)