from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.StudioLoginView.as_view(), name='login'),
    path('logout/', views.StudioLogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path('service/<int:id>/', views.SepServiceView.as_view(), name='separate_service'),
    path('order/<int:service_id>/', views.order_service, name='order_service'),
    path('services/all/', views.services_all, name='services_all'),
    path('search/', views.search_service, name='search_service'),
]
