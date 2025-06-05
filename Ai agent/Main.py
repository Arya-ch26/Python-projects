from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool,wiki_tool,save_tool
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# Schema
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# LLM and Parser
llm = ChatOpenAI(model="gpt-4o-mini")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Prompt with format_instructions
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a research assistant.
Wrap the output in this format and provide no other text:
{format_instructions}"""
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

# Agent setup
tools = [search_tool,wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools,
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run
query = input("What can I help you with? \n")
raw_response = agent_executor.invoke({
    "query": query,
    "chat_history": []  # pass an empty list if no history yet
})

# Parse
try:
    structured_response = parser.parse(raw_response["output"])
    print(structured_response)
except Exception as e:
    print(f"Error parsing response: {e}", raw_response)
