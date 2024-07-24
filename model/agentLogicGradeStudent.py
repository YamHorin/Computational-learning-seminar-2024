    #TODO:
    ## write a function agent 3 that he will grade the answer base on the question 
    # and the answers from the bank
    # and give an explation of what he could do betetr
    # function will be  

import sys
import os
import re
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import autogen as ag

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

                You are an educational assistant who need to provide detailed feedback on each student's answer.
                
                You have the correct answers and the question point. You are given the student answers and answer grade.

                You will provide feedback based on the student's answers and grades, compare to the correct answer and points.
                
                If student got the full point it is a good answer and no need to improve it.
                                            
                Format your response as follows:

                Feedback for Question 1:
                [Your feedback here]

                Feedback for Question 2:
                [Your feedback here]

                Final grade: [sum of all answers grades]
                the final grade is the end of the output, you need to finish here.
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
                # print("Feedback:", feedback)
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

    def generate_feedback(self, text):
        # Parse the feedback provided by Kevin
        feedback_pattern = re.compile(r'Feedback for Question \d+:\n(.+?)\n', re.DOTALL)
        feedbacks = feedback_pattern.findall(text)

        # Calculate the grades and integrate static feedback
        static_feedback = self.provide_feedback(self.points)

        # Combine the dynamic feedback from Kevin with the static feedback
        combined_feedback = ""
        for i, feedback in enumerate(feedbacks):
            combined_feedback += f"Feedback for Question {i + 1}:\n{feedback}\n"
        
        combined_feedback += f"\n{static_feedback}"
        return combined_feedback

    def provide_feedback(self, grades):
        feedback = []
        total_score = sum(grades)

        for i, grade in enumerate(grades):
            feedback.append(f"Feedback for Question {i + 1}: You earned {grade:.2f} points.")

        feedback.append(f"Final grade: {total_score:.2f}")
        return "\n".join(feedback)
    

        # # Define function to process and provide feedback
    # def provide_feedback(self, grades):
    #     feedback = []
    #     total_score = sum(grades)

    #     for i, grade in enumerate(grades):
    #         feedback.append(f"Feedback for Question {i + 1}: You earned {grade:.2f} points.")

    #     feedback.append(f"Final grade: {total_score:.2f}")
    #     return "\n".join(feedback)


    # # Define function to process and provide feedback
    # def generate_feedback(self, text):
    #     # Here you would parse the text to extract grades and provide detailed feedback.
    #     feedback = []
    #     total_score = 0

    #     # Assuming `text` is a JSON string containing the grades for each question.
    #     grades = json.loads(text)

    #     for i, grade in enumerate(grades):
    #         feedback.append(f"Feedback for Question {i + 1}: You earned {grade['score']:.2f} points. {grade['feedback']}")
    #         total_score += grade['score']

    #     feedback.append(f"Final grade: {total_score:.2f}")
    #     return "\n".join(feedback)