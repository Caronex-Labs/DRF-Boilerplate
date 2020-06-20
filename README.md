# Caronex Labs - DRF Boilerplate

## Overview:
> A Django Rest Framework implementation that comes with a set of pre-implemented features commonly seen in most projects.

**Features Implemented:**
1. `django-rest-auth` package implemented along with the common settings and instructions to change them.
2. Custom login and registration serializers for `django-rest-auth` along with instructions on how to modify them.
3. `drf-yasg` package implemented along with the common url patterns to provide Swagger documentation out of the box.
4. A `users_module` along with implementations of `AbstractUser`, `CustomUserManager` and a `UserAdmin` class for Django's Admin Panel. Along with instructions on how to modify all of the above.
5. Email configuration settings, preset to work with `Mailgun` but will work with any provider.
6. `python-dotenv` package implemented and imported into `settings.py`. Information that is commonly stored in an env file has already been moved to the same.
7. A environment file template along with instructions to modify it.
8. A `.gitignore` file preset for Python projects, Visual Studio Code IDE, Jetbrains IDEs and other commonly ignored files. 
9. The boilerplate is preconfigured to be ready to host on `Heroku`. It contains all the necessary packages and the `Procfile`. Along with any settings that need to be configured inside of `settings.py`. 
10. `django-cors-headers` is implemented and the `clickjacking` middleware has been removed to ensure proper performance.
11. `django-filters` is implemented and has been added to the `REST_FRAMEWORK.DEFAULT_FILTER_BACKENDS`.
12. Both `AnonRateThrottle` and `UserRateThrottle` have been implemented along with instructions on how to set the `Throttling Rates`.
13. `DEBUG` set to `False` by default but `Error Propagation` is set to allow logging of errors to the server console even if not in debug mode.

---

## Instructions

1. On the Github Repository of this project, you'll find an option to `Use this template` on the top right.
2. Follow the prompts to create your new repository using this one as a template.
3. Clone your new repository to your local system.
4. After opening your new project inside a text editor or IDE, perform a `global search and replace` on the whole project for the phrase `DRF_Boilerplate` and change it to the name of your new project. 
5. Then change the name of the main app to the name of your project. 
6. Delete your editor config files and restart your IDE. For more detailed instructions, look up '*How to change Django project name*' and follow along.   
7. Create your virtual environment and install all requirements with `pip install -r requirements.txt`
8. Find the `env_template.txt` file inside of your main app directory ( the same directory as the `settings.py` ). Follow the instructions inside of this file. Check the references section for support.
9. Go to the `settings.py` file and read through it. There are comments indicating any modifications you might want to make.
10. Go through every file inside of the `users_module` app and follow any instructions that apply to you.
11. Go through the templates provided, they contain instructions as well. These are generally the templates pertaining to the emails sent and the email confirmation pages. 
12. Make migrations with the command: `python manage.py makemigrations` and then the command `python manage.py makemigrations users_module` and then apply them with `python manage.py migrate`
13. You then need to run the command: `python manage.py collectstatic` in order to collect and store the static files needed for the Admin panel. If you want to avoid doing this for some reason, you can also just set `DEBUG=True` in the `settings.py` file. 
14. Before you continue to build your project, check the `Admin Panel` ('`/admin/`') and the `swagger documentation` ('`/docs/`') to ensure that the boilerplate has set up successfully. You will have to run the command `python manage.py createsuperuser` in order to access the Admin Panel.

---

## References

- [`django-rest-auth`](https://django-rest-auth.readthedocs.io/en/latest/introduction.html)
- [`drf-yasg`](https://django-au-restth.readthedocs.io/en/latest/introduction.html)
- [`django-cors-headers`](https://pypi.org/project/django-cors-headers/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- [Configuring Django apps for Heroku](https://devcenter.heroku.com/articles/django-app-configuration)
- [Configuring Mailgun for Django](https://simpleisbetterthancomplex.com/tutorial/2017/05/27/how-to-configure-mailgun-to-send-emails-in-a-django-app.html)
- [Secret Key Generator for Django](https://miniwebtool.com/django-secret-key-generator/)
- [How to setup a Custom User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html)

---

## Roadmap

- Amazon AWS Buckets configuration
- `django-rest-auth` OAuth implementation
- A demo project inside the template
- A custom manage.py command to set the project up interactively.
