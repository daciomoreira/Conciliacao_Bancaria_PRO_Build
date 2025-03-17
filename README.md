# Conciliação Bancária PRO v3.1.2

Sistema de conciliação bancária automática com inteligência artificial desenvolvido pelo Dácio Moreira na KAPEX Assessoria Empresarial.

1. 🚀 Funcionalidades

- Conciliação automática de extratos bancários (OFX) com relatórios financeiros
- Suporte para múltiplos formatos de relatório (CSV, Excel)
- Interface gráfica intuitiva com Streamlit
- Perfis de mapeamento personalizáveis
- Exportação de resultados em múltiplos formatos
- Gráficos e análises visuais
- Sistema de cache para melhor performance
- Logging completo para rastreamento de erros

2. 📋 Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)
- Acesso a arquivos OFX do banco
- Relatórios financeiros em formato CSV ou Excel

3. Siga os passos na interface:
   - Carregue o arquivo OFX do banco
   - Carregue o relatório financeiro
   - Configure o mapeamento das colunas
   - Execute a conciliação
   - Analise os resultados
   - Exporte conforme necessário

## 📁 Estrutura do Projeto

```
conciliacao-bancaria-pro/
├── src/
│   ├── utils/
│   │   ├── logger.py
│   │   ├── cache.py
│   │   └── validators.py
│   ├── data_loader.py
│   └── reconciliation.py
├── tests/
├── docs/
├── config/
│   └── settings.py
├── assets/
├── profiles/
├── data/
│   ├── uploads/
│   └── temp/
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ Configuração

As principais configurações podem ser ajustadas no arquivo `config/settings.py`:

- Limites de upload
- Timeouts de cache
- Formatos de arquivo permitidos
- Configurações de logging
- Diretórios de trabalho

## 🔍 Logging

O sistema mantém logs detalhados em `logs/app.log` com:

- Erros e exceções
- Operações de arquivo
- Eventos de cache
- Métricas de performance

## 🔒 Segurança

- Validação de tipos de arquivo
- Limite de tamanho de upload
- Sanitização de dados
- Cache com timeout
- Sem armazenamento permanente de dados sensíveis

## 🤝 Suporte

Para suporte técnico ou dúvidas:
- Email: controladoria@kapex.com.br
- Site: www.kapex.com.br

## 📄 Licença

Copyright © 2025 KAPEX Assessoria Empresarial.
Todos os direitos reservados.
