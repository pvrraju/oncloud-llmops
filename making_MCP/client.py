from langchain_mcp_adapters.client import MultiServerMCPClient

from langgraph.prebuilt import create_react_agent

from langchain_openai import ChatOpenAI 

from dotenv import load_dotenv


load_dotenv()


import asyncio


async def main():
    client = MultiServerMCPClient(
        {
            "maths":{
                "command" : "python",
                "args" : ["making_MCP/mathserver.py"],          
                "transport":"stdio",
            },
            "weather":{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":"streamable-http",
            }
        }
    )

    import os 
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

    tools = await client.get_tools()

    model = ChatOpenAI(model='gpt-4o-mini')

    agent = create_react_agent(
        model, tools
    )

    math_response = await agent.ainvoke(
        {'messages': [{"role":"user","content":"what is (45 + 91) * 21"}]}

    )

    print("Math response: " , math_response['messages'][-1].content) 


asyncio.run(main())