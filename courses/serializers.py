from rest_framework import serializers
from .models import CourseModels, ReviewModels


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {
                'write_only': True,
            }
        }
        model = ReviewModels
        fields = [
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created_at',
            'updated_at',
            'active',
        ]

    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModels
        fields = [
            'id',
            'title',
            'url',
            'created_at',
            'updated_at',
            'active',
        ]