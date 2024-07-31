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
                You have the correct answers and the questions points. You are given the student answers and their grades.
                Provide feedback for each answer, comparing it to the correct answer.
                If a student got full points, acknowledge it as a good answer but still provide some insight.
                                   
                Format your response as follows:
                Feedback for Question 1:
                [Your detailed feedback here]
                Points: [student's points]/[max points]

                Feedback for Question 2:
                [Your detailed feedback here]
                Points: [student's points]/[max points]

                ... (continue for all questions)

                Final grade: [sum of all answer grades]/[sum of all max points]
            ''',
            llm_config={"config_list": config_list},
            human_input_mode="NEVER",  # Never ask for human input.
        )

        initializer = ag.UserProxyAgent(name="Init")

        def state_transition(last_speaker, groupchat):
            #messages = groupchat.messages
            #text = str(messages[-1]["content"])

            if last_speaker is initializer:
                # Initialize feedback process
                return kevin
            elif last_speaker is kevin:
                #feedback = self.generate_feedback(text)
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
        feedback_pattern = re.compile(r'Feedback for Question (\d+):\n(.*?)\nPoints: (.*?)(?=\nFeedback for Question|\Z)', re.DOTALL)
        feedbacks = feedback_pattern.findall(text)

        # Extract the final grade
        final_grade_pattern = re.compile(r'Final grade: (.+)')
        final_grade_match = final_grade_pattern.search(text)
        final_grade = final_grade_match.group(1) if final_grade_match else "Not provided"

        # Combine the feedback
        combined_feedback = ""
        for feedback_tuple in feedbacks:
            if len(feedback_tuple) == 3:
                question_num, feedback, points = feedback_tuple
                combined_feedback += f"Feedback for Question {question_num}:\n{feedback.strip()}\n"
                combined_feedback += f"Points: {points.strip()}\n\n"
            else:
                combined_feedback += f"Unexpected feedback format: {feedback_tuple}\n\n"

        if not feedbacks:
            combined_feedback = "No structured feedback found. Here's the raw output:\n\n" + text

        combined_feedback += f"Final grade: {final_grade}"
        return combined_feedback
        # # Combine the feedback
        # combined_feedback = ""
        # for i, feedback in enumerate(feedbacks):
        #     combined_feedback += f"Feedback for Question {i + 1}:\n{feedback.strip()}\n\n"
        # if not feedbacks:
        #     combined_feedback = "No structured feedback found. Here's the raw output:\n\n" + text

        # combined_feedback += f"Final grade: {final_grade}"
        # return combined_feedback

    # def provide_feedback(self, grades):
    #     feedback = []
    #     total_score = sum(grades)

    #     for i, grade in enumerate(grades):
    #         feedback.append(f"Feedback for Question {i + 1}: You earned {grade:.2f} points.")

    #     feedback.append(f"Final grade: {total_score:.2f}")
    #     return "\n".join(feedback)
    

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