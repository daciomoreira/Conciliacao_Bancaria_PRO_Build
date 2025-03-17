"""
Módulo de cache para o sistema de Conciliação Bancária.
"""

import os
import json
import pickle
from datetime import datetime, timedelta
from typing import Any, Optional
import hashlib

# Importar configurações
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config.settings import CACHE_TIMEOUT_MINUTES, TEMP_DIR
from src.utils.logger import logger

class Cache:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Cache, cls).__new__(cls)
            cls._instance._initialize_cache()
        return cls._instance
    
    def _initialize_cache(self):
        """Inicializa o sistema de cache."""
        self.cache_dir = os.path.join(TEMP_DIR, 'cache')
        os.makedirs(self.cache_dir, exist_ok=True)
        self._clean_expired_cache()
    
    def _get_cache_path(self, key: str) -> str:
        """Retorna o caminho do arquivo de cache para a chave."""
        # Criar hash da chave para evitar problemas com caracteres especiais
        key_hash = hashlib.md5(key.encode()).hexdigest()
        return os.path.join(self.cache_dir, f"{key_hash}.cache")
    
    def _clean_expired_cache(self):
        """Remove arquivos de cache expirados."""
        try:
            now = datetime.now()
            for filename in os.listdir(self.cache_dir):
                filepath = os.path.join(self.cache_dir, filename)
                if os.path.isfile(filepath):
                    # Verificar data de modificação do arquivo
                    mtime = datetime.fromtimestamp(os.path.getmtime(filepath))
                    if now - mtime > timedelta(minutes=CACHE_TIMEOUT_MINUTES):
                        os.remove(filepath)
                        logger.debug(f"Cache expirado removido: {filename}")
        except Exception as e:
            logger.error(f"Erro ao limpar cache expirado: {str(e)}")
    
    def get(self, key: str) -> Optional[Any]:
        """Recupera um valor do cache."""
        try:
            cache_path = self._get_cache_path(key)
            if not os.path.exists(cache_path):
                return None
            
            # Verificar se o cache expirou
            mtime = datetime.fromtimestamp(os.path.getmtime(cache_path))
            if datetime.now() - mtime > timedelta(minutes=CACHE_TIMEOUT_MINUTES):
                os.remove(cache_path)
                return None
            
            with open(cache_path, 'rb') as f:
                return pickle.load(f)
        except Exception as e:
            logger.error(f"Erro ao recuperar do cache: {str(e)}")
            return None
    
    def set(self, key: str, value: Any) -> bool:
        """Armazena um valor no cache."""
        try:
            cache_path = self._get_cache_path(key)
            with open(cache_path, 'wb') as f:
                pickle.dump(value, f)
            return True
        except Exception as e:
            logger.error(f"Erro ao armazenar no cache: {str(e)}")
            return False
    
    def delete(self, key: str) -> bool:
        """Remove um valor do cache."""
        try:
            cache_path = self._get_cache_path(key)
            if os.path.exists(cache_path):
                os.remove(cache_path)
            return True
        except Exception as e:
            logger.error(f"Erro ao remover do cache: {str(e)}")
            return False
    
    def clear(self) -> bool:
        """Limpa todo o cache."""
        try:
            for filename in os.listdir(self.cache_dir):
                filepath = os.path.join(self.cache_dir, filename)
                if os.path.isfile(filepath):
                    os.remove(filepath)
            return True
        except Exception as e:
            logger.error(f"Erro ao limpar cache: {str(e)}")
            return False

# Instância global do cache
cache = Cache() 