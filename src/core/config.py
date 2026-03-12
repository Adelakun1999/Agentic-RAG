from dotenv import load_dotenv
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    DOCUMENTS_DIR: str
    VECTOR_STORE_DIR: str
    COLLECTION_NAME: str
    GROQ_API_KEY : str 
    MODEL_NAME: str
    MODEL_TEMPERATURE: float
    API_HOST: str = "localhost"
    API_PORT: int = 8000
    CHAT_ENDPOINT_URL: str = "http://localhost:8000/chat/answer"







    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"