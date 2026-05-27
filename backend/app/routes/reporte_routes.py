from fastapi import APIRouter
from app.services import reporte_service

router = APIRouter(
    prefix="/reportes",
    tags=["Reportes"]
)

@router.get("/total-envios")
async def total():
    return await reporte_service.total_envios()

@router.get("/promedio-valor")
async def promedio():
    return await reporte_service.promedio_valor()

@router.get("/max-valor")
async def maximo():
    return await reporte_service.max_valor()

@router.get("/min-valor")
async def minimo():
    return await reporte_service.min_valor()

@router.get("/envios-por-estado")
async def estados():
    return await reporte_service.envios_por_estado()