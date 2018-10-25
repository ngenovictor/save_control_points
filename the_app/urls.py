from django.urls import path
from the_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home' )
]
