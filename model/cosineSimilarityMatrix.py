from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def caculateSimilarityAnswersWithKeyWordStudentToAgent(AI_answer,student_answer ,keyWords):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([AI_answer, student_answer])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    print("Cosine Similarity:", cosine_sim[0][0])
    # Initialize counter for keywords
    counter_key_words = 0
    
    if keyWords:
        ai_words = student_answer.split()
        total_keywords = len(keyWords)
        counter_key_words = sum(1 for word in ai_words if word in keyWords) / total_keywords
    

    print("Cosine Similarity:", cosine_sim[0][0])

    return (cosine_sim[0][0] *0.7 + counter_key_words*0.3)

    

def calculateSimilarityAnswersWithKeyWordAgentToTeacher(AI_answer, teacher_answer, keyWords):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([AI_answer, teacher_answer])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    # Initialize counter for keywords
    counter_key_words = 0
    
    if keyWords:
        ai_words = AI_answer.split()
        total_keywords = len(keyWords)
        counter_key_words = sum(1 for word in ai_words if word in keyWords) / total_keywords
    
    # print(f"Cosine Similarity: {cosine_sim[0][0]}\n\n")
    # print(f"Keyword Fraction: {counter_key_words}")s

    if keyWords:
        return cosine_sim[0][0] * 0.7 + counter_key_words * 0.3
    else:
        return cosine_sim[0][0]
#'''
# agent1 list answer
# check similarity  
# check key words ?how much words have been used from the key words list 0-10
# simitiry -70 %
# key words -30 %
# send score 
# 
# 
# 
# 
# 
# '''
