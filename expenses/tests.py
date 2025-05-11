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


class TestCategoryViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.other_user = User.objects.create_user(username='seconduser', password='secondpassword')

    def test_create_category(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('category-create'), {
            'category': 'groceries'
        })
        self.assertEqual(Category.objects.count(), 1)
        self.assertRedirects(response, reverse('category-list'))

    def test_category_list_user_filtering(self):
        Category.objects.create(user=self.user, category='my stuff')
        Category.objects.create(user=self.other_user, category='not mine')

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('category-list'))

        self.assertContains(response, 'my stuff')
        self.assertNotContains(response, 'not mine')

    def test_update_category(self):
        category = Category.objects.create(user=self.user, category='Old Name')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('category-update', args=[category.pk]), {
            'category': 'New Name'
        })
        category.refresh_from_db()
        self.assertEqual(category.category, 'New Name')
        self.assertRedirects(response, reverse('category-list'))

    def test_delete_category(self):
        category = Category.objects.create(user=self.user, category='To Delete')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('category-delete', args=[category.pk]))
        self.assertEqual(Category.objects.count(), 0)
        self.assertRedirects(response, reverse('category-list'))

    def test_login_required_for_category_list(self):
        response = self.client.get(reverse('category-list'))
        self.assertRedirects(response, '/login/?next=/expenses/categories/')

    def test_category_form_rejects_blank_submission(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('category-create'), {})

        self.assertEqual(Category.objects.count(), 0)
        self.assertEqual(response.status_code, 200)

    def test_user_cannot_edit_another_users_category(self):
        category = Category.objects.create(user=self.other_user, category='dont touch')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('category-update', args=[category.pk]), {
            'category': 'try to touch'
        })

        self.assertEqual(response.status_code, 404)

    def test_delete_nonexistent_category_returns_404(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('category-delete', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_user_only_sees_their_own_categories(self):
        category1 = Category.objects.create(user=self.user, category='my data')
        category2 = Category.objects.create(user=self.other_user, category='not mine')

        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('category-list'))

        self.assertContains(response, 'my data')
        self.assertNotContains(response, 'not mine')





