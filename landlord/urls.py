from django.urls import path
from landlord import views

app_name = 'landlord'

urlpatterns = [
    path('', views.LandlordListView.as_view(), name='landlord_home'),
    path('properties/', views.LandlordProperties.as_view(), name='landlord_properties'),
    path('property/create', views.PropertyCreateView.as_view(), name='property_create'),
    path('property/detail/<int:pk>', views.PropertyDetailView.as_view(), name='property_detail'),

    
    # Reminder
    path('reminder/create', views.ReminderCreateView.as_view(), name='reminder_create'),

    # Add Tenant
    path('add-tenant', views.TenantAddCreateView.as_view(), name='add_tenant'),
    path('remove-tenant/<int:pk>', views.remove_tenant, name='remove_tenant'),

    path('message/', views.LandlordMessages.as_view(), name='landlord_messages'),
    path('message/application/approve/<int:pk>/', views.approve_application, name='approve_application'),
    path('message/application/disapprove/<int:pk>/', views.disapprove_application, name='disapprove_application'),
    path('message/individual', views.LandlordIndividualMessages.as_view(), name='individual_messages'),
    path('message/due_date', views.due_date, name='due_date'),
    path('payment/', views.Payment.as_view(), name='payment'),
    path('payment/paid/<int:pk>', views.mark_tenant_paid, name='payment_paid'),
    # path('payment/paid-bedspace/<int:pk>', views.mark_tenant_paid_bedspace, name='payment_paid_bedspace'),
    
    # NOTE For viewing purposes only
    path('add-payment/',views.AddExpenseCreateView.as_view(), name='add_payment'),
    path('history/<int:pk>', views.HistoryListView.as_view(), name='payment_history'),
]