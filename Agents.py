
# before you start coding you need to install autoGen 
# run this command in the terminal:
# pip install pyautogen

import os
from autogen import AssistantAgent, UserProxyAgent , ConversableAgent

agent = ConversableAgent(
    "chatbot",
    llm_config={"config_list": [{"model": "Ollama", "api_key": 'ollama'}]},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)
reply = agent.generate_reply(messages=[{"content": "Tell me a joke.", "role": "user"}])
print(reply)
