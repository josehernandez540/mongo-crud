from bson import ObjectId
from fastapi import HTTPException
from app.config.database import db
from app.utils.objectid import str_id


async def crear_cliente(cliente):
    nuevo = cliente.dict()
    resultado = await db.clientes.insert_one(nuevo)
    creado = await db.clientes.find_one({"_id": resultado.inserted_id})

    return str_id(creado)


async def listar_clientes():
    clientes = []
    async for cliente in db.clientes.find():
        clientes.append(str_id(cliente))

    return clientes


async def obtener_cliente(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(400, "ID inválido")

    cliente = await db.clientes.find_one({"_id": ObjectId(id)})

    if not cliente:
        raise HTTPException(404, "Cliente no encontrado")

    return str_id(cliente)


async def actualizar_cliente(id: str, datos):

    if not ObjectId.is_valid(id):
        raise HTTPException(400, "ID inválido")

    campos = {k: v for k, v in datos.dict().items() if v is not None}

    if not campos:
        raise HTTPException(400, "No hay campos para actualizar")

    await db.clientes.update_one({"_id": ObjectId(id)}, {"$set": campos})

    actualizado = await db.clientes.find_one({"_id": ObjectId(id)})

    return str_id(actualizado)


async def eliminar_cliente(id: str):

    if not ObjectId.is_valid(id):
        raise HTTPException(400, "ID inválido")

    resultado = await db.clientes.delete_one({"_id": ObjectId(id)})

    if resultado.deleted_count == 0:
        raise HTTPException(404, "Cliente no encontrado")

    return {"mensaje": "Cliente eliminado correctamente"}
