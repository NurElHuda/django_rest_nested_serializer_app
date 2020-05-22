from rest_framework import exceptions, serializers
from django.contrib.auth.models import User

from .models import Client


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField(source='pk', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField(source='pk', read_only=True)
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ('id', 'user', 'last_login_date', 'points')

    def create(self, validated_data):
        user_validated_data = validated_data.pop('user', None)
        user_password = user_validated_data.pop('password', None)

        user = User.objects.create(**user_validated_data)
        user.set_password(user_password)
        user.save()

        client = Client.objects.create(user=user, **validated_data)
        return client

    def update(self, instance, validated_data):
        user_validated_data = validated_data.pop('user', None)

        user = instance.user                    
        user.username = user_validated_data.get('username', user.username)
        user.email = user_validated_data.get('email', user.email)
        user.first_name = user_validated_data.get('first_name', user.first_name)
        user.last_name = user_validated_data.get('last_name', user.last_name)
        if user_validated_data.get('last_name'):
            user.set_password(user_validated_data.get('last_name'))
        user.save()

        instance.points = validated_data.get('points', instance.points)
        instance.last_login_date = validated_data.get('last_login_date', instance.last_login_date)
        instance.save()
        return instance
