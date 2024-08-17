import View.answers_window as window
from model.agentLogixMake_AI_Answers import initialize_agents
import View.objectsPrograms as obj
import controller.sql_server as sql
import re
class controllerTeacher():
       def __init__(self,gui_app ,pwd):
              self.app =gui_app
              self.sql_server = sql.sql_server( 'root',pwd,'ai_answers')
       def runApp(self):
              self.app.mainloop()
              answers_ai = self.getAIAnswers(self.app.questions ,self.app.answers )
              answers_ai = self.teacher_edit_win(answers_ai)
              self.sql_server.add_answers(answers_ai)
              self.sql_server.close_connection()
       def teacher_edit_win(self ,answers_ai ):
            self.app_edit = window.TestAnswersWindow(answers_ai , self.app.questions)
            self.app_edit.mainloop()
            return self.app_edit.answers
       def enter_agents_answers_in_db(self,answers_agent , question_teacher):
            factory = obj.AnswerFactory_Agent()
            answers_to_db = []
            for question_teacher in question_teacher:  
                for answer in answers_agent:
                     answer_obj = factory.createAnswer(answer
                                                       ,question_teacher.points 
                                                       , question_teacher.id )
                     answers_to_db.append(answer_obj)
            self.sql_server.add_answers(answers_to_db)
            
       def getAIAnswers(self,questions , answers):
              print("Initializing agents and starting group chat...")
              self.sql_server.add_answers(answers)
              self.sql_server.add_questions(questions)
              key_words  = [f"{question.keyWords}" for question in questions]
              
              initializer, manager, groupchat = initialize_agents(answers , key_words)
              questions_text = "Questions:\n" + "\n".join(f"{i}: {question.text}" for i, question in enumerate(questions))
              answers_text = "Answers:\n" + "\n".join(f"{i}: {answer.text}" for i, answer in enumerate(answers))
              key_words_text = "Keywords for question:\n" + "\n".join(f"{question.id}.{question.keyWords}" for question in questions)

              # Combine all parts into one message
              msg = f"{questions_text}\n\n{answers_text}\n\n{key_words_text}"
              initializer.initiate_chat(manager, message=msg)
              messages = groupchat.messages
              text = str(messages[-1]["content"])
              if messages[-1]['name'] == 'helper':
                     text = str(messages[-2]["content"])
              print (text)
              list_answers = extract_answers(text , questions)
              return list_answers
       



def extract_answers(text , questions):
    # Split the text into lines
    lines = text.strip().split('\n')

    # Find the line containing the answers
    answers = []
    counter=0
    factory = obj.AnswerFactory_Agent()
    for line in lines:
        stripped_line = line.strip()

        if stripped_line and stripped_line[0].isdigit() and stripped_line[1] == '.':
            if stripped_line.startswith("1."):
                counter += 1
            answer = stripped_line.split('. ', 1)[-1].strip()
            answer_obj = factory.createAnswer(answer ,questions[counter-1].points ,counter)
            answer_obj.show()
            answers.append(answer_obj)
            
        if stripped_line and stripped_line[0].isdigit() and stripped_line[1] == ':':
            if stripped_line.startswith("1:"):
                counter += 1
            answer = stripped_line.split('. ', 1)[-1].strip()
            answer_obj = factory.createAnswer(answer ,questions[counter-1].points ,counter)
            answer_obj.show()
            answers.append(answer_obj)
    
    return answers
