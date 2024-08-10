from flask_caching import Cache

# Configuração do cache
config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
}

cache = Cache()  # Inicializa o objeto Cache sem configuração
