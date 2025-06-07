from fastapi import FastAPI
from .routers import fitness_class

app = FastAPI()

app.include_router(fitness_class.router)
