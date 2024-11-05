# decorator app.route() , used for url mapping
from flask import Flask, render_template,request,redirect, url_for
# initialize app as flask app
app = Flask(__name__)
# list of dictionaries to represent records
# sample data
tasks = [
    {'id': 1, 'title': "Buy Groceries", 'description': "Milk, Bread, Flour, Sugar"} ,
    {'id': 2, 'title': "Study", 'description': "Review Python Flask!"}
]
## routes
## landing route
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)
@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        # get a new id for our new task item
        new_id = len(tasks) + 1
#         pick items from the form
        title = request.form['title']
        description = request.form['description']
#         add my new record to the list of task dictionaries
        tasks.append({'id' : new_id, 'title': title, 'description': description})
        # redirect after a new addition
        return redirect(url_for('index'))
@app.route('/delete/<int:id>')
def delete(id):
#     to access a global variable that wont be overriden : global : keyword that maintains the values of the
#     global scoped variable even on reassignment
    global tasks
#     to filter the list and remove the item whose id has been searched
#     for task in tasks:
#         if task['id'] == id:
#             tasks.remove(task)
#     return tasks
    # LIST COMPREHENSION : loop iterables and they will return the end value as a list
    tasks = [task for task in tasks if task['id'] != id]
    return redirect(url_for('index'))
@app.route('/edit/<int:id>', methods=["GET","POST"])
def edit(id):
    task = next((task for task in tasks if task['id'] == id), None)
    print(task)
    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
