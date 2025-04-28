from fastapi import FastAPI
from pydantic import BaseModel
from database import get_database_connection

app = FastAPI()

class User(BaseModel):
    name: str
    Age: int
    email: str

@app.post("/students")
async def add_student(user: User):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Studentss (name, Age, email) VALUES (%s, %s, %s)"
    values = (user.name, user.Age, user.email)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": "User created successfully"}

@app.get("/students")
async def get_all_students():
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Studentss"
    cursor.execute(query)
    students = cursor.fetchall()
    connection.close()
    return students

@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "DELETE FROM Studentss WHERE id = %s"
    cursor.execute(query, (student_id,))
    connection.commit()
    connection.close()
    return {"message": f"User with ID {student_id} deleted successfully"}

@app.put("/students/{student_id}")
async def update_student(student_id: int, user: User):
    connection = get_database_connection()
    cursor = connection.cursor()
    query = "UPDATE Studentss SET name = %s, Age = %s, email = %s WHERE id = %s"
    values = (user.name, user.Age, user.email, student_id)
    cursor.execute(query, values)
    connection.commit()
    connection.close()
    return {"message": f"User with ID {student_id} updated successfully"}
