from django.urls import path
from . import views

urlpatterns = [
    path('', views.studylist),
    path('uploadform/', views.studyuploadform),

]
