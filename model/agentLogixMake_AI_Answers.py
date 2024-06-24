import autogen as ag
import re
import model.cosineSimilarityMatrix as cosin
import View.objectsPrograms
#answers_teacher - list of View.objectsPrograms Answers
def initialize_agents(answers_teacher):
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

           If we come back to you one more time in a conversation so that you know that the answers 
            
            you gave were not good enough and we ask you for better answers than you did.

            Any message you find will be output according to the following format:

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
            # Output the list of answers
            print(all_answers)
            #caculate avg score of answers
            average =0
            total_score =0
            counter_total_answer =0
            for answer in answers_teacher:
                for answerAI in all_answers:
                    score  = cosin.caculateSimilarityAnswersWithKeyWordAgentToTeacher(answerAI,answer.text ,answer.keyWords)
                    total_score += score
                    counter_total_answer+=1
            average  = total_score//counter_total_answer
            if average<=60:
                return bob
            else:
                return None

                        



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
