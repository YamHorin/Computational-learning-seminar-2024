
# before you start coding you need to install autoGen 
# run this command in the terminal:
#   pip install pyautogen
#   ollama pull llama3
#   install docker 
#   docker build -f .devcontainer/Dockerfile -t autogen_base_img https://github.com/microsoft/autogen.git#main
#   docker build -f .devcontainer/full/Dockerfile -t autogen_full_img https://github.com/microsoft/autogen.git#main
#   docker run -d --name exciting_chatterjee alpine watch "date >> /var/log/date.log"

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import autogen as ag
import re
from model.cosineSimilarityMatrix import calculateSimilarityAnswersWithKeyWordAgentToTeacher as cosin

# answers_teacher - list of View.objectsPrograms Answers
def initialize_agents(answers_teacher, key_words):
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

            You are a professor who must provide 5 different answers to each question the user will send you.

            You need to answer with the key words we will provide you.

            You need to answer as close as possible to the answers we will provide you.

            You need to give the answers that you think are the most correct. Ensure the answers are accurate.

            Each answer should be numbered separately.

            If we come back to you one more time in a conversation, it means the answers you gave were not good enough, and we ask you for better answers than you did.

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
            and so on.
        ''',
        llm_config={"config_list": config_list},
        human_input_mode="NEVER",  # Never ask for human input.
    )


    helper = ag.ConversableAgent(
        "helper",
        system_message='''
        Your job is to tell Bob to the following message: "hey bob remake the answers better" for every time it's your turn to speak in the chat.
        ''',
        llm_config={"config_list": config_list},
        human_input_mode="NEVER",  # Never ask for human input.

        )
        
    

    initializer = ag.UserProxyAgent(
        name="Init",
        system_message='Please provide the questions and key words to Bob.',
    )

    def state_transition(last_speaker, groupchat):
        messages = groupchat.messages
        text = str(messages[-1]["content"])
        iteration_count = len([m for m in messages if m['name'] == 'bob'])

        if iteration_count >= 5:  # Set a maximum number of iterations
            return initializer  # End the conversation after 5 iterations
    
        if last_speaker is initializer:
            # init -> retrieve
            return bob
        elif last_speaker is helper:
            return bob
        elif last_speaker is bob:
            # Calculate similarity to each answer
            all_answers = extract_answers(text)
            total_score = 0
            counter_total_answer = len(all_answers)
            if (counter_total_answer==0):
                return bob  # Request better answers from Bob

            for answer, key_words_answer in zip(answers_teacher, key_words):
                for answerAI in all_answers:
                    score = cosin(answerAI, answer.text, key_words_answer)
                    total_score += score * 100
            average = total_score / counter_total_answer
            #print(f"Average score: {average}")
            if average <= 65:
                return helper  # Request better answers from Bob
            else:
                return initializer  # End conversation if answers are satisfactory

    # Making the group chat
    groupchat = ag.GroupChat(
        agents=[initializer, bob, helper],
        messages=[],
        max_round=6,
        speaker_selection_method=state_transition,
    )

    # Manager
    manager = ag.GroupChatManager(groupchat=groupchat, llm_config={"model": "llama3", "base_url": "http://localhost:11434/v1", "api_key": "ollama"})

    return initializer, manager, groupchat

def extract_answers(text):
    # Split the text into lines
    lines = text.strip().split('\n')

    # Find the line containing the answers
    answers_start = False
    answers = []

    for line in lines:
        if line.strip().startswith("the answers for"):
            answers_start = True
            continue
        
        if answers_start:
            # Remove leading numbers and dots
            if line.strip() and not line.strip().lower().startswith("end"):
                answer = line.split('. ', 1)[-1]
                answers.append(answer)
            elif line.strip().lower().startswith("end"):
                answers_start = False
    
    return answers

# Example usage:
# initializer, manager, groupchat = initialize_agents(answers_teacher, key_words)
# manager.start_chat()
