from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

@app.route("/")
def hello_world():
    todo = Todo(title="first title", desc="start investing in Stock Market")
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all()
    return render_template("index.html", allTodo=allTodo)
    # return "<p>Hello, World!</p>"

@app.route("/show")
def products():
    allTodo = Todo.query.all()  # for print all tables in databse
    print(allTodo)
    return "<p>this is an products page</p>"

if __name__ == "__main__":
    app.run(debug=True)