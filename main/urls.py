from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    
    # Admin Panel URLs
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    # Admin Panel URLs for managing Home Features
    path('homepage_management/',views.homepage_management,name='homepage_management'),
    path('homepage_management/add-hero/',views.add_hero,name='add_hero'),
    path('homepage_management/edit-hero/<int:id>/',views.edit_hero,name='edit_hero'),
    path('homepage_management/delete-hero/<int:id>/',views.delete_hero,name='delete_hero'),
    # Admin Panel URLs for managing Home categories
    path('homepage_management/add-category/',views.add_category, name='add_category'),
    path('homepage_management/edit-category/<int:id>/',views.edit_category,name='edit_category'),
    path('homepage_management/delete-category/<int:id>/',views.delete_category,name='delete_category'),
    # Owner Panel URLs
    path('owner_panel/owner_register/',views.owner_register,name='owner_register'),
    path('owner_panel/owner_login/',views.owner_login,name='owner_login'),
    path('owner_panel/owner_dashboard/',views.owner_dashboard,name='owner_dashboard'),
    path('owner_panel/owner_logout/',views.owner_logout,name='owner_logout'),   
    # 
]