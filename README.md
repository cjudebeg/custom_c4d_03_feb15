
This Django project is built to test best approaches for handling user models. It isn't in a container and the db is sqlite.

To get started:

# Check the the python-version file. Virtual environment will ideally run python 3.11.3. (running 3.12 and above can complicate install of all-auth) 
run
# pyenv local 3.11.3
if you don't have 3.11.3, run: 
# pyenv install 3.11.3 && pyenv local 3.11.3
then
# python -m venv venv
# source venv/bin/activate
# python -m pip install -r requirements.txt
shouldn't need to run makemigrations or migrate. 
# ./manage.py runserver




Description:

# custom_c4d_03_feb15
User = CustomUser(AbstractUser) and a Profile OneToOneField. 


CustomUser is enabled but nothing from the AbstractUser is implemented. 
To configure email and password only for sign-in, allauth installed with these constants in settings.py 

ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_EMAIL_REQUIRED = True


The built-in templates allauth comes with can be overwritten to allow for htmx, alpine and styling to be applied. 

Django for Professionals, Chapter 10 Page 149 outlines how to go about this.
