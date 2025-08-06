questions = ("How many elements in periodic table?: ", "Which animal lays largest Egg?: ", "What is the most abundant ga in the Earth's atmosphare?: ", "How many bones in human body?: ",
             "Which planet in the solar system is the hottest?: ", "What is the capital of France?: ", "What is the largest mammal?: ", "What is the smallest country in the world?: ",
             "What is the largest ocean on Earth?: ", "What is the longest river in the world?: ")
# fill these A B C D options with with differnt options
options = (("A. 118", "B. 100", "C. 90", "D. 120"),
           ("A. Crocodile", "B. Ostrich", "C. Eagle", "D. Penguin"),
           ("A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Helium"),
           ("A. 206", "B. 205", "C. 210", "D. 200"),
           ("A. Mars", "B. Jupiter", "C. Venus", "D. Mercury"),
           ("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
           ("A. Blue Whale", "B. Elephant", "C. Giraffe", "D. Great White Shark"),
           ("A. Vatican City", "B. Monaco", "C. San Marino", "D. Liechtenstein"),
           ("A. Atlantic Ocean", "B. Indian Ocean",
            "C. Pacific Ocean", "D. Arctic Ocean"),
           ("A. Nile River", "B. Amazon River",
            "C. Yangtze River", "D. Mississippi River")
           )
answers = ("A", "B", "C", "D",
           "C", "B", "A", "D",
           "C", "A")
# guesses will be stored in this list
guesses = []
# score will be stored in this variable
score = 0
# loop through each question
question_num = 0


for question in questions:
    print("--" * 20)
    print(question)
    print("--" * 20)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The correct answer is:", answers[question_num])
        print(f"Your answer: {guess}, Correct answer: {answers[question_num]}")
    print("Your current score is:", score)
    question_num += 1
