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
    student = UserSerializers(many =True)
    parents = UserSerializers(many = True)
    class Meta:
        model = student_realtions
        fields = ['student','parents']
    
    def create(self, validated_data):
        import pdb;pdb.set_trace()
        return 'order'