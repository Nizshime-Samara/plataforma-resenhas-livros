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

DEFAULT_TTL = 300  # 5 minutos

async def save_state(session_id: str, state: str, ttl: int = DEFAULT_TTL) -> bool:
    """
    Armazena o 'state' da sessão OAuth no Redis com TTL.
    """
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(
                f"{UPSTASH_REDIS_URL}/set/{session_id}",
                headers=HEADERS,
                json={"value": state, "ex": ttl}
            )
            return response.status_code == 200
    except httpx.RequestError as e:
        print(f"❌ Erro ao salvar state no Redis: {e}")
        return False

async def get_state(session_id: str) -> Optional[str]:
    """
    Recupera o 'state' da sessão salvo no Redis.
    """
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(
                f"{UPSTASH_REDIS_URL}/get/{session_id}",
                headers=HEADERS
            )
            if response.status_code == 200:
                return response.json().get("result")
    except httpx.RequestError as e:
        print(f"❌ Erro ao recuperar state do Redis: {e}")
    return None