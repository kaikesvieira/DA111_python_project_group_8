from flask import Flask, render_template #create a server on your laptop
import pathlib
import sqlite3

base_path = pathlib.Path(r'C:\Users\defaultuser0\OneDrive\Documents\GitHub\DA111_python_project_group_8\Database')
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
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    trees = cursor.execute("SELECT *, AVG(DBH) AS avg_dbh FROM trees GROUP BY Species ORDER BY avg_dbh DESC LIMIT 20").fetchall()
    trees_sorted = sorted(trees, key=lambda x: x[4], reverse=True)
    con.close()

    return render_template("data_table.html", trees = trees_sorted)

if __name__=="__main__":
    app.run(debug=True)