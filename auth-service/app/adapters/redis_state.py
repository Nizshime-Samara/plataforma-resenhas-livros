import httpx
import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)

UPSTASH_REDIS_URL = os.getenv("UPSTASH_REDIS_REST_URL")
UPSTASH_REDIS_TOKEN = os.getenv("UPSTASH_REDIS_REST_TOKEN")

if not UPSTASH_REDIS_URL or not UPSTASH_REDIS_TOKEN:
    raise RuntimeError("❌ Variáveis de ambiente do Redis não configuradas corretamente.")

HEADERS = {
    "Authorization": f"Bearer {UPSTASH_REDIS_TOKEN}",
    "Content-Type": "application/json"
}

DEFAULT_TTL = 300  # 5 minutos

async def save_state(key: str, value: str, ttl: int = DEFAULT_TTL) -> bool:
    """
    Salva o valor no Redis com TTL.
    """
    try:
        logger.info(f"📝 Salvando chave {key} no Redis com TTL de {ttl}s")
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.post(
                f"{UPSTASH_REDIS_URL}/set/{key}",
                headers=HEADERS,
                json={"value": value, "ex": ttl}
            )
            if response.status_code != 200:
                logger.error(f"❌ Falha ao salvar no Redis: {response.text}")
            return response.status_code == 200
    except httpx.RequestError as e:
        logger.exception(f"❌ Erro de requisição ao salvar state no Redis: {e}")
        return False

async def get_state(key: str) -> Optional[str]:
    """
    Recupera o valor salvo no Redis para a chave.
    """
    try:
        logger.info(f"🔍 Buscando chave {key} no Redis")
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(
                f"{UPSTASH_REDIS_URL}/get/{key}",
                headers=HEADERS
            )
            if response.status_code == 200:
                value = response.json().get("result")
                logger.info(f"✅ Valor obtido: {value}")
                return value
            else:
                logger.warning(f"⚠️ Chave {key} não encontrada ou expirada")
    except httpx.RequestError as e:
        logger.exception(f"❌ Erro de requisição ao recuperar state do Redis: {e}")
    return None
