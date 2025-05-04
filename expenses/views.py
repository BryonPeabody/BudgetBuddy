from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Expense, Category
from .forms import ExpenseForm, CategoryForm


class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expense-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
