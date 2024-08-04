from rest_framework import serializers
from .models import Student


class StudentSerialize(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'