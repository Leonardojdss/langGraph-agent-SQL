from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.prebuilt import ToolNode
from infra.llm import chat_llm
from dotenv import load_dotenv
import os

load_dotenv()
llm = chat_llm("gpt-4o-mini")

def sql_tool_node():

    database = os.getenv("DATABASE_SQLITE_PATH")
    db = SQLDatabase.from_uri(
        f"sqlite:///{database}"
    )

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    tools = toolkit.get_tools()

    get_schema_tool = next(tool for tool in tools if tool.name == "sql_db_schema")
    get_schema_node = ToolNode([get_schema_tool])

    run_query_tool = next(tool for tool in tools if tool.name == "sql_db_query")
    run_query_node = ToolNode([run_query_tool])

    list_tables_tool = next(tool for tool in tools if tool.name == "sql_db_list_tables")

    llm_with_tools_get_schema = llm.bind_tools([get_schema_tool], tool_choice="any")

    llm_with_tools_generate_query = llm.bind_tools([run_query_tool])

    return db, llm, get_schema_node, run_query_node, run_query_tool, list_tables_tool, llm_with_tools_get_schema, llm_with_tools_generate_query