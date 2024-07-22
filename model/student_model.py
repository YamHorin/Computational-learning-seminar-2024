from Model.cosineSimilarityMatrix import caculateSimilarityAnswersWithKeyWordStudentToAgent


class StudentModel:
    def __init__(self, correct_answers, keywords, points):
        self.correct_answers = correct_answers
        self.keywords = keywords
        self.points = points  # Points for each question

    def grade_answers(self, student_answers):
        grades = []
        for i, answer in enumerate(student_answers):
            # Calculate cosine similarity
            similarity = caculateSimilarityAnswersWithKeyWordStudentToAgent(self.correct_answers[i], answer, self.keywords[i])
            # Calculate actual grade
            grade = similarity * self.points[i]
            grades.append(grade)
        return grades
    def save_grades(self, grades):
        print("NEED TO SAVE GRADES IN DB")
        pass
