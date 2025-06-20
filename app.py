from agents.agent_sql import sql_agent

def chat_sql():
    """
    Chat with your database using agent SQL
    """

    agent_sql = sql_agent()

    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat.")
                break

            for step in agent_sql.stream(
                {"messages": [{"role": "user", "content": user_input}]},
                stream_mode="values",
            ):
                step["messages"][-1].pretty_print()

        except Exception as e:
            print(f"An error occurred: {e}")
            break


if __name__ == "__main__":
    chat_sql()