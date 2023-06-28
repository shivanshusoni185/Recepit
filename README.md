Problem statement11:-

Develop a reporting utility for generating customized PDF and XLSX reports by extracting data from a database,
in-memory data, external systems like Mambu, or through APIs. The utility should allow users to define report
templates with corresponding queries or logic to retrieve the reqta. Users should also be able to provide 
input parameters to further customize the report generation process. The objectiuired dave is to create a flexible and 
efficient reporting solution that can seamlessly retrieve data from various sources and generate professional-looking 
reports in PDF or XLSX format. The challenge is to design and implement his reporting utility with focusing on data 
retrieval mechanisms, template customization, and output generation in tthe desired file formats.
=========================================================================================================
For this we are using python with django framework

Requirements:-
Python3.9
install django framework
IDE(VSCode or PyCharm)
Required a aws account for send file in s3 bucket
follow this link for setup of s3 bucket-->

Make sure your path is added in the environoment variables
====================================================================================================================

Create a folder->Name_of_folder
open this folder inside vscode , once the folder is open 
Install django Inside it,Use django so, you need to install django on your folder use this command ,

*pip install django

we also need so more libary like boto3,requests,reportlab to install this use these commands
pip install boto3
pip install reportlab
pip install requests
====================================================================================================================
After all installation we need create our django project so create django project use this command 

django-admin startproject Name_of_project

once you hit enter it creates somefile for you like 
asgi.py
urls.py
settings.py
wsgi.py

we create some more files as well like :-
models.py
views.py
admin.py

This is the basic structure of django project structure 

***We also need a one Template folder where we can put our all the .html .css page and file 
=========================================================================================================================
settings.py
Update your settings INSTALLED_APPS but your project inside INSTALLED_APPS 
example INSTALLED_APPS=['Name_of_project',]

Update Templates DIR as well
 TEMPLATES = [
    {
        
        'DIRS': [os.path.join(BASE_DIR, '/Templates')],

If your want to upload your files in s3 bucket so bucket this in last of settings files as well you not want to upload in s3 so leave it as it 

AWS_ACCESS_KEY_ID ='*****'
AWS_SECRET_ACCESS_KEY = '*****************'
AWS_STORAGE_BUCKET_NAME = '**************'
AWS_S3_SIGNATURE_NAME = '*****',
AWS_S3_REGION_NAME = '******'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
============================================================================================================================

Models.py:-This file is used for Database Here we can define what kind of database field is required .

Once Model.py is done register it into the Admnin.py(admin.site.register(Name_of_model)) take name of model form models.py 

perform migration as well perfrom migration we need to follow this commands

python manage.py runserver makemigrations Name_of_Project #That you register in a settings

python manage.py migrate 

once this commands run sucessfully that means database created sucessfully
========================================================================================================================================

urls.py

In this file we can declared all the path for urls


===========================================================================================================================================
views.py

This is the important file of django app here we can put all the custom logic in the form of functions and connected this functions with urls.py
================================================================================================================================================
To run this project locate a manage.py in project folder and use this command
python manage.py runserver
This is the entire structure how we can create and configure django project 

=============================================================================================================================================




















