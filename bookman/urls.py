from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),  # Custom registration view
    # path('', views.loginsuccess),  # Example homepage
]



