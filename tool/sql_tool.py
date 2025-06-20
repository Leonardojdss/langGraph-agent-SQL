from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from infra.llm import chat_llm
from dotenv import load_dotenv
import os

load_dotenv()
llm = chat_llm("gpt-4.1")

def sql_tool():
    database = os.getenv("DATABASE_SQLITE_PATH")

    db = SQLDatabase.from_uri(
        f"sqlite:///{database}"
    )

    # print(f"Dialect: {db.dialect}")
    # print(f"Available tables: {db.get_usable_table_names()}")

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    tools = toolkit.get_tools()

    # for tool in tools:
    #     print(f"{tool.name}: {tool.description}\n")

    return db, llm, tools