from graph_agents.agent_sql import sql_agent
from langchain.schema import AIMessage

def chat_sql():
    """
    Chat with your database using agent SQL
    """

    agent_sql, config = sql_agent()

    while True:
   
        try:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat.")
                break
            
            last_message = None
            for step in agent_sql.stream(
                {"messages": [{"role": "user", "content": user_input}]},
                config=config,
                stream_mode="values",
            ):
                for value in step.values():
                    for msg in value:
                        if isinstance(msg, AIMessage):
                            last_message = msg
            if last_message:
                print("Agent SQL: ", last_message.content[-1] if isinstance(last_message.content, list) else last_message.content)

        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    chat_sql()