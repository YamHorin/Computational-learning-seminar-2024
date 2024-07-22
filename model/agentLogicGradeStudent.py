    #TODO:
    ## write a function agent 3 that he will grade the answer base on the question 
    # and the answers from the bank
    # and give an explation of what he could do betetr
    # function will be  

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import autogen as ag
import re
import json
from Model.cosineSimilarityMatrix import caculateSimilarityAnswersWithKeyWordStudentToAgent

class KevinAgent:
    def __init__(self, correct_answers, points):
        self.correct_answers = correct_answers
        self.points = points

    def initialize_agents(self):
        config_list = [
            {
                "model": "llama3",
                "base_url": "http://localhost:11434/v1",
                "api_key": "ollama",
            }
        ]

        kevin = ag.ConversableAgent(
            "kevin",
            system_message='''
                Your name is Kevin.

                You are an educational assistant who must provide detailed feedback on each student's answer.

                You will provide feedback based on the student's answers and grades.
            
                Use the provided grades to give detailed feedback for each question.
                
                For each answer, you need to provide a note on why points were lost or why the answer received a specific grade.

                Your feedback should explain what was correct or incorrect and how the student can improve.

                After providing feedback for all answers, calculate the total grade and provide the final score.
                
                Format your response as follows:

                Feedback for Question 1:
                [Your feedback here]

                Feedback for Question 2:
                [Your feedback here]

                Final grade: [sum of all answers grades]
            ''',
            llm_config={"config_list": config_list},
            human_input_mode="NEVER",  # Never ask for human input.
        )

        initializer = ag.UserProxyAgent(name="Init")

        def state_transition(last_speaker, groupchat):
            messages = groupchat.messages
            text = str(messages[-1]["content"])

            if last_speaker is initializer:
                # Initialize feedback process
                return kevin
            elif last_speaker is kevin:
                feedback = self.generate_feedback(text)
                print("Feedback:", feedback)
                return None  # End the conversation after providing feedback

        # Creating the group chat
        groupchat = ag.GroupChat(
            agents=[initializer, kevin],
            messages=[],
            max_round=20,
            speaker_selection_method=state_transition,
        )

        # Manager
        manager = ag.GroupChatManager(
            groupchat=groupchat,
            llm_config={"model": "llama3", "base_url": "http://localhost:11434/v1", "api_key": "ollama"}
        )

        return initializer, manager, groupchat
   
    # Define function to process and provide feedback
    def provide_feedback(self, grades):
        feedback = []
        total_score = sum(grades)

        for i, grade in enumerate(grades):
            feedback.append(f"Feedback for Question {i + 1}: You earned {grade:.2f} points.")

        feedback.append(f"Final grade: {total_score:.2f}")
        return "\n".join(feedback)
