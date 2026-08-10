from fastapi import FastAPI

app = FastAPI(title="DevOps Demo API")


@app.get("/")
def root():
    return {
        "message": "Hello DevOps!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
