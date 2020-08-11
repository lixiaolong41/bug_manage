from django.contrib import admin
from .models import Project, BugList, Modular, Edition, History


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'founder', 'status')


admin.site.register(Project, ProjectAdmin)


class BugListAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_name', 'edition', 'modular', 'priority', 'handler', 'describe')


admin.site.register(BugList, BugListAdmin)


class ModularAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'modular')


admin.site.register(Modular, ModularAdmin)


class EditionAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'edition')


admin.site.register(Edition, EditionAdmin)


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('bug', 'handler', 'handler_time', 'describe', 'operation')


admin.site.register(History, HistoryAdmin)
