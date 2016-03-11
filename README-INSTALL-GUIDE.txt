To install dependencies (Django 1.8 and Pillow), create a virtual environment, then run;
pip install -r requirements.txt

To initialise the database run:
python scs_project/manage.py migrate

FInally, to run the webserver, enter the command:
python scs_project/manage.py runserver

The website should now be hosted at:
localhost:8000

If this does not work, I have deployed a version of the website at:
http://scotthood.pythonanywhere.com/

The code is hosted at:
http://www.github.com/hoodscott/FMECAngo