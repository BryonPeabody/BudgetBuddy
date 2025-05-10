from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from expenses.models import Expense, Category


class TestExpenseViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(user=self.user, category='Test Category')
        self.expense = Expense.objects.create(
            user=self.user,
            description='Test Expense',
            amount=50,
            date='2025-05-01',
            category=self.category
        )

    def test_login_required_redirect(self):
        response = self.client.get(reverse('expense-list'))
        self.assertRedirects(response, '/login/?next=/expenses/')

    def test_expense_list_shows_only_user_expenses(self):
        other_user = User.objects.create_user(username='otheruser', password='otherpass')
        Category.objects.create(user=other_user, category='Other Cat')
        Expense.objects.create(
            user=other_user,
            description='Not your business',
            amount=100,
            date='2025-05-02',
            category=self.category
        )

        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('expense-list'))
        self.assertContains(response, 'Test Expense')
        self.assertNotContains(response, 'Not your business')

    def test_create_expense(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('expense-create'), {
            'description': 'Groceries',
            'amount': 75,
            'date': '2025-05-03',
            'category': self.category.id
        })
        self.assertEqual(Expense.objects.count(), 2)
        self.assertRedirects(response, reverse('expense-list'))

    def test_register_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'aComplexPass123!',
            'password2': 'aComplexPass123!',
        })
        self.assertEqual(User.objects.count(), 2)  # testuser, otheruser, newuser
        self.assertRedirects(response, reverse('login'))
