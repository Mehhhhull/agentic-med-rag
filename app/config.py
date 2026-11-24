import os
import certifi
from dotenv import load_dotenv

load_dotenv()
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    gemini_api_key: str = ''
    pinecone_api_key: str = ''
    tavily_api_key: str = ''
    pinecone_index: str = 'agentic-med-rag'
    gemini_chat_model: str = ''
    gemini_embed_model: str = ''
    gemini_vision_model: str = ''
    api_token: str = ''
    allowed_origins: str = 'http://localhost:8000,http://127.0.0.1:8000'
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

settings=Settings()