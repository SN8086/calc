from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
tasks = []

HTML = """
<!doctype html>
<title>To-Do List</title>
<h1>My To-Do List</h1>
<form method="post" action="/add">
    <input type="text" name="task" required>
    <input type="submit" value="Add">
</form>
<ul>
    {% for task in tasks %}
    <li>{{ task }}</li>
    {% endfor %}
</ul>
"""

@app.route('/')
def index():
    return render_template_string(HTML, tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tasks.append(task)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
