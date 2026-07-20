1. pip install fastapi
2. mysite/
3. mysite/ --> admin, --> __init__.py
              api, --> __init__.py
              db, --> __init__.py
4. db/  --> database.py
           models.py
           schema.py
5. db/
    5.1 database.py
    5.2 pip install sqlalchemy
    5.3 database.py --> (FastAPI + db)
    5.4 models.py --> (Mapped, mapped_column)
    5.5 schema.py --> (2x validation),
                    schema.py --> views.py -> 20%
                              --> serializer -> 80%
6. --> PostgreSQL
    pip install alembic --> ORM
    6.1 alembic -> models.py(class) --> migration(db)
    6.2 alembic init migrations
    6.3 migrations -> env (models *)
                   -> alembic.ini -> (DB_URL)
    6.4 alembic upgrade head
    6.5 alembic revision --autogenerate
7. api/
    7.1 category/ --> CRUD

8. pip install uvicorn
        --> uvicorn main:wildberies_app
        --> uvicorn main:wildberies_app --reload
9. Authorization
            jwt_token