from fastapi import APIRouter
from app.models.cliente_model import ClienteIn, ClienteUpdate
from app.services import cliente_service

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

@router.post("/")
async def crear(cliente: ClienteIn):
    return await cliente_service.crear_cliente(cliente)

@router.get("/")
async def listar():
    return await cliente_service.listar_clientes()

@router.get("/{id}")
async def obtener(id: str):
    return await cliente_service.obtener_cliente(id)

@router.put("/{id}")
async def actualizar(id: str, datos: ClienteUpdate):
    return await cliente_service.actualizar_cliente(id, datos)

@router.delete("/{id}")
async def eliminar(id: str):
    return await cliente_service.eliminar_cliente(id)