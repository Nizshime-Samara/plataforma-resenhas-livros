import httpx
import os
from typing import Optional

UPSTASH_REDIS_URL = os.getenv("UPSTASH_REDIS_REST_URL")
UPSTASH_REDIS_TOKEN = os.getenv("UPSTASH_REDIS_REST_TOKEN")

if not UPSTASH_REDIS_URL or not UPSTASH_REDIS_TOKEN:
    raise RuntimeError("❌ Variáveis de ambiente do Redis não configuradas corretamente.")

HEADERS = {
    "Authorization": f"Bearer {UPSTASH_REDIS_TOKEN}",
    "Content-Type": "application/json"
}

async def save_state(session_id: str, state: str, ttl: int = 300) -> bool:
    """
    Armazenando o estado no Redis com TTL (uso de time padrão: 5 minutos).
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{UPSTASH_REDIS_URL}/set/{session_id}",
            headers=HEADERS,
            json={"value": state, "ex": ttl}
        )
        return response.status_code == 200

async def get_state(session_id: str) -> Optional[str]:
    """
    Recuperando o estado salvo no Redis via REST API.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{UPSTASH_REDIS_URL}/get/{session_id}",
            headers=HEADERS
        )
        if response.status_code == 200:
            return response.json().get("result")
        return None
