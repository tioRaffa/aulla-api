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

    # reviews = ReviewSerializer(many=True, read_only=True)

    reviews = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='review-detail'
    )


    class Meta:
        model = CourseModels
        fields = [
            'id',
            'title',
            'url',
            'created_at',
            'updated_at',
            'active',
            'reviews',
        ]
        