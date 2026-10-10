import os

from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from . import prompts
from .state import ClassifierResult


def run_classifier(user_prompt: str) -> ClassifierResult:
    MODEL = "openrouter/free"
    PROVIDER = "openrouter"
    API_KEY = os.getenv("OPENROUTER_API_KEY")

    classifier = init_chat_model(
        model=MODEL,
        model_provider=PROVIDER,
        api_key=API_KEY,
    )
    classifier = classifier.with_structured_output(ClassifierResult)
    return classifier.invoke(
        [SystemMessage(prompts.CLASSIFIER_PROMPT), HumanMessage(user_prompt)]
    )


def run_agent(user_prompt: str, action: str) -> ChatGoogleGenerativeAI:
    MODEL = "gemini-2.5-flash"
    PROVIDER = "google-genai"
    API_KEY_1 = os.getenv("GEMINI_API_KEY_1")
    # API_KEY_2 = os.getenv("GEMINI_API_KEY_2")

    primary_model = init_chat_model(
        model=MODEL, model_provider=PROVIDER, api_key=API_KEY_1
    )
    backup_model = init_chat_model(
        model=MODEL, model_provider=PROVIDER, api_key=API_KEY_1
    )

    def get_prompt(action):
        match action:
            case "chat":
                return prompts.CHATBOT_PROMPT
            case "make":
                return prompts.GENERATOR_PROMPT
            # rest of prompts...

    main_model = primary_model.with_fallbacks([backup_model])
    return main_model.invoke([SystemMessage(get_prompt()), HumanMessage(user_prompt)])
