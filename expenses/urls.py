from django.urls import path
from .views import ExpenseCreateView, ExpenseListView


urlpatterns = [
    path('create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('', ExpenseListView.as_view(), name='expense-list')
]