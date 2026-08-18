from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

app = FastAPI(
    title="DevOps Demo API",
    version="3.0.0"
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
        "message": "Hello DevOps v3!",
        "version": "3.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "3.0.0",
        "environment": "production"
    }


@app.get("/info")
def info():
    return {
        "application": "DevOps Demo API",
        "version": "3.0.0",
        "environment": "production",
        "status": "running"
    }


@app.get("/users")
def get_users():
    return {
        "count": len(users),
        "users": users
    }


@app.get("/users/count")
def get_user_count():
    return {
        "count": len(users)
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


@app.get("/search")
def search_users(
    name: str = Query(..., min_length=1)
):
    results = [
        user
        for user in users
        if name.lower() in user["name"].lower()
    ]

    return {
        "query": name,
        "count": len(results),
        "users": results
    }


@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    new_id = max(
        [u["id"] for u in users],
        default=0
    ) + 1

    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)

    return new_user


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)

            return {
                "message": "User deleted successfully",
                "user": deleted_user
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )