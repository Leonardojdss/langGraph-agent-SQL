from langchain.chat_models import init_chat_model

def chat_llm(model_name: str):
    llm = init_chat_model(f"openai:{model_name}")
    return llm