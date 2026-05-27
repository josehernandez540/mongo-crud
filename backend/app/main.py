from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import cliente_routes, reporte_routes

app = FastAPI(
    title="Transportadora API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cliente_routes.router)
app.include_router(reporte_routes.router)

@app.get("/")
async def root():
    return {
        "mensaje": "API funcionando correctamente"
    }