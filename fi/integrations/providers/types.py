from enum import Enum


class ApiKeyName(str, Enum):
    ANYSCALE_API_KEY = "ANYSCALE_API_KEY"
    ANTHROPIC_API_KEY = "ANTHROPIC_API_KEY"
    AZURE_API_KEY = "AZURE_API_KEY"
    AZURE_AI_API_KEY = "AZURE_AI_API_KEY"
    BEDROCK_API_KEY = "BEDROCK_API_KEY"
    CLOUDFLARE_API_KEY = "CLOUDFLARE_API_KEY"
    COHERE_API_KEY = "COHERE_API_KEY"
    COHERE_CHAT_API_KEY = "COHERE_CHAT_API_KEY"
    DATABRICKS_API_KEY = "DATABRICKS_API_KEY"
    DEEPINFRA_API_KEY = "DEEPINFRA_API_KEY"
    FIREWORKS_AI_API_KEY = "FIREWORKS_AI_API_KEY"
    FIREWORKS_AI_EMBEDDING_MODELS_API_KEY = "FIREWORKS_AI-EMBEDDING-MODELS_API_KEY"
    GEMINI_API_KEY = "GEMINI_API_KEY"
    HUGGINGFACE_API_KEY = "HUGGINGFACE_API_KEY"
    OLLAMA_API_KEY = "OLLAMA_API_KEY"
    OPENAI_API_KEY = "OPENAI_API_KEY"
    PALM_API_KEY = "PALM_API_KEY"
    PERPLEXITY_API_KEY = "PERPLEXITY_API_KEY"
    TEXT_COMPLETION_OPENAI_API_KEY = "TEXT-COMPLETION-OPENAI_API_KEY"
    VERTEX_AI_CHAT_MODELS_API_KEY = "VERTEX_AI-CHAT-MODELS_API_KEY"
    VERTEX_AI_CODE_CHAT_MODELS_API_KEY = "VERTEX_AI-CODE-CHAT-MODELS_API_KEY"
    VERTEX_AI_CODE_TEXT_MODELS_API_KEY = "VERTEX_AI-CODE-TEXT-MODELS_API_KEY"
    VERTEX_AI_EMBEDDING_MODELS_API_KEY = "VERTEX_AI-EMBEDDING-MODELS_API_KEY"
    VERTEX_AI_TEXT_MODELS_API_KEY = "VERTEX_AI-TEXT-MODELS_API_KEY"
    VOYAGE_API_KEY = "VOYAGE_API_KEY"
