from core.account.models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    """Serializes the custom user model object. """
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields="__all__"
        extra_kwargs={
        'password':{'write_only':True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs

    def create(self, validated_data):
        _ = validated_data.pop('password2')
        user = CustomUser(**validated_data)
        user.save()
        return user
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    class Meta:
        fields = ('email', 'password')