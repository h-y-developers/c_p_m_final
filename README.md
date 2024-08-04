# Campus Placement Management System

### Project Setup

- Clone the repo

```
git clone https://github.com/h-y-developers/c_p_m_final.git
```

- Go indside the project

```
cd c_p_m_final
```

- Create virtual environment using virtualenv

```
virtualenv venv
```

If virtualvenv not installed then run below command

```
pip install virtualenv
```

_NOTE_ :- Always start venv before running the project

```
source venv/bin/activate
```

After activating venv install requirements

```
pip install -r requirements.txt
```

Run Migrations

```
python manage.py makemigrations

python manage.py migrate
```

Run server

```
python manage.py runserver
```

## Credentials

### DB Admin Credentials

```
Username :-  db_admin
Password :-  Admin@123
```

### Student Credentials

```
Username :-  18IT401
Password :-  Bvm@12345
```

### Campus admin Credentials

```
Username :-  campus_admin
Password :-  Admin@123
```

## URLs

#### DB Admin Url

```
http://127.0.0.1:8000/admin
```

#### Campus Admin url

```
http://127.0.0.1:8000/c_admin
```

#### Project Starting url

```
http://127.0.0.1:8000/students/login
```
