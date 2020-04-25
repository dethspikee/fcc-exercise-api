from rest_framework import serializers
from .models import UserAPIModel, Exercise




class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ('user', 'description', 'duration')

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    count = serializers.SerializerMethodField()
    logs = ExerciseSerializer(many=True, read_only=True)
    class Meta:
        model = UserAPIModel
        fields = ('username', '_id', 'count' ,'logs')


    def get_count(self, obj):
        return obj.logs.count()

    def validate_username(self, value):
        """
        Check if username already exist
        """
        if UserAPIModel.objects.filter(username=value).count() > 0:
            raise serializers.ValidationError('Username taken')
        return value