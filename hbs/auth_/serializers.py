from rest_framework import serializers
from .models import MainUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainUser
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}


class ProfileSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(write_only=True)
    avatar = serializers.ImageField()

    def update(self, instance, validated_data):
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance
