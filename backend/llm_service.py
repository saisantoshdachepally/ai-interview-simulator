from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)


def generate_question(role: str, difficulty: str):
    prompt = f"""
    Generate ONE unique and new {difficulty} level interview question
    for a {role} position.
    Do not repeat common generic questions.
    """

    chat = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=GROQ_MODEL,
        temperature=0.9  # high creativity
    )

    return chat.choices[0].message.content.strip()


def evaluate_answer(question: str, answer: str):
    prompt = f"""
    You are an expert technical interviewer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Give:
    - Score out of 10
    - Strengths
    - Weaknesses
    - Suggestions to improve
    """

    chat = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model=GROQ_MODEL,
        temperature=0.3
    )

    return chat.choices[0].message.content.strip()
