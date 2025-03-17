"""
Módulo de logging para o sistema de Conciliação Bancária.
"""

import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler
import sys

# Importar configurações
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config.settings import LOG_LEVEL, LOG_FORMAT, LOG_FILE

class Logger:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance
    
    def _initialize_logger(self):
        """Inicializa o logger com as configurações definidas."""
        # Criar diretório de logs se não existir
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        
        # Configurar logger
        self.logger = logging.getLogger('ConciliacaoBancaria')
        self.logger.setLevel(getattr(logging, LOG_LEVEL))
        
        # Configurar formato
        formatter = logging.Formatter(LOG_FORMAT)
        
        # Handler para arquivo com rotação
        file_handler = RotatingFileHandler(
            LOG_FILE,
            maxBytes=5*1024*1024,  # 5MB
            backupCount=5
        )
        file_handler.setFormatter(formatter)
        
        # Handler para console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        
        # Adicionar handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def info(self, message):
        """Registra mensagem de informação."""
        self.logger.info(message)
    
    def error(self, message, exc_info=True):
        """Registra mensagem de erro."""
        self.logger.error(message, exc_info=exc_info)
    
    def warning(self, message):
        """Registra mensagem de aviso."""
        self.logger.warning(message)
    
    def debug(self, message):
        """Registra mensagem de debug."""
        self.logger.debug(message)
    
    def critical(self, message):
        """Registra mensagem crítica."""
        self.logger.critical(message)

# Instância global do logger
logger = Logger() 