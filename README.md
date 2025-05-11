# BudgetBuddy 

**BudgetBuddy** is a personal expense tracking application built with Django.
It allows users to log expenses, categorize them, and view their data in a clean, user-specific dashboard.
This project demonstrates full CRUD functionality, user authentication, access control, and automated testing.

---

##  Features

- User registration and login/logout
- Create, update, and delete personal expense records
- Create and manage custom spending categories
- Expenses are tied to each user and private by default
- Class-based views (CBVs) for clean, maintainable logic
- Basic styling and responsive layout with custom CSS
- Full test suite for key views (creation, listing, security)

---

##  Tech Stack

- Python 3.7+
- Django 3.2
- SQLite (default dev DB)
- HTML, CSS (basic)
- Pytest/Django TestCase for testing

---

## ⚙ Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/BudgetBuddy.git
   cd BudgetBuddy
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

6. (Optional) Run tests:

   ```bash
   python manage.py test
   ```

---

##  User Authentication

- Users must register and log in to manage expenses and categories.
- All views are protected with `LoginRequiredMixin` and object-level filtering (`get_queryset()`).

---

##  Tests Included

This project includes tests for:
- Expense and Category creation
- Ownership protection (users cannot edit/delete others' data)
- View access restrictions
- Form validation

---

##  Status

**Complete**  


---

## 👤 Author

- Bryon Peabody (Tempe, AZ)
- [LinkedIn](https://www.linkedin.com) 
- [GitHub](https://github.com/BryonPeabody)

---
