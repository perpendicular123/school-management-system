from rest_framework import serializers
from student.models import user_model

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = '__all__'