from django.urls import path
from .views import ExpenseCreateView, ExpenseListView, ExpenseUpdateView, ExpenseDeleteView


urlpatterns = [
    path('create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('', ExpenseListView.as_view(), name='expense-list'),
    path('<int:pk>/update/', ExpenseUpdateView.as_view(), name='expense-update'),
    path('<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense-delete')
]