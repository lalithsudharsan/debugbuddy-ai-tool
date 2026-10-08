🐞 DebugBuddy

Beginner-Friendly Coding Error Explainer

DebugBuddy is a beginner-friendly tool that helps students understand coding errors instead of simply giving them the answer.

It allows users to enter their code and error message, then explains what went wrong in simple language, identifies the relevant line, and helps the user learn how to fix it.

---

🚀 Features

- 🔍 Error Detection – Identifies the type of coding error.
- 📍 Line Identification – Points out the line where the error occurs when possible.
- 💡 Simple Explanation – Explains the error in beginner-friendly language.
- 🧠 Learn Mode – Provides progressive hints so users can solve the problem themselves.
- 🔧 Fix Mode – Provides the corrected code with a short explanation.
- 📚 Concept Explanation – Explains the programming concept behind the error.
- 📝 Tiny Examples – Gives simple examples to reinforce learning.

---

🎯 How It Works

User enters Code + Error Message
              ↓
       DebugBuddy analyzes it
              ↓
       Identifies the error
              ↓
     Explains the problem simply
              ↓
   ┌──────────┴──────────┐
   ↓                     ↓
Learn Mode            Fix Mode
   ↓                     ↓
Progressive hints    Corrected code
   ↓                     ↓
User solves it       Short explanation

---

🧑‍💻 Example

Input

numbers = [1, 2, 3]

for i in range(5):
    print(numbers[i])

Error

IndexError: list index out of range

DebugBuddy Explanation

The loop tries to access positions that do not exist in the list.

The list contains only 3 elements, so valid indexes are:

0, 1, 2

The loop reaches index "3" and beyond, causing the error.

---

🛠️ Technology Used

- Python
- Streamlit
- Git & GitHub

---

📦 Installation

Clone the repository:

git clone <YOUR_GITHUB_REPOSITORY_URL>

Move into the project directory:

cd DebugBuddy

Install the required dependencies:

pip install -r requirements.txt

---

▶️ Run the Application

Start the Streamlit application using:

streamlit run app.py

The application will open in your browser.

---

📂 Project Structure

DebugBuddy/
│
├── app.py
├── requirements.txt
├── README.md
└── ...

---

🌱 Project Goal

The goal of DebugBuddy is to make debugging a learning experience rather than just an answer-generating process.

Instead of immediately showing users the corrected code, DebugBuddy encourages them to understand:

1. What went wrong
2. Why the error happened
3. Where the error occurred
4. How they can solve it
5. What programming concept they should learn

---

🔮 Future Improvements

- Support for more programming languages
- More advanced error classification
- Improved line-level error detection
- Interactive debugging exercises
- More programming concepts and examples
- AI-powered explanations
- User progress tracking

---

🤝 Contributing

Contributions are welcome!

If you have an idea for improving DebugBuddy:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Create a Pull Request

---

📜 License

This project is open source and available under the MIT License.