from rest_framework.serializers import ModelSerializer
from .models import CustomeUser, Role

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomeUser
        fields = ['id', 'phone', 'password', 'role', 'bio']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return CustomeUser.objects.create_user(**validated_data)