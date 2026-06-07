from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Good Day Vibeee", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "ok"}