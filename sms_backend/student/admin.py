from django.contrib import admin
from student.models import user_model,student_realtions,attendence,subject,classes_model,attendence,teacher_relations

# Register your models here.
admin.site.register(user_model)
# admin.site.register(student_realtions)
admin.site.register(attendence)
admin.site.register(subject)
admin.site.register(teacher_relations)
admin.site.register(classes_model)

@admin.register(student_realtions)
class HeroAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(db_field.name)
        if db_field.name == "student":
            kwargs["queryset"] = user_model.objects.filter(role='student').values_list('name',flat=True)
        if db_field.name == "parent":
            kwargs["queryset"] = user_model.objects.filter(role='parents').values_list('name',flat=True)
        if db_field.name == "classes":
            kwargs["queryset"] = classes_model.objects.all().values_list('name',flat = True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

