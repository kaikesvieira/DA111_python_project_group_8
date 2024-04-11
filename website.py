from flask import Flask, render_template #create a server on your laptop
import pathlib
import sqlite3

base_path = pathlib.Path('DA111_python_project_group_8')
db_name = "Trees.db"
db_path = base_path / db_name
print(db_path)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    con = sqlite3.connect('Trees.db')
    cursor = con.cursor()
    trees = cursor.execute("SELECT * FROM trees").fetchall()
    con.close()

    return render_template("data_table.html", trees = trees)

if __name__=="__main__":
    app.run(debug=True)