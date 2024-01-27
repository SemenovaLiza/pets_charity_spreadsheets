# API service for QR-Кот cat charitable foundation && QRkot_spreadseets.
 Google API has been added so that the foundation's volunteers know which projects are closing the fastest. This will help them identify projects that need additional advertising.

QR-Кот is a training project of the application API for the QRKot Cat Charitable Foundation. Its purpose is to collect and distribute donations among various charity projects.

## Technologies
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](http://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [FastAPI Users](https://fastapi-users.github.io/fastapi-users/)
- [Uvicorn](https://www.uvicorn.org/)
## Instructions
Clone the repository:
```
git clone git@github.com:SemenovaLiza/cat_charity_fund.git
```
Create and activate virtual environment:
```
python -m venv venv
```
Install requirements.txt:
```
pip install -r requirements.txt
``` 
Create .env file:
```
touch .env
```
Fill the .env file:
```
APP_TITLE=App_title
DESCRIPTION=Description
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=Secret
FIRST_SUPERUSER_EMAIL=login@email.com
FIRST_SUPERUSER_PASSWORD=password
```
Make migrations file
```
alembic revision --autogenerate -m "First migration" 
```
Run migrations
```
alembic upgrade head
```
Run server
```
uvicorn app.main:app --reload
```

## Documentation

Download project's documentation openapi.json:

To view the documentation, upload the file to the website https://redocly.github.io/redoc/. There is a **Upload a file** button at the top of the page, click it and upload the downloaded file. The project specification will be displayed in Doc format.
