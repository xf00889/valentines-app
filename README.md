# Valentine's Day Web Application

A romantic and interactive Valentine's Day web application built with Django and MySQL. Features include love letter writing with background music, photo gallery, and animated elements.

## Features

- Love Letter Writing with Background Music
- Photo Gallery with Lightbox View
- Animated Landing Page
- Responsive Design
- Modern UI with Bootstrap 5

## Prerequisites

- Python 3.8+
- MySQL
- pip

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd valentines_project
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the database in `valentines_project/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',
    }
}
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

## Deployment to PythonAnywhere

1. Create a PythonAnywhere account at https://www.pythonanywhere.com/

2. Upload your code:
```bash
git clone <repository-url>
```

3. Create a virtual environment:
```bash
mkvirtualenv --python=/usr/bin/python3.8 myenv
pip install -r requirements.txt
```

4. Configure MySQL Database:
- Go to the Databases tab
- Create a new database
- Update settings.py with your PythonAnywhere database credentials

5. Configure Web App:
- Go to the Web tab
- Add a new web app
- Choose Manual Configuration
- Set the virtual environment path
- Update WSGI configuration file
- Set STATIC_ROOT and MEDIA_ROOT paths

6. Update settings.py:
- Set DEBUG = False
- Update ALLOWED_HOSTS
- Configure your SECRET_KEY
- Enable security settings

7. Collect static files:
```bash
python manage.py collectstatic
```

8. Apply migrations:
```bash
python manage.py migrate
```

## Environment Variables

Create a `.env` file in the project root with the following variables:
```
DJANGO_SECRET_KEY=your_secret_key
DATABASE_PASSWORD=your_database_password
```

## Security Considerations

- Keep DEBUG = False in production
- Use strong passwords
- Keep secret key secure
- Enable HTTPS
- Configure security settings in settings.py

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.