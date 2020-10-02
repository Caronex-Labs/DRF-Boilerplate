import os
import shutil

from django.core.management.base import BaseCommand, CommandError
from pip._vendor.distlib.compat import raw_input


class Command(BaseCommand):
    help = "Configures the DRF_Boilerplate interactively."

    project_name = 'DRF_Boilerplate'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("\nGreetings from Caronex Labs!\n\n"))
        self.stdout.write("We will now configure this project interactively...")
        self.stdout.write("Please answer the following questions about your project...\n\n")
        try:
            self.rename_project(*args, **options)
            self.env_setup(*args, **options)
            self.post_configuration(*args, **options)
        except:
            raise CommandError("Something went wrong.")

    def rename_project(self, *args, **options):
        name_input = ''
        validity_flag = False
        while name_input == '' or not validity_flag:
            validity_flag = True
            name_input = raw_input("Enter a valid Django project name: ")

            if name_input.startswith('_'):
                validity_flag = False

            for letter in name_input:
                if not (letter.isalpha() or letter == '_') or letter == ' ':
                    validity_flag = False
                    break

            if not validity_flag:
                self.stdout.write(self.style.ERROR(
                    "\nInvalid project name. Django project names may only contain underscores, letters and numbers. They "
                    "also cannot start with an underscore.\n\n", ))

        self.stdout.write(self.style.SUCCESS("\nFantastic! Renaming project ...\n\n"))

        files_to_rename = ['DRF_Boilerplate/settings.py',
                           'DRF_Boilerplate/wsgi.py',
                           'DRF_Boilerplate/asgi.py',
                           'DRF_Boilerplate/urls.py',
                           'nginx/nginx.conf',
                           'manage.py',
                           'Procfile']

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace("DRF_Boilerplate", name_input)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename("DRF_Boilerplate", name_input)

        self.project_name = name_input

        self.stdout.write(self.style.SUCCESS(
            'Project has been renamed to %s' % name_input))

    def env_setup(self, *args, **options):
        create_env = raw_input("Would you like for us to generate the .env file ? (y/N): ")

        if create_env.lower() in ['y', 'yes']:
            env_file = open(f"{self.project_name}/.env", "w")

            secret_key = raw_input(
                "Please enter the Django Secret Key for this project. You can create one using online tools: ")

            if secret_key != '':
                env_file.write(f"DJANGO_SECRET_KEY={secret_key}\n")

            domain_1 = raw_input(
                "Please enter your production hostname. This will be the domain name to be used in production. (Leave "
                "it blank if you don't have one yet): ")

            env_file.write(f"PROD_HOSTNAME_1={domain_1}\n")

            domain_2 = raw_input(
                "Please enter your hosting hostname. This should be your hosting service's url if it provides one. ("
                "Heroku for example provides one) (Leave "
                "it blank if you don't have one yet): ")

            env_file.write(f"PROD_HOSTNAME_2={domain_2}\n")

            email_host_password = raw_input(
                "Please enter your email host password or API key here. (Leave "
                "it blank if you don't have one yet): ")

            env_file.write(f"EMAIL_HOST_PASSWORD={email_host_password}\n")

            email_host_user = raw_input(
                "Please enter your email host user here. In case of Mailgun, this will be your primary "
                "'no-reply@mail.subdomain.domain.com'. (Leave "
                "it blank if you don't have one yet): ")

            env_file.write(f"EMAIL_HOST_USER={email_host_user}\n")

            email_from = raw_input(
                "Please enter your from email here. This is the email that will be shown to be the source of any "
                "emails sent from the backend. (Leave "
                "it blank if you don't have one yet): ")

            env_file.write(f"EMAIL_FROM={email_from}\n")

            login_redirect = raw_input(
                "Please enter your frontend's Login URL. This is where users will be redirected to after they confirm their Email ID's or change their passwords. (Add "
                "any valid placeholder URL if you don't have one yet): ")

            env_file.write(f"LOGIN_REDIRECT_URL={login_redirect}\n")
            env_file.write(f"LOGIN_URL={login_redirect}\n")


            docker_usage = raw_input("Would you like to use docker for development? (y/N)")

            if docker_usage.lower() in ['y', 'yes']:
                env_file.write(f"DOCKER=1\n")
            else:
                env_file.write(f"DOCKER=0\n")

            heroku_usage = raw_input("Will you be hosting on Heroku? (y/N)")

            if heroku_usage.lower() in ['y', 'yes']:
                env_file.write(f"HEROKU=1\n")
            else:
                env_file.write(f"HEROKU=0\n")

            env_file.write(f"PROD=0")

            self.stdout.write(self.style.SUCCESS(".env file created successfully...\n\n\n"))

        else:
            self.stdout.write("Skipping .env File Creation...\n\n\n")

    def post_configuration(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Configuration completed successfully. Cleaning up...\n\n"))

        # self.stdout.write("Removing Readme...\n\n")
        # try:
        #     if os.path.exists("README.md"):
        #         os.remove("README.md")
        #
        # except OSError as e:
        #     self.stdout.write(
        #         self.style.ERROR(f"Error deleting Readme. Received the following error message: \n {e.strerror}"))
        #
        # self.stdout.write(self.style.SUCCESS("Readme removed successfully\n\n\n"))

        self.stdout.write("Removing IDE/Code-Editor configuration files...\n\n")
        try:
            if os.path.exists(".idea"):
                shutil.rmtree('.idea')

            if os.path.exists(".vscode"):
                shutil.rmtree(".vscode")

        except OSError as e:
            self.stdout.write(self.style.ERROR(
                f"Error deleting IDE/Code-Editor configuration files. Received the following error message: \n "
                f"{e.strerror}"))

        self.stdout.write(self.style.SUCCESS("IDE/Code-Editor configuration files removed successfully\n\n\n"))

        self.stdout.write(self.style.SUCCESS("\n\nCleanup Complete.\n\n"))
        self.stdout.write(
            "Please restart your IDE/Code-Editor before continuing. The Readme has further instructions, "
            "complete those before starting your development.")
