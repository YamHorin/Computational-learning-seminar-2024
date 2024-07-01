class Answer():
    def __init__(self , answer_text , id_question , creadedBy):
        self.text = answer_text
        self.questionId = id_question
        self.createdBy = creadedBy

    def show(self):

        print( f'''
        {self.text} = answers_text
        {self.questionId} = id_question
        {self.createdBy} = creadedBy
        ''')


class AnswerFactory_teacher():
    def createAnswer(self , answers_text, answer_points, id_question):
        return Answer(answers_text, id_question , "teacher")

class AnswerFactory_Agent():
    def createAnswer(self , answers_text, answer_points, id_question):
        return Answer(answers_text, id_question , "Agent")

class Question():
    def __init__(self ,id, question_text, points,  keyWords,id_answer_teacher , answerFromTeacher ,test_id):
        #keys word not gonna be store in the sql
        self.id  =id
        self.keyWords = keyWords
        self.text = question_text
        self.points = points
        self.idAnswerTeacher = id_answer_teacher
        self.answerFromTeacher = answerFromTeacher
        self.test_id =test_id
    def show(self):

        print( f'''
        {self.id}  =id
        {self.test_id} =test_id
        {self.keyWords} = keyWords
        {self.text} = question_text
        {self.points} = points
        {self.idAnswerTeacher} = id_answer_teacher
        {self.answerFromTeacher} = answerFromTeacher
        ''')


class QuestionFactory():
    def __init__(self , num):
        self.id =num
    def createQuestion(self, question_text, points,  keyWords,id_answer_teacher , answerFromTeacher ,test_id):
        self.id+=1
        return Question(self.id, question_text, points,  keyWords,id_answer_teacher , answerFromTeacher ,test_id)
    
