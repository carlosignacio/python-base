#!/usr/bin/env python3
"""
"""
import os
import logging

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

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
    logging.error("Deu erro %s", str(e))
    # stdout
    # sterr