from rest_framework import viewsets

from .serializers import AuthorSerializer
from .serializers import PublisherSerializer
from .serializers import BookSerializer
from .serializers import StoreSerializer

from base.models import Author
from base.models import Publisher
from base.models import Book
from base.models import Store

from rest_framework.permissions import AllowAny

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny, )
    queryset = Author.objects.all()
    lookup_field = 'pk'


class PublisherViewSet(viewsets.ModelViewSet):
    serializer_class = PublisherSerializer
    permission_classes = (AllowAny, )
    queryset = Publisher.objects.all()
    lookup_field = 'pk'


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = (AllowAny, )
    queryset = Book.objects.all()
    lookup_field = 'pk'


class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    permission_classes = (AllowAny, )
    queryset = Store.objects.all()
    lookup_field = 'pk'