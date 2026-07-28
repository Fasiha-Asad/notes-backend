from fastapi import FastAPI 
app=FastAPI() 
notes=[] 

@app.post("/create")
def create_note(note: str): 
    notes.append(note)
    return {
        "message":"Note created successfully",
        "note":note
    }
@app.get("/getnotes")
def get_notes():
    return notes