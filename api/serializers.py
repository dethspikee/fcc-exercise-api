from rest_framework import serializers
from .models import UserAPIModel, Exercise
from datetime import date




class ExerciseSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=False, format="%a %b %d %Y")
    class Meta:
        model = Exercise
        fields = ('id', 'user', 'description', 'duration', 'date')

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20)
    class Meta:
        model = UserAPIModel
        fields = ('_id', 'username')
        
    def validate_username(self, value):
        """
        Check if username already exist
        """
        if UserAPIModel.objects.filter(username=value).count() > 0:
            raise serializers.ValidationError('Username taken')
        return value

    

class UserLogSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    username = serializers.CharField(max_length=20)
    log = ExerciseSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserAPIModel
        fields = ('_id', 'username', 'count' ,'log')

    def get_count(self, obj):
        return obj.log.count()

    def validate_username(self, value):
        """
        Check if username already exist
        """
        if UserAPIModel.objects.filter(username=value).count() > 0:
            raise serializers.ValidationError('Username taken')
        return value


class UserFromSerializer(UserLogSerializer,serializers.ModelSerializer):
    logs_from = serializers.SerializerMethodField()

    class Meta(UserLogSerializer.Meta):
        fields = ('_id', 'username', 'logs_from', 'count', 'log')

    def get_logs_from(self, obj):
        """
        Get a year value passed from a view and create valid date
        """
        year = int(self.context.get('from'))
        return date(year,1,1).strftime('%b %m %Y')
