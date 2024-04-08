#!/usr/bin/env python3
"""
"""
import os
import logging
from logging import handlers

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level)
#ch = logging.StreamHandler()
#ch.setLevel(logging.DEBUG)
fh = handlers.RotatingFileHandler(
    "meulog.log", 
    maxBytes=100,   # 10**6 (1MB)
    backupCount=10,  # bytes, qtd_files_backup 
)
fh.setFormatter(log_level) 
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s %(message)s'
)
#ch.setFormatter(fmt)
fh.setFormatter(fmt)
#log.addHandler(ch)
log.addHandler(fh)

"""
log.critical("Erro geral ex: banco de dados sumiu")
log.debug("Mensagem pro dev, qa, sysadmin")
log.warning("Aviso que não causa erro")
log.error("Erro que afeta uma unica execucao")
log.info("Mensagem geral para usuarios")
"""

try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
    # stdout
    # sterr