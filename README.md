# custom_c4d_03_feb15
User = CustomUser(AbstractUser) and a Profile OneToOneField. 


CustomUser is enabled but nothing from the AbstractUser is implemented. 
To configure email and password only for sign-in, allauth installed with these constants in settings.py 

ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_EMAIL_REQUIRED = True


The built-in templates allauth comes with can be overwritten to allow for htmx, alpine and styling to be applied. 

Django for Professionals, Chapter 10 Page 149 outlines how to go about this.
