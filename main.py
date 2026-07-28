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
@app.get("/get/{id}")
def get_note(id: int):
    return notes[id]