from typing import Literal
from langchain_core.messages import AIMessage
from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START, MessagesState, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from tool.sql_tool import sql_tool_node

db, llm, get_schema_node, run_query_node, run_query_tool, list_tables_tool, llm_with_tools_get_schema, llm_with_tools_generate_query = sql_tool_node()
    
def list_tables(state: MessagesState):
    tool_call = {
        "name": "sql_db_list_tables",
        "args": {},
        "id": "abc123",
        "type": "tool_call",
    }
    tool_call_message = AIMessage(content="", tool_calls=[tool_call])

    tool_message = list_tables_tool.invoke(tool_call)
    response = AIMessage(f"Available tables: {tool_message.content}")

    return {"messages": [tool_call_message, tool_message, response]}

def call_get_schema(state: MessagesState):
    # Note that LangChain enforces that all models accept `tool_choice="any"`
    # as well as `tool_choice=<string name of tool>`.
    response = llm_with_tools_get_schema.invoke(state["messages"])

    return {"messages": [response]}

def generate_query(state: MessagesState, prompt_query):
    system_message = {
        "role": "system",
        "content": prompt_query,
    }
    # We do not force a tool call here, to allow the model to
    # respond naturally when it obtains the solution.
    response = llm_with_tools_generate_query.invoke([system_message] + state["messages"])

    return {"messages": [response]}

def check_query(state: MessagesState, prompt_check_query):
    system_message = {
        "role": "system",
        "content": prompt_check_query,
    }

    # Generate an artificial user message to check
    tool_call = state["messages"][-1].tool_calls[0]
    user_message = {"role": "user", "content": tool_call["args"]["query"]}
    llm_with_tools_check_query = llm.bind_tools([run_query_tool], tool_choice="any")
    response = llm_with_tools_check_query.invoke([system_message, user_message])
    response.id = state["messages"][-1].id

    return {"messages": [response]}

def should_continue(state: MessagesState) -> Literal[END, "check_query"]:
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:
        return END
    else:
        return "check_query"

def agent_graph(prompt_query, prompt_check_query):

    def generate_query_node(state: MessagesState):
        return generate_query(state, prompt_query)
    
    def check_query_node(state: MessagesState):
        return check_query(state, prompt_check_query)

    builder = StateGraph(MessagesState)
    builder.add_node("list_tables", list_tables)
    builder.add_node("call_get_schema", call_get_schema)
    builder.add_node("get_schema", get_schema_node)
    builder.add_node("generate_query", generate_query_node)
    builder.add_node("check_query", check_query_node)
    builder.add_node("run_query", run_query_node)

    builder.add_edge(START, "list_tables")
    builder.add_edge("list_tables", "call_get_schema")
    builder.add_edge("call_get_schema", "get_schema")
    builder.add_edge("get_schema", "generate_query")
    builder.add_conditional_edges(
        "generate_query",
        should_continue,
    )
    builder.add_edge("check_query", "run_query")
    builder.add_edge("run_query", "generate_query")
    memory = MemorySaver()
    agent = builder.compile(checkpointer=memory)

    config = {
        "configurable": {
            "thread_id": "1"
        }
    }

    return agent, config