from rest_framework import serializers

from base.models import Author
from base.models import Publisher
from base.models import Book
from base.models import Store

from sqlalchemy.orm import sessionmaker
from project.settings import SQLALCHEMY_ENGINE

Session = sessionmaker(bind=SQLALCHEMY_ENGINE)
session = Session()

import datetime


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data['name']
        age = validated_data['age']
        created_on = datetime.datetime.today()
        instance = Author(name=name,age=age, created_on=created_on)
        session.add(instance)

        return instance



class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(read_only=True, many=True)
    publisher = PublisherSerializer(read_only=True)
    class Meta:
        model = Book
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Store
        fields = "__all__"