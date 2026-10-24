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
    # Admin Panel URLs for managing Home Features
    path('homepage_management/add-why-choose/',views.add_why_choose_feature,name='add_why_choose_feature'),
    path('homepage_management/edit-why-choose/<int:id>/',views.edit_why_choose_feature,name='edit_why_choose_feature'),
    path('homepage_management/delete-why-choose/<int:id>/',views.delete_why_choose_feature,name='delete_why_choose_feature'),
    
    # Owner Panel URLs
    path('owner_panel/owner_register/',views.owner_register,name='owner_register'),
    path('owner_panel/owner_login/',views.owner_login,name='owner_login'),
    path('owner_panel/owner_dashboard/',views.owner_dashboard,name='owner_dashboard'),
    path('owner_panel/owner_logout/',views.owner_logout,name='owner_logout'),   
    # owner panel URLs for managing properties
    path('owner_panel/add_property/', views.add_property, name='add_property'),
    path('owner_panel/my_properties/', views.my_properties, name='my_properties'),
    # myproperties URLs for editing and deleting properties
    path('owner_panel/edit_property/<int:property_id>/',views.edit_property,name='edit_property'),
    path('owner_panel/delete_property/<int:property_id>/', views.delete_property,name='delete_property'),
    # My Profile URLs
    path('owner_panel/edit_profile/', views.edit_owner_profile, name='edit_owner_profile'),
    path('owner_panel/delete_profile/', views.delete_owner_profile, name='delete_owner_profile'),

    # User Panel URLs
    
path('user_panel/register/', views.user_register, name='user_register'),
path('user_panel/login/', views.user_login, name='user_login'),
path('user_panel/properties/', views.property_list, name='property_list'),
path('user_panel/logout/', views.user_logout, name='user_logout'),
path(
    'user_panel/dashboard/',
    views.user_dashboard,
    name='user_dashboard'
),

# path('user_panel/profile/', views.user_profile, name='user_profile'),

]