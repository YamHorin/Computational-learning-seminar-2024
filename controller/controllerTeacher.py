from model.agentLogixMake_AI_Answers import initialize_agents
import controller.sql_server as sql


def getAIAnswers(questions , answers , key_words):
    sql.sql_server.add_answers(answers)
    sql.sql_server.add_questions(questions)
    
    
    initializer, manager, groupchat = initialize_agents(answers)
    msg = ("Questions: ".join(i+question+"\n" for i,question in enumerate(questions))+
           "Answers :".join(i+answer+"\n" for i,answer in enumerate(answers))+
           "key words :".join(i+key_word+"\n" for i,key_word in enumerate(key_words)))
    initializer.initiate_chat(manager, message=msg)
    



