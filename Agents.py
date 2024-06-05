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
        You are a professor who has to give 10-15 answers to the questions that Bob will send you
        You have to give the answers that you think is the most correct
        Answers should be accurate
        Notice that they are separated by numbers
        when you finish start the message with THE Answers:
    ''',
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",  # Never ask for human input.
)

bob  = ag.ConversableAgent(
    "bob",
    system_message='''
        Your name is bob 
        You are a AI assitent 
        your job is to get questions from the user and pass them to cathy and shir
        so cathy can answer them
    
    ''',
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",  # Never ask for human input.
)
shir  = ag.ConversableAgent(
    "shir",
    system_message='''
        Your name is shir 
        You are a AI assitent 
        your job is to get Answers from cathy and check The quality of the answers
        if the answers were not good enough say "this is not good enoght cathy"
        and tell cathy what to change in the answers of the qeustions
        and print the answers
    ''',
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",  # Never ask for human input.
)

tony = ag.ConversableAgent(
    "tony",
    system_message='''
        Your name is tony 
        You are a AI assitent 
        your job is to get the questions from bob
        and the answers from shir
        and print the result 
        in a table side by side 
        the question vs the answers to that question 
        notice the numbers 
    ''',
    llm_config={"config_list": config_list},
    human_input_mode="NEVER",  # Never ask for human input.
)

initializer = ag.UserProxyAgent(
    name="Init",
)

def state_transition(last_speaker, groupchat):
    messages = groupchat.messages

    if last_speaker is initializer:
        # init -> retrieve
        return bob
    elif last_speaker is bob:
        # retrieve: action 1 -> action 2
        return cathy
    elif last_speaker is cathy:
    # retrieve: action 2 -> action 3
        return shir
    elif last_speaker is shir:
        if messages[-1]["content"] == "this is not good enoght cathy":
            # retrieve --(execution failed)--> retrieve
            return cathy
        else:
            # retrieve --(execution success)--> research
            return tony
    elif last_speaker == "tony":
        # research -> end
        return None
    
##making the group chat:
groupchat = ag.GroupChat(
agents=[initializer, bob, shir, tony , cathy],
messages=[],
max_round=20,
speaker_selection_method=state_transition,
)

##manager
manager = ag.GroupChatManager(groupchat=groupchat, llm_config=config_list)

initializer.initiate_chat(
    manager, message=questions
)