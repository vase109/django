from django.urls import path
from . import views


urlpatterns=[
    path('', views.FoodListView.as_view() , name='food_list'),
    path('<int:pk>/', views.FoodDetailView.as_view() , name='food_detail')
]