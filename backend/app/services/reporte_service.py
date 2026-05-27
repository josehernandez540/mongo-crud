from app.config.database import db


async def total_envios():
    pipeline = [{"$group": {"_id": None, "totalEnvios": {"$sum": "$valorReportado"}}}]
    resultado = await db.envios.aggregate(pipeline).to_list(1)

    return resultado[0] if resultado else {"totalEnvios": 0}


async def promedio_valor():
    pipeline = [{"$group": {"_id": None, "promedioValor": {"$avg": "$valorReportado"}}}]
    resultado = await db.envios.aggregate(pipeline).to_list(1)

    return resultado[0] if resultado else {"promedioValor": 0}


async def max_valor():
    pipeline = [{"$group": {"_id": None, "mayorValor": {"$max": "$valorReportado"}}}]
    resultado = await db.envios.aggregate(pipeline).to_list(1)

    return resultado[0] if resultado else {"mayorValor": 0}


async def min_valor():
    pipeline = [{"$group": {"_id": None, "menorValor": {"$min": "$valorReportado"}}}]
    resultado = await db.envios.aggregate(pipeline).to_list(1)

    return resultado[0] if resultado else {"menorValor": 0}


async def envios_por_estado():
    pipeline = [{"$group": {"_id": "$estado", "cantidad": {"$sum": 1}}}]

    return await db.envios.aggregate(pipeline).to_list(100)