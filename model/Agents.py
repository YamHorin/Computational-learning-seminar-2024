# before you start coding you need to install autoGen 
# run this command in the terminal:
#   pip install pyautogen
#   ollama pull llama3
#   install docker 
#   docker build -f .devcontainer/Dockerfile -t autogen_base_img https://github.com/microsoft/autogen.git#main
#   docker build -f .devcontainer/full/Dockerfile -t autogen_full_img https://github.com/microsoft/autogen.git#main
#   docker run -d --name exciting_chatterjee alpine watch "date >> /var/log/date.log"

# import gui
# import autogen as ag

# # gui.start_gui()
# # questions  = gui.get_input()
# # print(questions)
# questions = '''
#     1. Supply and Demand Analysis: How do shifts in supply and demand affect the equilibrium price and quantity in a competitive market? Provide examples to illustrate your answer.

#     2. Monetary Policy: Explain the role of central banks in managing economic stability. How do interest rates and open market operations influence inflation and unemployment?

#     3. International Trade: Discuss the advantages and disadvantages of free trade. How do trade policies such as tariffs and quotas impact domestic industries and global economic relations?
# '''

# config_list = [
#   {
#     "model": "llama3",
#     "base_url": "http://localhost:11434/v1",
#     "api_key": "ollama",
#   }
# ]
# config_list2 ={
#     "model": "llama3",
#     "base_url": "http://localhost:11434/v1",
#     "api_key": "ollama",
#   }


# bob  = ag.ConversableAgent(
#     "bob",
#     system_message='''
#         Your name is Bob.

#         You are a professor who must provide 10 different answers to the questions the user will send you.

#         You need to give the answers that you think are the most correct. Ensure the answers are accurate.

#         Each answer should be numbered separately.

#         When you finish, wait for a feedback from shir 
#         if shir tells you this is not good "This is not good enough, Bob,"
#         see what it is to be fixed
#         if not 
#         show the result in the form: 

#         question 1:
#         [put the question here]
#         the answers:
#         [answer 1]
#         [answer 2]
#         [answer 3]

#         question 2:
#         [put the question here]
#         the answers:
#         [answer 1]
#         [answer 2]
#         [answer 3]

        
#         ".
    
#     ''',
#     llm_config={"config_list": config_list},
#     human_input_mode="NEVER",  # Never ask for human input.
# )
# shir  = ag.ConversableAgent(
#     "shir",
#     system_message='''
#         Your name is Shir.

#         You are an Professor.

#         Your job is to get answers from Bob and check the quality of the answers.

#         If the answers are not good enough, say "This is not good enough, Bob!" and tell Bob what to change in the answers.

#         If the answers are good, pass them to Tony without printing a summar
#     ''',
#     llm_config={"config_list": config_list},
#     human_input_mode="NEVER",  # Never ask for human input.
# )

# initializer = ag.UserProxyAgent(
#     name="Init",
# )

# def state_transition(last_speaker, groupchat):
#     messages = groupchat.messages

#     if last_speaker is initializer:
#         # init -> retrieve
#         return bob
#     elif last_speaker is bob:
#         if "This is not good enough, Bob!" in str(messages[-2]["content"]):
#         # retrieve: action 1 -> action 2
#             return shir
#         else:
#             return None
#     elif last_speaker is shir:
#             return bob
    
# ##making the group chat:
# groupchat = ag.GroupChat(
# agents=[initializer, bob, shir],
# messages=[],
# max_round=20,
# speaker_selection_method=state_transition,
# )

# ##manager
# manager = ag.GroupChatManager(groupchat=groupchat, llm_config=config_list2)

# initializer.initiate_chat(
#     manager, message=questions
# )
