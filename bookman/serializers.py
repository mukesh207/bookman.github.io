from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

def validate(self, data):
        if Book.objects.filter(isbn_number=data['isbn_number'], author=data['author']).exists():
            raise serializers.ValidationError("A book with this isbn_number and author already exists.")
        return data