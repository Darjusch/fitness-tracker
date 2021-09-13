from django.contrib import admin
from userauth.models import Training
# Register your models here.

class TrainingAdmin(admin.ModelAdmin):
    # empty_value_display = '-empty-'
    list_display = ('user', 'bench', 'squats', 'pullups', 'deadlift', 'militarypress', 'date',)
    list_filter= ('user', 'date',)


admin.site.register(Training, TrainingAdmin)