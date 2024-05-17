from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signin/', views.signin, name='signin'),
    path('main/', views.afterSigninPage.as_view(), name='main-page'),
    path("<slug:slug>/", views.graduateInfoView.as_view(), name='graduate'),
]


