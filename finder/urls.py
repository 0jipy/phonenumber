from django.urls import path
from . import views

urlpatterns = [
    path('', views.Finders.as_view()),
    path('<int:pk>/', views.FinderDetail.as_view()),
    # path('', views.index),
    # path('<int:pk>/', views.single_page),
]