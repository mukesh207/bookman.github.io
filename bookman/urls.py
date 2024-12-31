from django.urls import path
from .views import SignupView, LogoutView, BookListView, BookDetailView
from .views import SignInWithTokenView
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('books/', BookListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('signin/', SignInWithTokenView.as_view(), name='signin'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]