from langchain_community.utilities import SQLDatabase
from graph_agents.graph_sql import agent_graph
from dotenv import load_dotenv
import os

load_dotenv()

database = os.getenv("DATABASE_SQLITE_PATH")
db = SQLDatabase.from_uri(
    f"sqlite:///{database}"
)

def sql_agent():

    with open("prompt/generate_query_system_prompt.txt", "r") as f:
        system_prompt_generate_query = f.read()

    generate_query_system_prompt = f"""{system_prompt_generate_query}
    """.format(
        dialect=db.dialect,
        top_k=5,
    )

    with open("prompt/check_query_system_prompt.txt", "r") as f:
        system_prompt_check_query = f.read()

    check_query_system_prompt = f"""{system_prompt_check_query}
    """.format(dialect=db.dialect)

    agent, config = agent_graph(generate_query_system_prompt, check_query_system_prompt)

    return agent, config