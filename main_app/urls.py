from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_comment/', views.add_comment, name='add_comment'),
    path('websites/', views.WebsiteList.as_view(), name='websites_index'),
    path('websites/<int:pk>/', views.WebsiteDetail.as_view(), name='websites_detail'),
    path('websites/create/', views.WebsiteCreate.as_view(), name='websites_create'),
    path('websites/<int:pk>/update/', views.WebsiteUpdate.as_view(), name='websites_update'),
    path('websites/<int:pk>/delete/', views.WebsiteDelete.as_view(), name='websites_delete'),
    path('cars/<int:car_id>/assoc_website/<int:website_id>/', views.assoc_website, name='assoc_website'),
    path('cars/<int:car_id>/unassoc_website/<int:website_id>/', views.unassoc_website, name='unassoc_website'),
]