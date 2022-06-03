from rest_framework import serializers
from student.models import user_model,classes_model,student_realtions

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = '__all__'

class ClassSerilizer(serializers.ModelSerializer):
    class Meta:
        model = classes_model
        fields = "__all__"

class StudentSerilizer(serializers.ModelSerializer):
    student = UserSerializers()
    parent = UserSerializers()
    
    class Meta:
        model = student_realtions
        fields = ['student','parent','classes','section']
    
    def create(self, validated_data):   
        student = user_model.objects.create(**validated_data.get('student'))
        parent = user_model.objects.create(**validated_data.get('parent'))
        classes = validated_data.get('classes')
        section = validated_data.get('section')
        student_relation = student_realtions.objects.create(student = student, parent = parent,classes = classes,section = section)
        return student_relation
