from client.mcp_client import create_mcp_client
from agent.options_agent import create_options_agent

def main():
    mcp_client = create_mcp_client()

    with mcp_client:
        tools = mcp_client.list_tools_sync()

        agent = create_options_agent(tools)

        print("Options Analysis Agent Ready. Type 'exit' to quit.\n")

        while True:
            user_input = input("Question: ")

            if user_input.lower() in ["exit", "quit"]:
                break

            print("\nThinking...\n")
            response = agent(user_input)
            print(f"{response}\n")

if __name__ == "__main__":
    main()
