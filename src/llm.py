import os
from aisuite import Client
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

# Model slugs use OpenRouter naming (see https://openrouter.ai/models)
DEFAULT_MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4.1-mini")
PLANNER_MODEL = os.getenv("OPENROUTER_PLANNER_MODEL", "openai/o4-mini")

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY not set")

# OpenRouter exposes an OpenAI-compatible API, so we reuse aisuite's OpenAI
# provider and point it at OpenRouter's base URL.
client = Client(
    provider_configs={
        "openai": {
            "api_key": api_key,
            "base_url": OPENROUTER_BASE_URL,
            "default_headers": {"X-Title": "Agentic AI Research"},
        }
    }
)


def model_id(slug: str) -> str:
    """Map an OpenRouter slug (e.g. 'anthropic/claude-sonnet-4') to an aisuite model id."""
    return slug if slug.startswith("openai:") else f"openai:{slug}"
