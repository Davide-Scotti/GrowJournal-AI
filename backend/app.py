from fastapi import FastAPI
from routes import log_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS per il frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # cambierai questo in produzione
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Includi il router dei log
app.include_router(log_routes.router, prefix="/logs")