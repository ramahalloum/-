import csv

def load_questions_from_csv(file_path):
    questions = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            questions.append(row)
    return questions

def quiz_user(questions):
    score = 0
    for q in questions:
        print(q[0])
        user_answer = input("Your answer: ")
        if user_answer.lower() == q[1].lower():
            score += 1
    return score

def save_result_to_csv(user_name, score):
    with open('quiz_results.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([user_name, score])

file_path = 'quiz_questions.csv'
questions = load_questions_from_csv(file_path)

user_name = input("Enter your name: ")
user_score = quiz_user(questions)

print(f"Quiz completed! Your score: {user_score}/{len(questions)}")
save_result_to_csv(user_name, user_score)
