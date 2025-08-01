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
├── .github/                       # GitHub Actions workflows
│   └── workflows/
│       ├── ci.yml                 # CI pipeline (testing, linting, security)
│       └── deploy.yml             # Deployment pipeline
├── core/                          # Main application
│   ├── migrations/                # Database migrations
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── templates/
│   │   └── core/                  # HTML templates
│   │       ├── base.html
│   │       ├── home.html
│   │       └── tasks.html
│   ├── tests/                     # Modular test suite
│   │   ├── __init__.py            # Test package init
│   │   ├── test_models.py         # Model unit tests
│   │   ├── test_api.py            # API endpoint tests
│   │   ├── test_views.py          # View/template tests
│   │   └── test_ui.py             # Selenium UI tests
│   ├── __init__.py
│   ├── admin.py                   # Admin interface setup
│   ├── apps.py                    # App configuration
│   ├── models.py                  # User and Task models
│   ├── serializers.py             # DRF serializers
│   ├── urls.py                    # URL configurations
│   └── views.py                   # API and traditional views
├── django_api_boilerplate/        # Project settings
│   ├── __init__.py
│   ├── asgi.py                    # ASGI configuration
│   ├── settings.py                # Django configuration
│   ├── urls.py                    # Root URL config
│   └── wsgi.py                    # WSGI configuration
├── .env.example                   # Environment variables template
├── .flake8                        # Flake8 linting configuration
├── .gitignore                     # Git ignore patterns
├── Dockerfile                     # Docker container configuration
├── README.md                      # Project documentation
├── manage.py                      # Django management
├── pyproject.toml                 # Tool configurations (black, isort, pytest)
├── pytest.ini                    # Pytest configuration
└── requirements.txt               # Dependencies
```

## ⚙️ Environment Setup

### Local Development
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your settings
# Update SECRET_KEY, DATABASE_URL, etc.
```

### Environment Variables
The `.env.example` file contains all available environment variables:
- `SECRET_KEY` - Django secret key (required)
- `DEBUG` - Debug mode (default: True for development)
- `DATABASE_URL` - Database connection string
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- Email, static files, security, and third-party service configurations

## 🚀 CI/CD Pipeline

### GitHub Actions Workflows

#### CI Workflow (`.github/workflows/ci.yml`)
- **Triggers**: Push/PR to `main` and `develop` branches
- **Testing**: Multi-Python version testing (3.8-3.11)
- **Quality**: Code linting with flake8, black, isort
- **Security**: Vulnerability scanning with bandit and safety
- **Coverage**: Automated coverage reporting to Codecov

#### Deployment Workflow (`.github/workflows/deploy.yml`)
- **Triggers**: Push to `main` branch or version tags
- **Testing**: Pre-deployment test validation
- **Docker**: Automated container building and registry push
- **Production**: Environment-specific deployment

### Required GitHub Secrets
For deployment workflow to work, configure these repository secrets:
```
SECRET_KEY=your-django-secret-key
DOCKER_USERNAME=your-docker-hub-username
DOCKER_PASSWORD=your-docker-hub-password-or-token
```

## 🐳 Docker Deployment

### Build and Run Locally
```bash
# Build the Docker image
docker build -t django-api-boilerplate .

# Run the container
docker run -p 8000:8000 -e SECRET_KEY=your-secret-key django-api-boilerplate
```

### Production Deployment
```bash
# Pull from registry (after CI/CD push)
docker pull django-api-boilerplate:latest

# Run with environment file
docker run -p 8000:8000 --env-file .env django-api-boilerplate:latest
```

### Docker Compose (Optional)
Create a `docker-compose.yml` for local development:
```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    volumes:
      - .:/app
    command: python manage.py runserver 0.0.0.0:8000
```

## 🔧 Code Quality

### Formatting and Linting
```bash
# Format code with black
black .

# Sort imports with isort
isort .

# Lint with flake8
flake8 .

# Security scan with bandit
bandit -r .

# Check dependencies with safety
safety check
```

### Pre-commit Setup (Optional)
```bash
# Install pre-commit
pip install pre-commit

# Install git hooks
pre-commit install
```

