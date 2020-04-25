from rest_framework import serializers
from .models import UserAPIModel, Exercise


class UserSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()
    username = serializers.CharField(max_length=20)

    class Meta:
        model = UserAPIModel
        fields = ('username', '_id', 'exercises')


    def get_exercises(self, obj):
        return obj.exercises.count()

    def validate_username(self, value):
        """
        Check if username already exist
        """
        if UserAPIModel.objects.filter(username=value).count() > 0:
            raise serializers.ValidationError('Username taken')
        return value


    