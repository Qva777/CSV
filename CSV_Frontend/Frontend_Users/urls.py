from django.urls import path
from django.contrib.auth import views as auth_views
from CSV_Frontend.Frontend_Users.views import UserLoginView

urlpatterns = [
    # Login / Logout
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
