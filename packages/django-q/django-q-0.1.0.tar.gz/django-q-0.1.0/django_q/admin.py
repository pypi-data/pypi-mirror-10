from django.contrib import admin

from django_q.core import async

from .models import Success, Failure, Schedule


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        u'name',
        'func',
        'started',
        'time_taken'
    )

    def has_add_permission(self, request, obj=None):
        """Don't allow adds"""
        return False

    def get_queryset(self, request):
        """Only show successes"""
        qs = super(TaskAdmin, self).get_queryset(request)
        return qs.filter(success=True)

    search_fields = ['name']
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields]


def retry_failed(FailAdmin, request, queryset):
    for task in queryset:
        async(task.func, *task.args, hook=task.hook, **task.kwargs)
        task.delete()


retry_failed.short_description = "Resubmit selected tasks to Q"


class FailAdmin(admin.ModelAdmin):
    list_display = (
        u'name',
        'func',
        'started',
        'result'
    )

    def has_add_permission(self, request, obj=None):
        """Don't allow adds"""
        return False

    actions = [retry_failed]
    search_fields = ['name']
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields]

class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'func',
        'schedule_type',
        'repeats',
        'next_run',
        'last_run',
        'success'
    )

    list_filter = ('next_run', 'schedule_type')

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Success, TaskAdmin)
admin.site.register(Failure, FailAdmin)
