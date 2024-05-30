from typing import Any
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data: Any) -> Course:
      return Course.objects.create(**validated_data)
