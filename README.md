# Valentine's Day Web Application 💝

A romantic and interactive Valentine's Day web application built with Django and MySQL. Features include love letter writing with background music, photo gallery with lightbox view, and animated elements.

## 📌 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Dependencies](#-dependencies)
- [Quick Start](#-quick-start)
- [Deployment](#-deployment-to-pythonanywhere)
- [Security](#-security-considerations)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## ✨ Features

- 💌 Love Letter Writing with Background Music
- 🖼️ Photo Gallery with Lightbox View
- 💕 Animated Landing Page with Floating Hearts
- 📱 Fully Responsive Design
- 🎨 Modern UI with Bootstrap 5
- 🎵 Background Music Support
- 💫 Smooth Animations and Transitions

## 🛠️ Prerequisites

- Python 3.8+
- MySQL 5.7+
- pip (Python package manager)
- Git (for version control)

## 📦 Dependencies

Main dependencies include:
```
Django==5.1.5
mysqlclient==2.2.7
Pillow==11.1.0
django-crispy-forms==2.3
crispy-bootstrap5==2024.10
python-dotenv==1.0.1
```

For a complete list of dependencies, see `requirements.txt`.

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/xf00889/valentines-app.git
cd valentines-app
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root:
```env
DJANGO_SECRET_KEY=your_secret_key_here
DATABASE_PASSWORD=your_database_password
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Configure the database in `valentines_project/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'valentines_db',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to see the application.

## 🌐 Deployment to PythonAnywhere

1. Sign up for a PythonAnywhere account at https://www.pythonanywhere.com/

2. From your PythonAnywhere dashboard:
   ```bash
   # Clone the repository
   git clone https://github.com/xf00889/valentines-app.git
   
   # Create virtual environment
   mkvirtualenv --python=/usr/bin/python3.8 valentines_env
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. Configure MySQL Database:
   - Go to the Databases tab
   - Create a new database named `yourusername$valentines_db`
   - Note your MySQL hostname: `yourusername.mysql.pythonanywhere-services.com`

4. Update `valentines_project/settings.py`:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
   
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'yourusername$valentines_db',
           'USER': 'yourusername',
           'PASSWORD': 'your_database_password',
           'HOST': 'yourusername.mysql.pythonanywhere-services.com',
       }
   }
   ```

5. Set up your Web app:
   - Go to Web tab → Add a new web app
   - Choose Manual Configuration → Python 3.8
   - Set Virtual Environment: `/home/yourusername/.virtualenvs/valentines_env`
   - Set Source Code: `/home/yourusername/valentines-app`

6. Configure WSGI file:
   ```python
   import os
   import sys
   
   path = '/home/yourusername/valentines-app'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'valentines_project.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

7. Set up static files:
   ```bash
   python manage.py collectstatic
   ```
   
   In Web tab, add:
   - URL: /static/
   - Directory: /home/yourusername/valentines-app/static

8. Apply migrations and create superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

## 🔒 Security Considerations

- Keep `DEBUG = False` in production
- Use strong, unique passwords
- Store sensitive information in environment variables
- Enable HTTPS (automatically handled by PythonAnywhere)
- Regularly update dependencies
- Back up your database regularly
- Set appropriate file permissions
- Configure proper CORS headers if needed
- Implement rate limiting for API endpoints

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read our [Contributing Guidelines](.github/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 🐛 Bug Reports and Feature Requests

- For bug reports, please use our [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md)
- For feature requests, please use our [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Bootstrap 5 for the responsive design
- Font Awesome for icons
- Google Fonts for typography
- Django community for the amazing framework
- All our contributors and users

## 📊 Project Status

This project is actively maintained. For the latest updates and planned features, check our [Issues](https://github.com/xf00889/valentines-app/issues) page.

## 📧 Contact

For questions and support, please:
1. Check our [FAQ](docs/FAQ.md) first
2. Search existing [Issues](https://github.com/xf00889/valentines-app/issues)
3. Open a new issue if needed