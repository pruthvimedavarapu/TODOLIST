from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect(url_for('view_tasks'))
    return render_template('add_task.html')

@app.route('/view')
def view_tasks():
    return render_template('view_tasks.html', tasks=tasks)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('view_tasks'))

if __name__ == '__main__':
    app.run(debug=True)

