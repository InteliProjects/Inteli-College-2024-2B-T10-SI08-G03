import os
import asyncio
import aiohttp

endpoints = {
    "qtd_viagens_por_linha": "/api/qtd_viagens_por_linha",
    "qtd_viagens_semana_linha": "/api/qtd_viagens_semana_linha",
    "taxa_atraso": "/api/taxa_atraso",
    "duracao_media": "/api/duracao_media",
    "duracao_real_programada": "/api/duracao_real_programada",
    "viagens_por_dia_mes": "/api/viagens_por_dia_mes",
    "alertas_pcd_por_linha": "/api/alertas_pcd_por_linha",
    "qtd_pcd_por_dia": "/api/qtd_pcd_por_dia",
    "qtd_pcd_semana_linha": "/api/qtd_pcd_semana_linha"
}
backend_url = "http://localhost:5000"

async def fetch_data(session, endpoint):
    """Fetch data from a single endpoint."""
    
    token = "BIGGIE123!"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        async with session.get(f"{backend_url}{endpoint}", headers=headers) as response:
            response.raise_for_status()
            return await response.json()
    except Exception as e:
        print(f"Erro ao carregar {endpoint}: {e}")
        return None

async def fetch_all_data():
    """Fetch all data concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, endpoint) for endpoint in endpoints.values()]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return {key: result for key, result in zip(endpoints.keys(), results)}
    
    
    
data = asyncio.run(fetch_all_data())

print(data)