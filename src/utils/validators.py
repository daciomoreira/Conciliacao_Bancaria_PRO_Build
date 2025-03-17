"""
Módulo de validação para o sistema de Conciliação Bancária.
"""

import os
from typing import Union, List, Dict
import pandas as pd
from datetime import datetime

# Importar configurações
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config.settings import MAX_FILE_SIZE_MB, ALLOWED_EXTENSIONS
from src.utils.logger import logger

class FileValidator:
    @staticmethod
    def validate_file_size(file) -> bool:
        """Valida o tamanho do arquivo."""
        try:
            file.seek(0, os.SEEK_END)
            size_bytes = file.tell()
            file.seek(0)
            size_mb = size_bytes / (1024 * 1024)
            
            if size_mb > MAX_FILE_SIZE_MB:
                logger.warning(f"Arquivo muito grande: {size_mb:.2f}MB (máximo: {MAX_FILE_SIZE_MB}MB)")
                return False
            return True
        except Exception as e:
            logger.error(f"Erro ao validar tamanho do arquivo: {str(e)}")
            return False

    @staticmethod
    def validate_file_extension(filename: str, file_type: str) -> bool:
        """Valida a extensão do arquivo."""
        try:
            ext = os.path.splitext(filename)[1].lower()
            if file_type not in ALLOWED_EXTENSIONS or ext not in ALLOWED_EXTENSIONS[file_type]:
                logger.warning(f"Extensão inválida: {ext} para tipo {file_type}")
                return False
            return True
        except Exception as e:
            logger.error(f"Erro ao validar extensão do arquivo: {str(e)}")
            return False

class DataValidator:
    @staticmethod
    def validate_date_format(date_str: str) -> bool:
        """Valida o formato da data."""
        try:
            if pd.isna(date_str) or date_str == "":
                return False
            
            # Tentar diferentes formatos de data comuns
            formats = [
                "%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y",
                "%d/%m/%y", "%Y/%m/%d", "%d.%m.%Y"
            ]
            
            for fmt in formats:
                try:
                    datetime.strptime(str(date_str), fmt)
                    return True
                except ValueError:
                    continue
            
            return False
        except Exception as e:
            logger.error(f"Erro ao validar formato de data: {str(e)}")
            return False

    @staticmethod
    def validate_monetary_value(value: Union[str, float, int]) -> bool:
        """Valida valor monetário."""
        try:
            if pd.isna(value):
                return False
            
            # Se for string, tentar converter para float
            if isinstance(value, str):
                # Remover R$, espaços e trocar , por .
                value = value.replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')
            
            # Converter para float
            float_value = float(value)
            return True
        except Exception as e:
            logger.error(f"Erro ao validar valor monetário: {str(e)}")
            return False

    @staticmethod
    def validate_required_columns(df: pd.DataFrame, required_columns: List[str]) -> bool:
        """Valida se todas as colunas necessárias estão presentes."""
        try:
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                logger.warning(f"Colunas ausentes: {missing_columns}")
                return False
            return True
        except Exception as e:
            logger.error(f"Erro ao validar colunas obrigatórias: {str(e)}")
            return False

class ProfileValidator:
    @staticmethod
    def validate_profile_data(profile_data: Dict) -> bool:
        """Valida os dados do perfil de mapeamento."""
        try:
            required_keys = ['mapeamento', 'tipo_relatorio']
            if not all(key in profile_data for key in required_keys):
                logger.warning("Dados do perfil incompletos")
                return False
            
            required_mappings = ['data', 'valor', 'descricao']
            if not all(key in profile_data['mapeamento'] for key in required_mappings):
                logger.warning("Mapeamento incompleto no perfil")
                return False
            
            return True
        except Exception as e:
            logger.error(f"Erro ao validar dados do perfil: {str(e)}")
            return False 