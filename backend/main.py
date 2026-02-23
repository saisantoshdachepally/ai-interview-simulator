from fastapi import FastAPI
from pydantic import BaseModel
from llm_service import generate_question, evaluate_answer

app = FastAPI()


@app.get("/question/{role}")
def get_question(role: str, difficulty: str = "medium"):
    question = generate_question(role, difficulty)
    return {"question": question}


class AnswerRequest(BaseModel):
    question: str
    answer: str


@app.post("/evaluate")
def evaluate(data: AnswerRequest):
    result = evaluate_answer(data.question, data.answer)
    return {"evaluation": result}
