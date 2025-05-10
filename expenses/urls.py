from django.urls import path
from expenses.views import (
    ExpenseCreateView,
    ExpenseListView,
    ExpenseUpdateView,
    ExpenseDeleteView,
    register,
    CategoryCreateView,
    CategoryListView,
    CategoryUpdateView,
    CategoryDeleteView,)


urlpatterns = [
    path('create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('', ExpenseListView.as_view(), name='expense-list'),
    path('<int:pk>/update/', ExpenseUpdateView.as_view(), name='expense-update'),
    path('<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense-delete'),
    path('register/', register, name='register'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view, name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view, name='category-delete')
]