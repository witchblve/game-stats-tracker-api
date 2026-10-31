from fastapi import FastAPI
from routers import players, matches

app = FastAPI(title="Game Stats Tracker API")

# Подключаем роутеры
app.include_router(players.router)
app.include_router(matches.router)

@app.get("/")
def root():
    return {"message": "Welcome to Game Stats Tracker API!"}
