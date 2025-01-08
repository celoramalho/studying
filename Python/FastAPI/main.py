from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_root():
    return {"message": "Hello World"}


# docs  to enter in Swagger UI: Exemple -> http://127.0.0.1:8000/docs