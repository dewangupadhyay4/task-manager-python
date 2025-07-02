from .models import TaskManagerModel
from rest_framework import serializers
from django.contrib.auth.models import User

class TaskManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskManagerModel
        fields='__all__'
        read_only_fields=['user']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        extra_kwargs={'password': {'write_only': True}}

    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password=']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user