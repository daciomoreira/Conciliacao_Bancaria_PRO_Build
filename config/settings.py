"""
Arquivo de configurações do sistema de Conciliação Bancária.
"""

# Configurações de Upload
MAX_FILE_SIZE_MB = 10
ALLOWED_EXTENSIONS = {
    'ofx': ['.ofx'],
    'report': ['.csv', '.xlsx', '.xls']
}

# Configurações de Interface
PAGE_TITLE = "IA Conciliação"
PAGE_ICON = "💲"
COMPANY_NAME = "KAPEX Assessoria Empresarial"
SUPPORT_EMAIL = "controladoria@kapex.com.br"
VERSION = "3.1.2"

# Configurações de Processamento
MAX_ROWS_DISPLAY = 1000
CACHE_TIMEOUT_MINUTES = 30
DEFAULT_ENCODINGS = ['cp1252', 'utf-8', 'latin1', 'iso-8859-1']
DEFAULT_DELIMITERS = [',', ';', '\t', '|']

# Configurações de Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "logs/app.log"

# Configurações de Exportação
PDF_PAGE_SIZE = "A4"
PDF_ORIENTATION = "landscape"
EXCEL_ENGINE = "openpyxl"

# Diretórios
UPLOAD_DIR = "data/uploads"
PROFILE_DIR = "profiles"
ASSETS_DIR = "assets"
TEMP_DIR = "data/temp" 