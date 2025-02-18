from langchain_community.chat_models import __all__

EXPECTED_ALL = [
    "ChatOpenAI",
    "BedrockChat",
    "AzureChatOpenAI",
    "FakeListChatModel",
    "PromptLayerChatOpenAI",
    "ChatEverlyAI",
    "ChatAnthropic",
    "ChatCohere",
    "ChatDatabricks",
    "ChatDeepInfra",
    "ChatGooglePalm",
    "ChatHuggingFace",
    "ChatMaritalk",
    "ChatMlflow",
    "ChatMLflowAIGateway",
    "ChatMLX",
    "ChatOllama",
    "ChatVertexAI",
    "JinaChat",
    "HumanInputChatModel",
    "MiniMaxChat",
    "ChatAnyscale",
    "ChatLiteLLM",
    "ChatLiteLLMRouter",
    "ErnieBotChat",
    "ChatJavelinAIGateway",
    "ChatKonko",
    "PaiEasChatEndpoint",
    "QianfanChatEndpoint",
    "ChatTongyi",
    "ChatFireworks",
    "ChatYandexGPT",
    "ChatBaichuan",
    "ChatHunyuan",
    "GigaChat",
    "ChatSparkLLM",
    "VolcEngineMaasChat",
    "LlamaEdgeChatService",
    "GPTRouter",
    "ChatYuan2",
    "ChatZhipuAI",
    "ChatPerplexity",
    "ChatKinetica",
    "ChatFriendli",
    "ChatPremAI",
]


def test_all_imports() -> None:
    assert set(__all__) == set(EXPECTED_ALL)
