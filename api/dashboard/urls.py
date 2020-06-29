from rest_framework.routers import DefaultRouter

from django.urls import path, include

from . import views

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet, basename='author')
router.register(r'publishers', views.PublisherViewSet, basename='publisher')
router.register(r'books', views.BookViewSet, basename='book')
router.register(r'stores', views.StoreViewSet, basename='store')

app_name='dashboard'

urlpatterns = [
    path('', include(router.urls)),
]