from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Expense, ExpenseCategory


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'password_confirm')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined')


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class ExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField()
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Expense
        fields = (
            'id', 'name', 'description', 'amount', 'date', 
            'category', 'category_name', 'user', 'user_username',
            'created_at', 'updated_at'
        )
        read_only_fields = ('user',)

    def create(self, validated_data):
        # Set the user from the request context
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ExpenseListSerializer(serializers.ModelSerializer):
    """Simplified serializer for listing expenses"""
    category_name = serializers.ReadOnlyField()
    class Meta:
        model = Expense
        fields = ('id', 'name', 'amount', 'date', 'category_name', 'created_at')