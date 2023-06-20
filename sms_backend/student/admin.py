from django.contrib import admin

from student.models import (
    attendence,
    classes_model,
    student_realtions,
    subject,
    teacher_relations,
    user_model,
)

# Register your models here.
admin.site.register(user_model)
# admin.site.register(student_realtions)
admin.site.register(attendence)
admin.site.register(subject)
# admin.site.register(teacher_relations)
admin.site.register(classes_model)


@admin.register(student_realtions)
class HeroAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(db_field.name)
        if db_field.name == "student":
            kwargs["queryset"] = user_model.objects.filter(role="student").values_list(
                "name", flat=True
            )
        if db_field.name == "parent":
            kwargs["queryset"] = user_model.objects.filter(role="parents").values_list(
                "name", flat=True
            )
        if db_field.name == "classes":
            kwargs["queryset"] = classes_model.objects.all().values_list(
                "name", flat=True
            )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(teacher_relations)
class teacherRelation(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(db_field.name)
        if db_field.name == "teacher":
            kwargs["queryset"] = user_model.objects.filter(role="teacher")
        if db_field.name == "parent":
            kwargs["queryset"] = user_model.objects.filter(role="parents")
        if db_field.name == "classes":
            kwargs["queryset"] = classes_model.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
