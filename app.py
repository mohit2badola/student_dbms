from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mohit@9684",
        database="student_dbms"
    )
    return connection


@app.route("/")
def home():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", students=students)
@app.route("/add", methods=["POST"])
def add_student():

    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]
    semester = request.form["semester"]

    connection = get_db_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO students (name, email, course, semester)
        VALUES (%s, %s, %s, %s)
    """

    values = (name, email, course, semester)

    cursor.execute(sql, values)
    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")
@app.route("/edit/<int:student_id>")
def edit_student(student_id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM students WHERE student_id = %s",
        (student_id,)
    )

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template("edit.html", student=student)
@app.route("/update/<int:student_id>", methods=["POST"])
def update_student(student_id):

    name = request.form["name"]
    email = request.form["email"]
    course = request.form["course"]
    semester = request.form["semester"]

    connection = get_db_connection()
    cursor = connection.cursor()

    sql = """
        UPDATE students
        SET name = %s,
            email = %s,
            course = %s,
            semester = %s
        WHERE student_id = %s
    """

    values = (
        name,
        email,
        course,
        semester,
        student_id
    )

    cursor.execute(sql, values)

    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")
@app.route("/delete/<int:student_id>")
def delete_student(student_id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = %s",
        (student_id,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)