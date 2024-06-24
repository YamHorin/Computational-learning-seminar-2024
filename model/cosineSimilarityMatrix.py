from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def caculateSimilarityAnswersWithKeyWordStudentToAgent(AI_answer,student_answer ,keyWords):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([AI_answer, student_answer])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    print("Cosine Similarity:", cosine_sim[0][0])
    for i, word in enumerate(student_answer):
        if (word in keyWords):
            print("word {i} found in key words ({word})")
            counter_key_words+=1

    print("Cosine Similarity:", cosine_sim[0][0])

    return (cosine_sim[0][0] *0.7 + counter_key_words*0.3)

    
    return cosine_sim[0][0]

def caculateSimilarityAnswersWithKeyWordAgentToTeacher(AI_answer,teacher_answer ,keyWords):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([AI_answer, teacher_answer])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    counter_key_words =0
    for i, word in enumerate(AI_answer):
        if (word in keyWords):
            print("word {i} found in key words ({word})")
            counter_key_words+=1

    print("Cosine Similarity:", cosine_sim[0][0])
    return (cosine_sim[0][0] *0.7 + counter_key_words*0.3)

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
