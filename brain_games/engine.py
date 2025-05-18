# engine module for basic logic
#
#
def run_engine(description, generate_round):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    print(description)
    
    for _ in range(3):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        else:
            print("Correct!")
    
    print(f"Congratulations, {name}!")

