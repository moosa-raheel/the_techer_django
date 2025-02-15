# The Techer

## A website for learning Django custom authentication and autherization

Recently I learn custom authentication and autherization in Django, so I decide to build something so I decide to build this application

### For Run this Project in your Computer

- First clone repository

```bash
git clone https://github.com/moosa-raheel/the_techer_django
```

- Then get in to the folder

```bash
cd the_techer_django
```

- Then create virtual environment and activate it

```bash
pip3 install virtualenv
virtualenv env
source env/bin/activate
```

- Then install all packages using requirements.txt file

```bash
pip3 install -r requirements.txt
```

- Then create .env file and declare following variables

| S.no | variable | value |
|:------:|:----------:|:-------:|
| 1    |EMAIL_HOST|Email host name |
| 2    |EMAIL_HOST_USER|Email host user |
| 3    |EMAIL_HOST_PASSWORD|Email host password |
| 4    |EMAIL_PORT|Email port |
| 5    |ADMIN_EMAIL|Admin email |

- Then start a server

```bash
python3 manage.py runserver
```
