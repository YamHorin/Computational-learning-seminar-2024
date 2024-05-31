# before you start coding you need to install autoGen 
# run this command in the terminal:
#   pip install pyautogen
#   ollama pull llama3
import gui
import autogen as ag

# gui.start_gui()
# questions  = gui.get_input()
# print(questions)
questions = '''
    1. Supply and Demand Analysis: How do shifts in supply and demand affect the equilibrium price and quantity in a competitive market? Provide examples to illustrate your answer.

    2. Monetary Policy: Explain the role of central banks in managing economic stability. How do interest rates and open market operations influence inflation and unemployment?

    3. International Trade: Discuss the advantages and disadvantages of free trade. How do trade policies such as tariffs and quotas impact domestic industries and global economic relations?
'''

config_list = [
  {
    "model": "llama3",
    "base_url": "http://localhost:11434/v1",
    "api_key": "ollama",
  }
]
#example:
# assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})

# user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False})
# user_proxy.initiate_chat(assistant, message="tell me a joke")

cathy = ag.ConversableAgent(
    "cathy",
    system_message='''
        Your name is Cathy 
        You are a student who has to give 10-15 answers to the questions that Bob will send you
        You have to give the answers that you think is the most correct
        Answers should be accurate
        Notice that they are separated by numbers
    
    ''',
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",  # Never ask for human input.
)

bob  = ag.ConversableAgent(
    "bob",
    system_message='''
        Your name is bob 
        You are a AI assitent 
        your job is to get question from the user and pass them to cathy
        so she can answer them
    
    ''',
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",  # Never ask for human input.
)

user_proxy = ag.UserProxyAgent("user", code_execution_config=False)