from django.contrib import admin
from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path("", views.index, name="index"),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/user_detail/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('dashboard/user_update/<int:pk>', views.UserUpdateView.as_view(), name='user_update'),
    path("dashboard/company/list", views.CompanyListView.as_view() , name="company_list"),
    path('dashboard/company/create', views.CompanyCreateView.as_view(), name='company_create'),
    path('dashboard/compnay/edit/<int:pk>', views.CompanyEditView.as_view(), name='company_edit'),
    path('dashboard/compnay/detail/<int:pk>', views.CompanyDetailView.as_view(), name='company_detail'),
    path("dashboard/item/list", views.ItemListView.as_view() , name="item_list"),
    path('dashboard/item/create', views.ItemCreateView.as_view(), name='item_create'),
    path('dashboard/item/edit/<int:pk>', views.ItemEditView.as_view(), name='item_edit'),
    path("dashboard/order/list", views.OrderListView.as_view() , name="order_list"),
    path('dashboard/order/create', views.OrderCreateView.as_view(), name='order_create'),
    path('dashboard/order/edit/<int:pk>', views.OrderEditView.as_view(), name='order_edit'),
    path('dashboard/order/detail/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('dashboard/orderdetail/create/<int:order_id>', views.OrderDetailCreateView.as_view(), name='orderdetail_create'),
    path('dashboard/orderdetail/edit/<int:pk>', views.OrderDetailEditView.as_view(), name='orderdetail_edit'),
    path('dashboard/orderdetail/delete/<int:pk>', views.OrderDetailDeleteView.as_view(), name='orderdetail_delete'),
]
