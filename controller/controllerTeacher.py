
from model.agentLogixMake_AI_Answers import initialize_agents
import controller.sql_server as sql

class controllerTeacher():
       def __init__(self,gui_app ,pwd):
              self.app =gui_app
              self.sql_server = sql.sql_server( 'root',pwd,'ai_answers')
       def runApp(self):
              self.app.mainloop()
              self.getAIAnswers(self.app.questions ,self.app.answers )

       def getAIAnswers(self,questions , answers):
              print("Initializing agents and starting group chat...")
              self.sql_server.add_answers(answers)
              self.sql_server.add_questions(questions)
              key_words  = [f"{question.keyWords}" for question in questions]
              
              initializer, manager, groupchat = initialize_agents(answers , key_words)
              questions_text = "Questions:\n" + "\n".join(f"{i}: {question.text}" for i, question in enumerate(questions))
              answers_text = "Answers:\n" + "\n".join(f"{i}: {answer.text}" for i, answer in enumerate(answers))
              key_words_text = "Keywords:\n" + "".join(f"{question.keyWords}" for question in questions)

              # Combine all parts into one message
              msg = f"{questions_text}\n\n{answers_text}\n\n{key_words_text}"
              initializer.initiate_chat(manager, message=msg)
              messages = groupchat.messages
              text = str(messages[-1]["content"])
              print (text)
              return text
       



