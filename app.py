from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista global de tareas (simulando una base de datos)
tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append({"text": task, "done": False})
        return redirect("/")
    return render_template("index.html", tasks=tasks)

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

@app.route("/toggle/<int:index>")
def toggle(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index]["done"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
