from model.cosineSimilarityMatrix import caculateSimilarityAnswersWithKeyWordStudentToAgent
class StudentModel:
    def __init__(self, correct_answers, keywords, points):
        self.correct_answers = correct_answers
        self.keywords = keywords
        #TODO make a list of point of every question 
        self.points = points  # Points for each question


    def grade_answers(self, student_answers):
        grades = []
        print(*self.correct_answers)
        count = 0
        for i, answer_student in enumerate(student_answers):
            grade=0
            sum = 0
            for answer_ai in self.correct_answers:
                count+=1
                # Calculate cosine similarity 
                if (answer_ai.questionId == i):
                    similarity = caculateSimilarityAnswersWithKeyWordStudentToAgent(self.correct_answers[i].text,
                                                                                    answer_student
                                                                                    , self.keywords[i])
                    # Calculate actual grade
                    if similarity < 0.8:
                        sum += similarity * self.points[i]
                    else: 
                        sum += self.points[i]
            grade = sum / count
            grades.append(grade)
        self.save_grades(grades)
        return grades
    
    def final_grade(self, grades):
        return sum(grades)
    
    def save_grades(self, grades):
        print("NEED TO SAVE GRADES IN DB")
        pass
