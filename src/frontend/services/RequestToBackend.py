import requests
import streamlit as st
import os
import asyncio
import aiohttp


class BackendService:
    def __init__(self):
        self.backend_url = os.getenv("BASE_URL")
        self.api_token = os.getenv("API_KEY")

    def get_data_from_backend(self, endpoint):
        try:
            if not self.api_token:
                st.error("Erro: API Token não está definido. Por favor, inclua o token na URL como parâmetro 'token'.")
                return []
            headers = {
                "Authorization": f"Bearer {self.api_token}"
            }
            response = requests.get(f"{self.backend_url}{endpoint}", headers=headers)
            if response.status_code == 200:
                return response.json().get("data", [])
            elif response.status_code == 401:
                st.error("Erro ao obter dados do backend: 401 - Não autorizado. Verifique o token de autenticação.")
            else:
                st.error(f"Erro ao obter dados do backend: {response.status_code}")
            return []
        except requests.exceptions.RequestException as e:
            st.error(f"Erro de conexão com o backend: {e}")
            return []
        
    async def fetch_data(self, session, endpoint):
        """Fetch data from a single endpoint."""
        
        headers = {"Authorization": f"Bearer {self.api_token}"}
        try:
            async with session.get(f"{self.backend_url}{endpoint}", headers=headers) as response:
                response.raise_for_status()
                return await response.json()
        except Exception as e:
            st.error(f"Erro ao carregar {endpoint}: {e}")
            return None

    async def fetch_all_data(self, endpoints):
        """Fetch all data concurrently."""
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_data(session, endpoint) for endpoint in endpoints.values()]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return {key: result for key, result in zip(endpoints.keys(), results)}


