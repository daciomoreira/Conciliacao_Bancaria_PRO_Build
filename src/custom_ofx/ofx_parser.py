"""
Parser OFX compatível com múltiplas versões do Python
Este módulo corrige problemas com a importação de collections.Iterable
no Python 3.10+ onde Iterable foi movido para collections.abc
"""
import sys

# Fix for Python 3.10+ compatibility
if sys.version_info >= (3, 10):
    import collections.abc as collections_abc
    sys.modules['collections'].Iterable = collections_abc.Iterable
    sys.modules['collections'].Mapping = collections_abc.Mapping

try:
    # Agora podemos importar ofxparse com segurança
    import ofxparse
    from ofxparse import OfxParser
except ImportError:
    raise ImportError("Biblioteca ofxparse não encontrada. Instale usando: pip install ofxparse")

def parse_ofx(arquivo_ofx):
    """
    Parseia um arquivo OFX e retorna o objeto de resultado
    
    Args:
        arquivo_ofx: Um objeto file-like contendo os dados OFX
        
    Returns:
        O objeto OFX parseado
    """
    try:
        # Verificar se é um objeto BytesIO
        if hasattr(arquivo_ofx, 'read'):
            ofx = OfxParser.parse(arquivo_ofx)
        else:
            # Se for um nome de arquivo ou outro tipo de objeto
            raise ValueError("O arquivo OFX deve ser um objeto file-like")
        
        return ofx
    except Exception as e:
        raise Exception(f"Erro ao processar arquivo OFX: {str(e)}") 