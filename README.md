# [![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=657&size=24&pause=1000&color=A93226&random=false&width=435&lines=🐾🐾Pets+charity+fund+API🐾🐾)](https://git.io/typing-svg)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pytest](https://img.shields.io/badge/tests-passing-brightgreen?style=flat-square&logo=pytest)
![FastAPI](https://img.shields.io/badge/FastAPI-0.78.0-brightgreen)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.36-red)
![Alembic](https://img.shields.io/badge/Alembic-1.7.7-lightgrey)
![FastAPI Users](https://img.shields.io/badge/FastAPI%20Users-10.0.4-blue)
![Uvicorn](https://img.shields.io/badge/Uvicorn-0.17.6-orange)
![Aiogoogle](https://img.shields.io/badge/Aiogoogle-4.2.0-yellowgreen)
![Status](https://img.shields.io/badge/status-finished-green?style=flat-square)

Extended version of [charity fund app](https://github.com/SemenovaLiza/pets_charity_fund). Added the ability to generate reports in Google Sheets to know which projects are closing the fastest.

## Technologies
- [Python - 3.10](https://www.python.org/) 🐶
- [FastAPI - 0.78.0](https://fastapi.tiangolo.com/) 🐶
- [SQLAlchemy - 1.4.36](http://www.sqlalchemy.org/) 🐶
- [Alembic - 1.7.7](https://alembic.sqlalchemy.org/) 🐶
- [FastAPI Users - 10.0.4](https://fastapi-users.github.io/fastapi-users/)🐶
- [Uvicorn - 0.17.6](https://www.uvicorn.org/) 🐶
- [Aiogoogle - 4.2.0](https://aiogoogle.readthedocs.io/en/latest/index.html) 🐶
## Instructions
Clone the repository:
```
git clone git@github.com:SemenovaLiza/QRkot_spreadsheets.git
```
Create and activate virtual environment:
```
python3 -m venv venv
```
Install requirements.txt, required python version >= 3.9::
```
pip install -r requirements.txt
``` 
Create .env file:
```
touch .env
```
Fill the .env file with your service account details to .env file in order to use Google API:
```
APP_TITLE=QRkot
APP_DESCRIPTION=Сервис поддержки котов
DATABASE_URL='sqlite+aiosqlite:///./fastapi.db'
SECRET=<secret>
FIRST_SUPERUSER_EMAIL=<email superuser>
FIRST_SUPERUSER_PASSWORD=<password superuser>
TYPE=service_account
PROJECT_ID=atomic-climate-<id>
PRIVATE_KEY_ID=<id private key>
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----<private key>-----END PRIVATE KEY-----\n"
CLIENT_EMAIL=<email service account>
CLIENT_ID=<id service account>
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=<link>
EMAIL=<email user>
```
Apply migrations to create an database:
```
alembic init --template async alembic
alembic revision --autogenerate -m "First migration"
alembic upgrade head
```
Run server
```
uvicorn app.main:app --reload
```

## Documentation

Documentation is available when project is running at http://127.0.0.1:8000/docs - automatically generated Swagger documentation.

# Author
Elizaveta Semenova
