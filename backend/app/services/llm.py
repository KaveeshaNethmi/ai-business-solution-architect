from langchain_openai import ChatOpenAI

from app.core.config import settings


def get_llm() -> ChatOpenAI:
    return ChatOpenAI(
        model="gpt-5-mini",
        api_key=settings.openai_api_key
    )