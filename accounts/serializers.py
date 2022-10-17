from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import CustomUser

class SignUpSerializer(serializers.ModelSerializer):
    # add avalidations
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password']

    # check if the user existing in the database

    def validate(self, attrs):
        email_exists = CustomUser.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("Email has already been used")
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)

        user.set_password(password)

        user.save()
        return user