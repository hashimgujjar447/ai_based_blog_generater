from fastapi import FastAPI
from schemas import BlogRequest
from services import generate_blog,ask_question


app=FastAPI()

@app.get("/")
def home():
    return {"message":"AI Blog generator API"}



@app.post("/ask")
def ask(request: BlogRequest):

    answer = ask_question(
        request.prompt
    )

    return {
        "success": True,
        "answer": answer
    }

@app.post("/generate-blog")
def generate(request:BlogRequest):

    if not request.prompt.strip():
        return {"message":"Prompt is required"}
    
    response=generate_blog(request.prompt)

    return {
        "success":True,
        "response":response
    }
    

   
    