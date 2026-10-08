import os
import json
import requests

API_KEY = os.environ["GROQ_API_KEY"]
URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "openai/gpt-oss-120b"


SYSTEM_PROMPT = """You are a patient programming teacher for first-year students.
The student gives you code (with line numbers) and an error message.

Reply with ONLY valid JSON using exactly these keys:
error_type, line, explanation, hints, fix, concept.

Rules:
- Use simple words. Explain any jargon.
- "line" is the line number where the problem is (integer, or null if unsure).
- "explanation" is 2-3 sentences on what went wrong and why.
- Describe the problem only. Do NOT say how to fix it.
- "hints" is a list of exactly 3 strings.
- Hint 1 is a gentle nudge.
- Hint 2 is more specific.
- Hint 3 almost gives the answer but not the full code.
- "fix" is the full corrected code, without line numbers.
- "concept" is a short explanation of the underlying idea with a tiny example.
- Never invent errors that are not in the code."""


EXPLAIN_PROMPT = """You are a patient programming teacher for first-year students.

The student gives you code and asks what the code does or what it is used for.

Reply with ONLY valid JSON using exactly these keys:
purpose, explanation, line_by_line, output, concept.

Rules:
- Use very simple beginner-friendly language.
- "purpose" should briefly explain what the whole program is for.
- "explanation" should explain the overall working in 2-4 sentences.
- "line_by_line" must be a list of strings explaining important lines in order.
- "output" should show the expected output if the code produces output.
- If the output depends on user input or cannot be determined, say so.
- "concept" should explain the main programming concept used, with a tiny example.
- Never invent functionality that is not present in the code."""


EMPTY = {
    "error_type": "Unknown",
    "line": None,
    "explanation": "Sorry, I couldn't analyze this. Please try again.",
    "hints": [],
    "fix": "",
    "concept": "",
}


def number_lines(code):
    return "\n".join(
        f"{i}: {line}"
        for i, line in enumerate(code.splitlines(), 1)
    )


def analyze_error(code, error, language="Python", mode="learn"):

    if not code.strip() or not error.strip():
        return {
            **EMPTY,
            "explanation": "Please paste both your code and the error."
        }

    user_msg = (
        f"Language: {language}\n\n"
        f"Code:\n{number_lines(code)}\n\n"
        f"Error:\n{error}"
    )

    try:
        r = requests.post(
            URL,
            headers={
                "Authorization": f"Bearer {API_KEY}"
            },
            json={
                "model": MODEL,
                "messages": [
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT
                    },
                    {
                        "role": "user",
                        "content": user_msg
                    }
                ],
                "response_format": {
                    "type": "json_object"
                },
            },
            timeout=60,
        )

        data = json.loads(
            r.json()["choices"][0]["message"]["content"]
        )

    except Exception as e:
        print("Error:", e)
        return EMPTY

    result = {**EMPTY, **data}

    if mode == "learn":
        result["fix"] = ""

    return result


def explain_code(code, language="Python"):

    if not code.strip():
        return {
            "purpose": "No code was provided.",
            "explanation": "",
            "line_by_line": [],
            "output": "",
            "concept": ""
        }

    user_msg = (
        f"Language: {language}\n\n"
        f"Code:\n{number_lines(code)}"
    )

    try:
        r = requests.post(
            URL,
            headers={
                "Authorization": f"Bearer {API_KEY}"
            },
            json={
                "model": MODEL,
                "messages": [
                    {
                        "role": "system",
                        "content": EXPLAIN_PROMPT
                    },
                    {
                        "role": "user",
                        "content": user_msg
                    }
                ],
                "response_format": {
                    "type": "json_object"
                },
            },
            timeout=60,
        )

        return json.loads(
            r.json()["choices"][0]["message"]["content"]
        )

    except Exception as e:
        print("Error:", e)

        return {
            "purpose": "Sorry, I couldn't explain this code.",
            "explanation": "Please try again.",
            "line_by_line": [],
            "output": "",
            "concept": ""
        }


if __name__ == "__main__":

    test_code = """name = "Asha"
print("Hello " + nme)"""

    test_error = "NameError: name 'nme' is not defined"

    print(
        json.dumps(
            analyze_error(
                test_code,
                test_error,
                mode="fix"
            ),
            indent=2
        )
    )