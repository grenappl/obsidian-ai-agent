from langchain.chat_models import init_chat_model
from langchain.messages import AIMessage, HumanMessage, SystemMessage

from obsidian_ai_agent.config.settings import (
    AGENT_ACTIONS,
    MODEL,
    PROVIDER,
    get_API_KEY1,
    get_API_KEY2,
)

from .prompts import CHATBOT_PROMPT, CLASSIFIER_PROMPT
from .schemas import ClassifierResult


def _get_models(temp: int = 0):
    primary_model = init_chat_model(
        model=MODEL,
        model_provider=PROVIDER,
        api_key=get_API_KEY1(),
        temperature=temp,
    )
    backup_model = init_chat_model(
        model=MODEL,
        model_provider=PROVIDER,
        api_key=get_API_KEY2(),
        temperature=temp,
    )
    return primary_model, backup_model


def run_classifier(user_prompt: str) -> ClassifierResult:
    print("Classifying prompt...")
    primary_classifier, backup_classifier = _get_models()

    primary_classifier = primary_classifier.with_structured_output(ClassifierResult)
    backup_classifier = backup_classifier.with_structured_output(ClassifierResult)

    unified_classifier = primary_classifier.with_fallbacks([backup_classifier])
    return unified_classifier.invoke(
        [SystemMessage(CLASSIFIER_PROMPT), HumanMessage(user_prompt)]
    )


def run_assistant(action: str, user_prompt: str) -> AIMessage:
    primary_assistant, backup_assistant = _get_models(temp=0.1)

    sys_prompt: str
    if action == AGENT_ACTIONS[0]:
        print("Running chatbot...")
        sys_prompt = CHATBOT_PROMPT

    unified_assistant = primary_assistant.with_fallbacks([backup_assistant])
    return unified_assistant.invoke(
        [SystemMessage(sys_prompt), HumanMessage(user_prompt)]
    )
