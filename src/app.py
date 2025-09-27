from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Ask My Data API is running 🚀"}
