
import json
import random
from datetime import datetime
from abc import ABC, abstractmethod
from pathlib import Path


# File used to store quiz results
RESULTS_FILE = Path(__file__).with_name("results.json")


# Question class
class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display(self):
        print("\n" + self.question)

        for index, option in enumerate(self.options, start=1):
            print(f"{index}. {option}")


# Abstract base class
class Quiz(ABC):
    def __init__(self, student_name):
        self.student_name = student_name
        self.__score = 0
        self.__total = 0

    @abstractmethod
    def get_questions(self):
        pass

    def start(self):
        questions = self.get_questions()
        random.shuffle(questions)
        self.__total = len(questions)

        print("\n" + "=" * 45)
        print("             QUIZ STARTED")
        print("=" * 45)
        print(f"Student: {self.student_name}")

        for number, question in enumerate(questions, start=1):
            print(f"\nQuestion {number}/{self.__total}")
            question.display()

            while True:
                try:
                    choice = int(input("Enter your answer (1-4): "))

                    if 1 <= choice <= len(question.options):
                        break

                    print("Please enter a valid option number.")

                except ValueError:
                    print("Invalid input! Enter a number.")

            if question.options[choice - 1] == question.answer:
                print("Correct answer!")
                self.__score += 1
            else:
                print(f"Wrong answer! Correct answer: {question.answer}")

        self.show_result()

    def show_result(self):
        percentage = (self.__score / self.__total) * 100

        print("\n" + "=" * 45)
        print("              QUIZ RESULT")
        print("=" * 45)
        print(f"Student Name : {self.student_name}")
        print(f"Score        : {self.__score}/{self.__total}")
        print(f"Percentage   : {percentage:.2f}%")

        if percentage >= 80:
            grade = "Excellent"
        elif percentage >= 60:
            grade = "Good"
        elif percentage >= 40:
            grade = "Average"
        else:
            grade = "Needs Improvement"

        print(f"Performance  : {grade}")

        self.save_result(percentage, grade)

    def save_result(self, percentage, grade):
        result = {
            "student_name": self.student_name,
            "category": self.__class__.__name__.replace("Quiz", ""),
            "score": self.__score,
            "total_questions": self.__total,
            "percentage": round(percentage, 2),
            "performance": grade,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        try:
            if RESULTS_FILE.exists():
                with open(RESULTS_FILE, "r", encoding="utf-8") as file:
                    results = json.load(file)
            else:
                results = []

            if not isinstance(results, list):
                results = []

            results.append(result)

            with open(RESULTS_FILE, "w", encoding="utf-8") as file:
                json.dump(results, file, indent=4)

            print("\nResult saved successfully!")

        except (OSError, json.JSONDecodeError) as error:
            print(f"Could not save result: {error}")


# Inheritance: PythonQuiz inherits from Quiz
class PythonQuiz(Quiz):
    def get_questions(self):
        return [
            Question(
                "Which keyword defines a function in Python?",
                ["func", "define", "def", "function"],
                "def"
            ),
            Question(
                "Which data type stores True or False?",
                ["int", "bool", "str", "list"],
                "bool"
            ),
            Question(
                "Which symbol is used for comments in Python?",
                ["//", "#", "/*", "--"],
                "#"
            ),
            Question(
                "Which method adds an item to a list?",
                ["add()", "insertEnd()", "append()", "push()"],
                "append()"
            ),
            Question(
                "Which keyword is used for inheritance?",
                ["extends", "inherits", "super", "class"],
                "class"
            ),
            Question(
                "What is the output of 3 ** 2?",
                ["5", "6", "9", "8"],
                "9"
            ),
            Question(
                "Which collection stores key-value pairs?",
                ["List", "Tuple", "Dictionary", "Set"],
                "Dictionary"
            ),
            Question(
                "Which block handles exceptions?",
                ["catch", "error", "except", "final"],
                "except"
            ),
            Question(
                "Which keyword creates a class?",
                ["object", "class", "new", "struct"],
                "class"
            ),
            Question(
                "Which function converts a value to an integer?",
                ["str()", "float()", "int()", "bool()"],
                "int()"
            )
        ]


# Inheritance and polymorphism
class GeneralKnowledgeQuiz(Quiz):
    def get_questions(self):
        return [
            Question(
                "What is the capital of India?",
                ["Mumbai", "New Delhi", "Chennai", "Hyderabad"],
                "New Delhi"
            ),
            Question(
                "Which planet is known as the Red Planet?",
                ["Earth", "Venus", "Mars", "Jupiter"],
                "Mars"
            ),
            Question(
                "How many days are there in a leap year?",
                ["365", "366", "364", "360"],
                "366"
            ),
            Question(
                "Which is the largest ocean?",
                ["Atlantic", "Indian", "Arctic", "Pacific"],
                "Pacific"
            ),
            Question(
                "Which is the national animal of India?",
                ["Lion", "Tiger", "Elephant", "Leopard"],
                "Tiger"
            )
        ]


class ComputerScienceQuiz(Quiz):
    def get_questions(self):
        return [
            Question(
                "What does CPU stand for?",
                [
                    "Central Processing Unit",
                    "Computer Personal Unit",
                    "Central Program Utility",
                    "Control Processing User"
                ],
                "Central Processing Unit"
            ),
            Question(
                "Which language is primarily used to structure web pages?",
                ["CSS", "HTML", "SQL", "Python"],
                "HTML"
            ),
            Question(
                "Which of these is an operating system?",
                ["Oracle", "Linux", "Python", "HTML"],
                "Linux"
            ),
            Question(
                "What does RAM stand for?",
                [
                    "Read Access Memory",
                    "Random Access Memory",
                    "Run Active Memory",
                    "Remote Access Machine"
                ],
                "Random Access Memory"
            ),
            Question(
                "Which number system uses only 0 and 1?",
                ["Decimal", "Octal", "Binary", "Hexadecimal"],
                "Binary"
            )
        ]


# File handling: display saved results
def view_results():
    try:
        if not RESULTS_FILE.exists():
            print("\nNo quiz results found yet.")
            return

        with open(RESULTS_FILE, "r", encoding="utf-8") as file:
            results = json.load(file)

        if not results:
            print("\nNo quiz results found yet.")
            return

        if not isinstance(results, list):
            print("\nThe results file has an invalid format.")
            return

        print("\n" + "=" * 65)
        print("                    PREVIOUS QUIZ RESULTS")
        print("=" * 65)

        for index, result in enumerate(results, start=1):
            print(f"\nResult {index}")
            print(f"Name       : {result['student_name']}")
            print(f"Category   : {result['category']}")
            print(
                f"Score      : {result['score']}/"
                f"{result['total_questions']}"
            )
            print(f"Percentage : {result['percentage']}%")
            print(f"Performance: {result['performance']}")
            print(f"Date       : {result['date']}")

    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        print(f"Unable to read results: {error}")


# Main menu
def main():
    while True:
        print("\n" + "=" * 45)
        print("           QUIZ MASTER APPLICATION")
        print("=" * 45)
        print("1. Python Quiz")
        print("2. General Knowledge Quiz")
        print("3. Computer Science Quiz")
        print("4. View Previous Results")
        print("5. Exit")

        try:
            choice = int(input("\nEnter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 5:
            print("\nThank you for using Quiz Master!")
            break

        if choice == 4:
            view_results()
            continue

        quiz_types = {
            1: PythonQuiz,
            2: GeneralKnowledgeQuiz,
            3: ComputerScienceQuiz
        }

        if choice not in quiz_types:
            print("Invalid choice! Select a number from 1 to 5.")
            continue

        student_name = input("Enter your name: ").strip()

        if not student_name:
            print("Name cannot be empty.")
            continue

        quiz = quiz_types[choice](student_name)
        quiz.start()


if __name__ == "__main__":
    main()
