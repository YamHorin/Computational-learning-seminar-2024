class Answer():
    def __init__(self , answer_text, keyWords , id_question):
        self.text = answer_text
        self.keyWords = keyWords
        self.questionId = id_question
    def show(self):

        print( f'''
        {self.text} = answers_text
        {self.keyWords} = keyWords
        {self.questionId} = id_question
        ''')


class AnswerFactory():
    def createAnswer(self , answers_text, answer_points, keyWords , id_question):
        return Answer(answers_text, answer_points, keyWords , id_question)


class Question():
    def __init__(self , question_text, points, id_answer_teacher , answerFromTeacher):
        self.text = question_text
        self.points = points
        self.idAnswerTeacher = id_answer_teacher
        self.answerFromTeacher = answerFromTeacher
    def show(self):

        print( f'''
        {self.text} = question_text
        {self.points} = points
        {self.idAnswerTeacher} = id_answer_teacher
        {self.answerFromTeacher} = answerFromTeacher
        ''')


class QuestionFactory():
    def createAnswer(self ,  question_text, points, id_answer_teacher , answerFromTeacher):
        return Question( question_text, points, id_answer_teacher , answerFromTeacher)
    
