from __future__ import annotations

from .....configs.config import Config

import ollama


def init_ollama():
    pass


def get_list_of_models_from_ollama() -> list:
    
    list_of_models: list = ollama.list()
    
    return list_of_models
    