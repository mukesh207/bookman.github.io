
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')  # Include username

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'created_at', 'updated_at', 'username']