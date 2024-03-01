### To Run this Project on your local machine

#### 1. create a virtual environment of python in directory of your choice (the command below creates a venv with the python installed in your system in your current directory)
```bash
python -m venv venv
```

#### 2. clone this directory in a directory of your choice
```bash
git clone https://github.com/thedevhack/TranslateR.git
cd TranslateR
```

#### 3. install the required dependinces in your python virtual environment(activate virtualenv) using
```bash
pip install -r requirements.txt
```

#### 4. Create a env.dev file in your current directory
```bash
touch env.dev
```

##### The contents of env.dev file are
```bash
DATABASE_URL="<your_postgres_db_url>"
DJANGO_SECRET_KEY="django-insecure-8tury6rw($r&f76f4)p5!-&i261cv)jcc)a+@f47+q2bhm@jc9"
DJANGO_DEBUG=1
ALLOWED_HOST=*
SITE_ID=1
GOOGLE_APPLICATION_CREDENTIALS="<path/to/authentication.json>"
```

#### 5. For authentication.json you need to get a API creds from google translate by registering for the API [https://cloud.google.com/translate/docs/reference/rest]

#### 6. Run the migrate and setup sites with google authentication and run migrations

For sites - you need to 

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
# NOTE
1. For sites - you need to change domain name from example.com to localhost or your domain if you are hosting whic can be done by admin of django.
2. For database - you can ignore postgres just comment the db.py file and the server will start using django internal sqlite db.
3. For actual translation to work you need to get Google Cloud Translation API credentials and store it in TranslateR folder (i.e Project Folder) with name "authentication.json".
4. Login Button is not visible on mobile so please adjust with it.
5. without env file the project won't run so please create a env file in ptoject folder (i.e. TranslateR)
6. For google auth to work you need to add google authentication from [https://console.cloud.google.com/apis/credentials] the client id and client secret you get from creating a Oauth 2.0 client id will need to added in social apps from admin of django
