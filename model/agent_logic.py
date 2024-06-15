import autogen as ag

def initialize_agents():
    config_list = [
        {
            "model": "llama3",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",
        }
    ]

    bob = ag.ConversableAgent(
        "bob",
        system_message='''
            Your name is Bob.

            You are a professor who must provide 10 different answers to the questions the user will send you.

            You need to give the answers that you think are the most correct. Ensure the answers are accurate.

            Each answer should be numbered separately.

            When you finish, wait for a feedback from shir 
            if shir tells you this is not good "This is not good enough, Bob,"
            see what it is to be fixed
            if not 
            show the result in the form: 

            question 1:
            [put the question here]
            the answers:
            [answer 1]
            [answer 2]
            [answer 3]

            question 2:
            [put the question here]
            the answers:
            [answer 1]
            [answer 2]
            [answer 3]
        ''',
        llm_config={"config_list": config_list},
        human_input_mode="NEVER",  # Never ask for human input.
    )

    shir = ag.ConversableAgent(
        "shir",
        system_message='''
            Your name is Shir.

            You are a Professor.

            Your job is to get answers from Bob and check the quality of the answers.

            If the answers are not good enough, say "This is not good enough, Bob!" and tell Bob what to change in the answers.

            If the answers are good, pass them to Tony without printing a summary
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
            if "This is not good enough, Bob!" in str(messages[-2]["content"]):
                # retrieve: action 1 -> action 2
                return shir
            else:
                return None
        elif last_speaker is shir:
            return bob

    # Making the group chat
    groupchat = ag.GroupChat(
        agents=[initializer, bob, shir],
        messages=[],
        max_round=20,
        speaker_selection_method=state_transition,
    )

    # Manager
    manager = ag.GroupChatManager(groupchat=groupchat, llm_config={"model": "llama3", "base_url": "http://localhost:11434/v1", "api_key": "ollama"})

    return initializer, manager, groupchat
