from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from GetChatModel import GetChatModel


class EnglishTransfer(BaseModel):
    result: str = Field(description="transfer result")


class Robot:

    @staticmethod
    def transfer_book(string: str, level: str):
        chat_model = GetChatModel.get_google_model()
        parser = PydanticOutputParser(pydantic_object=EnglishTransfer)
        format_instructions = parser.get_format_instructions()

        prompt = ChatPromptTemplate.from_messages(
            [("system", "please transfer the below novel content to english, english level:" + level + " keep all the detail"
                                                                                     " and response have to follow format:{format_instructions}"),
             ("human", "{query}")
             ]
        )

        chain = prompt | chat_model | parser
        response: EnglishTransfer = chain.invoke({"query": string, "format_instructions": format_instructions})
        return response.result
