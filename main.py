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
@app.put("/update/{id}")
def update_note(id: int, note: str):
    notes[id]=note
    return {
        "message": "Note update successfully",
        "note": notes[id]
    }
@app.delete("/delete/{id}")
def delete_note(id: int):
    note = notes.pop(id)
    return { 
        "message": "Note deleted successfully",
        "note": note
    }