from model.cosineSimilarityMatrix import caculateSimilarityAnswersWithKeyWordStudentToAgent
class StudentModel:
    def __init__(self, correct_answers, keywords, points):
        self.correct_answers = correct_answers
        self.keywords = keywords
        #TODO make a list of point of every question 
        self.points = points  # Points for each question


    def grade_answers(self, student_answers):
        grades = []
        for i, answer_student in enumerate(student_answers):
            total_sum = 0
            count = 0  # Count matches for the current student answer
            
            for answer_ai in self.correct_answers:
                # Check if the questionId matches
                if answer_ai.questionId == i:
                    # Calculate cosine similarity 
                    similarity = caculateSimilarityAnswersWithKeyWordStudentToAgent(
                        answer_ai.text,  # Use .text if answer_ai has this attribute
                        answer_student,
                        self.keywords[i]
                    )
                    similarity = similarity *100
                    print(f'***similarity = {similarity}')
                    # Calculate grade based on similarity
                    if similarity < 0.8:
                        total_sum += similarity * self.points[i]
                    else:
                        total_sum += self.points[i]
                    count += 1
            
            # Avoid division by zero if no matches were found
            if count > 0:
                grade = total_sum / count
            else:
                grade = 0  # or some default grade
            
            grades.append(grade)
        return grades
    

    
    def final_grade(self, grades):
        return sum(grades)
    
    def save_grades(self, grades):
        print("NEED TO SAVE GRADES IN DB")
        pass
