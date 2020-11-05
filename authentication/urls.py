from django.urls import path
from .views import RegisterView, LoginView,MovieList,moviedetails
from . import views

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('movies/', MovieList.as_view()),
    path('movies/<int:pk>/', views.moviedetails),
]
