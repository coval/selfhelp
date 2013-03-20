from django.contrib import admin
from dbflow.models import Field, Step

#class FieldAdmin(admin.ModelAdmin):
#    pass

#class StepAdmin(admin.ModelAdmin):
#    pass



class MembershipInline(admin.TabularInline):
    model = Step.field.through

class FieldAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]

class StepAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]
    exclude = ('field',)





admin.site.register(Field, FieldAdmin)
admin.site.register(Step, StepAdmin)
