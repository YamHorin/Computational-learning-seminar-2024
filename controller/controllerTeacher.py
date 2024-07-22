
from Model.agentLogixMake_AI_Answers import initialize_agents
import controller.sql_server as sql

class controllerTeacher():
       def __init__(self,gui_app ,pwd):
              self.app =gui_app
              self.sql_server = sql.sql_server( 'root',pwd,'ai_answers')
       def runApp(self):
              self.app.mainloop()
              self.getAIAnswers(self.app.questions ,self.app.answers , self.app.key_words)

       def getAIAnswers(self,questions , answers , key_words):
              print("Initializing agents and starting group chat...")
              self.sql_server.add_answers(answers)
              self.sql_server.add_questions(questions)
              
              
              initializer, manager, groupchat = initialize_agents(answers)
              msg = ("Questions: ".join(i+question+"\n" for i,question in enumerate(questions))+
                     "Answers :".join(i+answer+"\n" for i,answer in enumerate(answers))+
                     "key words :".join(i+key_word+"\n" for i,key_word in enumerate(key_words)))
              initializer.initiate_chat(manager, message=msg)
       



