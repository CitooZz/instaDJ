from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(source='user.profile.avatar')
    description = serializers.SerializerMethodField(
        source='user.profile.description')

    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    confirm_password = serializers.CharField()

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'avatar',
                  'description', 'follower_count', 'following_count',
                  'password', 'confirm_password')

        read_only_fields = ('follower_count', 'following_count')
        write_only_fields = ('confirm_password', 'password')

    @staticmethod
    def get_follower_count(self, instance):
        return instance.profile.followers.all().count()

    @staticmethod
    def get_following_count(self, instance):
        return instance.profile.followings.all().count()


class FollowingSerializer(serializers.Serializer):
    user = serializers.CharField()

    def validate(self, data):
        qs = User.objects.filter(id=data.get('user'))
        if not qs.exists():
            raise serializers.ValidationError('User not found')

        return data
