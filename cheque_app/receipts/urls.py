from django.urls import path

from . import views

app_name = 'receipts'

urlpatterns = [
    path('', views.index),
    # path('list/', views.receipts_list, name='receipts_list'),
    path('list/', views.ReceiptListView.as_view(), name='receipt_list'),
    path(
        'datail/<int:pk>/', views.receipt_detail, name='receipt_detail'),
    path('goups/', views.groups_list),
    path('groups/<slug:slug>/', views.group),
]