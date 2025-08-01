# Django API Boilerplate

![Django](https://img.shields.io/badge/Django-5.2.4-green?logo=django)
![DRF](https://img.shields.io/badge/DRF-3.16.0-red?logo=django)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Tests](https://img.shields.io/badge/tests-25%20passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

A comprehensive Django API boilerplate with a complete testing framework including unit tests, API tests, and UI tests using Selenium. Perfect for jumpstarting Django projects with a solid testing foundation.

## ✨ Features

- 🏗️ **Django 5.2.4** with Django REST Framework
- 👤 **Custom User Model** with extended fields
- 🔐 **Authentication** and permissions setup
- 📊 **API endpoints** with proper serialization
- 🎨 **Basic UI** with responsive templates
- 🧪 **Comprehensive Testing Suite**:
  - Unit tests for models and business logic
  - API tests with authentication
  - UI tests with Selenium WebDriver
  - View tests for template rendering
  - Modular test organization
- 📈 **Test Coverage** reporting
- 🔧 **Pytest & Django TestCase** support
- 📱 **Admin interface** configuration
- 🚀 **CI/CD Pipeline** with GitHub Actions:
  - Automated testing on multiple Python versions
  - Code quality checks (linting, formatting)
  - Security scanning with bandit and safety
  - Coverage reporting to Codecov
  - Automated deployment to production
- 🐳 **Docker Support** for containerized deployment
- ⚙️ **Environment Configuration** with .env support
- 🎯 **Production-ready** structure

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/FernandoZnga/django-api-boilerplate.git
cd django-api-boilerplate

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

## 🧪 Running Tests

### All Tests
```bash
# Using Django's test runner
python manage.py test --verbosity=2

# Using pytest
python -m pytest -v

# With coverage
python -m pytest --cov=core --cov-report=term-missing
```

### Specific Test Categories
```bash
# Model tests only
python -m pytest core/tests/test_models.py -v

# API tests only
python -m pytest core/tests/test_api.py -v

# View tests only
python -m pytest core/tests/test_views.py -v

# UI tests only (requires Chrome/ChromeDriver)
python -m pytest core/tests/test_ui.py -v

# Run specific test classes
python -m pytest core/tests/test_models.py::UserModelTest -v
python -m pytest core/tests/test_models.py::TaskModelTest -v
python -m pytest core/tests/test_api.py::APITest -v
python -m pytest core/tests/test_views.py::ViewsTest -v
python -m pytest core/tests/test_ui.py::UITest -v
```

## 🏗️ Project Structure

```
django_api_boilerplate/
├── core/                          # Main application
│   ├── models.py                  # User and Task models
│   ├── views.py                   # API and traditional views
│   ├── serializers.py             # DRF serializers
│   ├── urls.py                    # URL configurations
│   ├── admin.py                   # Admin interface setup
│   ├── tests/                     # Modular test suite
│   │   ├── __init__.py            # Test package init
│   │   ├── test_models.py         # Model unit tests
│   │   ├── test_api.py            # API endpoint tests
│   │   ├── test_views.py          # View/template tests
│   │   └── test_ui.py             # Selenium UI tests
│   └── templates/
│       └── core/                  # HTML templates
│           ├── base.html
│           ├── home.html
│           └── tasks.html
├── django_api_boilerplate/        # Project settings
│   ├── settings.py                # Django configuration
│   └── urls.py                    # Root URL config
├── requirements.txt               # Dependencies
├── pytest.ini                    # Pytest configuration
└── manage.py                      # Django management
```

