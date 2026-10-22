Quiz Master - Python Quiz Application
1. Project Title
Quiz Master: Python-Based Quiz Application
2. Project Description
Quiz Master is a console-based quiz application developed using Python. It allows students to test their knowledge through multiple-choice questions in three categories: Python Programming, General Knowledge, and Computer Science.

Users enter their name, select a quiz category, and answer questions by entering the number of their chosen option. At the end of the quiz, the application calculates the score and percentage, displays a performance level, and saves the result in a JSON file. Users can view their previous quiz results from the main menu.

This project demonstrates the practical use of Python concepts learned during the internship.
3. Features
- Three quiz categories:
  - Python Programming
  - General Knowledge
  - Computer Science
- Multiple-choice questions with four options.
- Randomized question order.
- Automatic score and percentage calculation.
- Performance evaluation based on the percentage.
- Immediate feedback showing whether an answer is correct.
- Input validation for menu choices and answers.
- Exception handling for invalid input and file errors.
- Saves quiz results in results.json.
- Displays previously saved quiz results.
- Uses object-oriented programming to organize the code.
4. Technologies Used
- Python 3 — main programming language.
- json — saves and loads quiz results.
- random — shuffles question order.
- datetime — records the date and time of each result.
- pathlib — manages the results file path.
- abc — supports abstract classes and methods.
- PyCharm or VS Code — code editor and development environment.
- Git and GitHub — source control and project hosting.
The application uses Python's built-in libraries, so no external Python packages are required.
5. Python Concepts Used
- Variables and data types: Stores names, scores, percentages, and other information.
- Input and output: Uses input() to receive user responses and print() to display information.
- Operators and type casting: Uses arithmetic and comparison operators and converts menu choices using int().
- Conditional statements: Uses if, elif, and else to validate answers and assign performance levels.
- Loops: Uses for loops to display questions and while loops to repeat the menu and validate input.
- Functions: Organizes tasks into reusable functions and methods.
- Data structures: Uses lists and dictionaries to store questions and results.
- File handling: Reads and writes result data using JSON files.
- Exception handling: Uses try and except to handle invalid input and file-related errors.
- Classes and objects: Uses Question, Quiz, and category-specific quiz classes.
- Constructors: Uses __init__() to initialize objects.
- Inheritance: Quiz category classes inherit common functionality from Quiz.
- Polymorphism: Each quiz category implements its own get_questions() method.
- Encapsulation: Uses double-underscore attributes for the score and total-question count.
- Abstraction: Uses ABC and @abstractmethod to define the quiz interface.
- Git and GitHub: Supports version control and sharing the project repository.
- 6. Installation / Setup
Requirements
- Python 3 installed on your computer.
- PyCharm, VS Code, or another Python-compatible editor.
- Git (optional, for version control and GitHub).
Setup Steps
1. Download or clone the project repository, or create a folder named QuizMaster.
2. Save the main Python program as main.py.
3. Open the project folder in PyCharm or another editor.
4. Confirm that Python 3 is installed by running:
   python --version
   On some Windows systems, use:
   py --version
5. No external packages need to be installed for the current version of the project.
Project Structure
QuizMaster/
├── main.py
├── README.md
├── .gitignore
└── results.json   # Created automatically after a quiz result is saved
7. How to Run the Project
1. Open a terminal in the QuizMaster project folder.
2. Run the application:
   python main.py
   On some Windows systems, use:
   py main.py
3. Select an option from the main menu:
   - 1 — Python Quiz
   - 2 — General Knowledge Quiz
   - 3 — Computer Science Quiz
   - 4 — View Previous Results
   - 5 — Exit
4. Enter your name when prompted.
5. Answer each question by entering the number of the selected option.
6. After the final question, review your score, percentage, and performance level.
7. Choose option 4 from the main menu to view saved results.
The results.json file is created automatically when the application successfully saves a quiz result.
8. Future Improvements
The project can be enhanced with the following features:
- Add a graphical user interface using Tkinter or PyQt.
- Introduce a timer for each question or quiz.
- Add easy, medium, and hard difficulty levels.
- Create a leaderboard to display top scores.
- Add more quiz categories and questions.
- Use SQLite or MySQL for storing larger amounts of data.
- Add student login and authentication.
- Allow administrators to add, edit, or remove questions.
- Generate detailed performance reports.
- Develop a web-based version using Flask or Django.
Conclusion
Quiz Master is a practical Python project that combines quiz functionality with automatic evaluation and persistent result storage. It demonstrates Python fundamentals, exception handling, file handling, built-in libraries, and object-oriented programming. The application can be extended into a more advanced quiz platform in the future.
Author Name: Gnaneswara Chokkana

Project: Quiz Master - Python