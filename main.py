from fastapi import FastAPI 
from pydantic import BaseModel
import sqlite3
app=FastAPI()

conn = sqlite3.connect("notes.db", check_same_thread=False)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Note(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    desc TEXT,
    date TEXT,
    user_id INTEGER
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS User(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")


conn.commit()
class Note(BaseModel):
    title:str
    desc:str
    date:str
    user_id: int


class User(BaseModel):
    name: str
    email: str


class UserId(BaseModel):
    user_id: int


@app.post("/user", status_code=201)
def create_user(user: User):

    cursor.execute(
        "INSERT INTO User(name, email) VALUES (?, ?)",
        (user.name, user.email)
    )

    conn.commit()
    return {
        "message": "User created successfully",
        "id": cursor.lastrowid,
        "name": user.name,
        "email": user.email
    }




   
@app.post("/note", status_code=201)
def create_note(note: Note):

    cursor.execute(
        "INSERT INTO Note(title, desc, date, user_id) VALUES (?, ?, ?, ?)",
        (note.title,
         note.desc, 
         note.date, 
         note.user_id)
    )

    conn.commit()



    return {
        "message": "Note created successfully",
        "id": cursor.lastrowid,
        "title": note.title,
        "desc": note.desc,
        "date": note.date,
        "user_id": note.user_id
    }


@app.post("/notes")
def get_notes(data: UserId):

    cursor.execute(
        "SELECT * FROM Note WHERE user_id = ?",
        (data.user_id,)
    )

    notes = cursor.fetchall()

    return {
        "message": "Notes fetched successfully",
        "notes": [dict(note) for note in notes]
    }
    

@app.get("/note/{id}", status_code=200)
def get_note(id: int):

    cursor.execute(
        "SELECT * FROM Note WHERE id = ?",
        (id,)
    )

    note = cursor.fetchone()

    if note:

        return dict(note)

    return {
        "message": "Note not found"
    }

@app.put("/note/{id}", status_code=200)
def upd_note(id: int, upd_note: Note):

    cursor.execute(
        """
        UPDATE Note
        SET title = ?, desc = ?, date = ?, user_id = ?
        WHERE id = ?
        """,
        (
            upd_note.title,
            upd_note.desc,
            upd_note.date,
            upd_note.user_id,
            id
        )
    )

    conn.commit()

    return {
        "message": "Note updated successfully"
    }

@app.delete("/note/{id}", status_code=200)
def del_note(id: int):

    cursor.execute(
        "DELETE FROM Note WHERE id = ?",
        (id,)
    )

    conn.commit()

    return {
        "message": "Note deleted successfully"
    } 