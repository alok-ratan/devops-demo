from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="DevOps Demo API",
    version="1.0.0"
)


class UserCreate(BaseModel):
    name: str
    email: str


users = [
    {
        "id": 1,
        "name": "Alok",
        "email": "alok@example.com"
    },
    {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@example.com"
    }
]


@app.get("/")
def root():
    return {
        "message": "Hello DevOps v2!",
        "version": "2.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0",
        "environment": "production"
    }


@app.get("/users")
def get_users():
    return {
        "count": len(users),
        "users": users
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    new_id = max([u["id"] for u in users], default=0) + 1

    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)

    return new_user