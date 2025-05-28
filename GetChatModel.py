import os

from langchain_aws import ChatBedrock
# from langchain_aws import Bedrock, BedrockChat
from langchain_community.chat_models import ChatOllama
from langchain_community.utilities.dalle_image_generator import (
    DallEAPIWrapper)
from langchain_core.callbacks import BaseCallbackHandler
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from env_value import EnvValue


# from token_call_back import TokenCounterCallback


class GetChatModel(object):
    @staticmethod
    def get_ollama_cht_model(model_name: str = "phi3:mini", cache: bool = False) -> ChatOllama:
        chat_model = ChatOllama(model=model_name, cache=cache)
        return chat_model

    @staticmethod
    def get_ollama_cht_model_c(model_name: str = "phi3:mini", cache: bool = False) -> ChatOpenAI:
        llm = ChatOpenAI(
            api_key="ollama",  # pyright: ignore [reportArgumentType]
            model="mistral",
            base_url="http://localhost:11434/v1",
        )
        return llm

    @staticmethod
    def get_google_model() -> ChatGoogleGenerativeAI:
        key = EnvValue.get_google_ai_key()
        # key = getpass.getpass(key)
        os.environ["GOOGLE_API_KEY"] = key  # pyright: ignore [reportArgumentType]
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-preview-05-20",
        )

        return llm

    @staticmethod
    def get_chat_gpt_35_model() -> ChatOpenAI:
        key = EnvValue.get_open_ai_key()
        # key = getpass.getpass(key)

        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            api_key=key,  # pyright: ignore [reportArgumentType]
        )

        return llm

    @staticmethod
    def get_chat_gpt_40Mini_model() -> ChatOpenAI:
        key = EnvValue.get_open_ai_key()
        # key = getpass.getpass(key)

        llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=key,  # pyright: ignore [reportArgumentType]
        )

        return llm

    @staticmethod
    def get_chat_gpt_40_model() -> ChatOpenAI:
        key = EnvValue.get_open_ai_key()
        # key = getpass.getpass(key)

        llm = ChatOpenAI(
            model="gpt-4o",
            api_key=key,  # pyright: ignore [reportArgumentType]
        )

        return llm

    @staticmethod
    def get_chat_gpt_default_model() -> ChatOpenAI:
        key = EnvValue.get_open_ai_key()
        # key = getpass.getpass(key)

        llm = ChatOpenAI(
            # model="gpt-3.5-turbo",
            api_key=key
        )

        return llm

    # @staticmethod
    # def get_dall_image_model() -> DallEAPIWrapper:
    #     key = EnvValue.get_open_ai_key()
    #     # key = getpass.getpass(key)
    #
    #     image_generator = DallEAPIWrapper(
    #         model='dall-e-3',
    #         api_key=key,
    #         size='1024x1024',
    #         quality='hd'
    #     )
    #     return image_generator

    @staticmethod
    def get_open_embedding_model() -> OpenAIEmbeddings:
        key = EnvValue.get_open_ai_key()
        embeddings_model = OpenAIEmbeddings(
            model='text-embedding-3-large',
            openai_api_key=key  # pyright: ignore [reportCallIssue]
        )

        return embeddings_model

    # token_counter_use = TokenCounterCallback()
    # @staticmethod
    # def get_aws_model_nova_lite(tokenCallBack: TokenCounterCallback):
    #     # lite
    #     access_key = EnvValue.get_aws_access_key()
    #     secret_key = EnvValue.get_aws_secret_key()
    # 
    #     os.environ["AWS_ACCESS_KEY_ID"] = access_key  # pyright: ignore [reportArgumentType]
    #     os.environ["AWS_SECRET_ACCESS_KEY"] = secret_key  # pyright: ignore [reportArgumentType]
    #     llm = ChatBedrock(  # pyright: ignore [reportCallIssue]
    #         # client=bedrock_client,
    #         model_id="us.amazon.nova-lite-v1:0",  # pyright: ignore [reportCallIssue]
    #         # You can also use other models like "ai21.j2-ultra"
    #         # model_kwargs={
    #         #     "max_tokens_to_sample": 500,
    #         #     "temperature": 0.7,
    #         # }
    # 
    #         region_name='us-east-1',  # pyright: ignore [reportArgumentType]
    #         callbacks=[tokenCallBack]
    # 
    #     )
    # 
    #     return llm

    # @staticmethod
    # def get_aws_model_nova_micro(tokenCallBack: TokenCounterCallback):
    #     # lite
    #     access_key = EnvValue.get_aws_access_key()
    #     secret_key = EnvValue.get_aws_secret_key()
    # 
    #     os.environ["AWS_ACCESS_KEY_ID"] = access_key  # pyright: ignore [reportArgumentType]
    #     os.environ["AWS_SECRET_ACCESS_KEY"] = secret_key  # pyright: ignore [reportArgumentType]
    #     llm = ChatBedrock(  # pyright: ignore [reportCallIssue]
    #         # client=bedrock_client,
    #         model_id="us.amazon.nova-micro-v1:0",  # You can also use other models like "ai21.j2-ultra"
    #         # model_kwargs={
    #         #     "max_tokens_to_sample": 500,
    #         #     "temperature": 0.7,
    #         # }
    # 
    #         region_name='us-east-1',
    #         callbacks=[tokenCallBack]
    # 
    #     )
    # 
    #     return llm

    # @staticmethod
    # def get_aws_model_nova_pro(tokenCallBack: TokenCounterCallback):
    #     # lite
    #     access_key = EnvValue.get_aws_access_key()
    #     secret_key = EnvValue.get_aws_secret_key()
    # 
    #     os.environ["AWS_ACCESS_KEY_ID"] = access_key  # pyright: ignore [reportArgumentType]
    #     os.environ["AWS_SECRET_ACCESS_KEY"] = secret_key  # pyright: ignore [reportArgumentType]
    #     llm = ChatBedrock(  # pyright: ignore [reportCallIssue]
    #         # client=bedrock_client,
    #         model_id="us.amazon.nova-pro-v1:0",  # You can also use other models like "ai21.j2-ultra"
    #         # model_kwargs={
    #         #     "max_tokens_to_sample": 500,
    #         #     "temperature": 0.7,
    #         # }
    # 
    #         region_name='us-east-1',
    #         callbacks=[tokenCallBack]
    # 
    #     )
    # 
    #     return llm
