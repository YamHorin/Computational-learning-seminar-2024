import autogen as ag
import re
import model.cosineSimilarityMatrix as cosin
def initialize_agents(answers):
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

            You are a professor who must provide 5 different answers to the each question the user will send you.
            
            You need to answer with the key words we will provide you 

            You need to answer as close as possible to the answers we will provide you 
            
            You need to give the answers that you think are the most correct. Ensure the answers are accurate.

            Each answer should be numbered separately.

            put the return message like that: 

            question 1:
            [put the question here]

            the answers for question 1 :
            [answer 1]
            [answer 2]
            [answer 3]
             
            end 
            
            question 2:
            [put the question here]
            the answers question 2:
            [answer 1]
            [answer 2]
            [answer 3]
            
            end
            and so on 
        ''',
        llm_config={"config_list": config_list},
        human_input_mode="NEVER",  # Never ask for human input.
    )

    initializer = ag.UserProxyAgent(
        name="Init",
    )

    def state_transition(last_speaker, groupchat):
        messages = groupchat.messages
        text = str(messages[-2]["content"])
        if last_speaker is initializer:
            # init -> retrieve
            return bob
        elif last_speaker is bob:
            #caculate similarity to each answer
            # Regular expression to match answers for each question
            answers_pattern = re.compile(r'the answers (?:for )?question \d+:\n((?:\[\w+ .+\]\n?)+)')
            all_answers = []
            matches = answers_pattern.findall(text)
            for match in matches:
                # Extract individual answers
                answers = re.findall(r'\[(.+?)\]', match)
                all_answers.append(answers)
            for answerAI in all_answers:
                score  = cosin.caculateSimilarityAnswersWithKeyWordAgentToTeacher(answerAI, ans)
            # Output the list of answers
            print(all_answers)



    # Making the group chat
    groupchat = ag.GroupChat(
        agents=[initializer, bob],
        messages=[],
        max_round=20,
        speaker_selection_method=state_transition,
    )

    # Manager
    manager = ag.GroupChatManager(groupchat=groupchat, llm_config={"model": "llama3", "base_url": "http://localhost:11434/v1", "api_key": "ollama"})

    return initializer, manager, groupchat
