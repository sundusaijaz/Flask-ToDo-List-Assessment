from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "Secret Key"


client =  MongoClient('mongodb+srv://sundus-test:test@cluster0.0wyke.mongodb.net/test?retryWrites=true&w=majority')
db = client['test']


#This is the index route where we are going to query on all our todo list
@app.route('/')
def Index():
    print("********Fetching all data*********")

    all_data = db.test.find()

    print(all_data)

    return render_template("index.html", tasks = all_data)
   



#this route is for inserting data to mongodb via html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        id = request.form['id']
        task = request.form['task']
        group = request.form['group']
        priority = request.form['priority']

        todo_list = db.test

        print("********Inserting Data**********")

        record = dict()
        record['id'] = id
        record['task'] = task
        record['group'] = group
        record['priority'] = priority

        db.test.insert_one(record)
        
        print("***********Record inserted***********")

        flash("Task Inserted Successfully")

        return redirect(url_for('Index'))


#this is our update route where we are going to update todo list
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':

        id = request.form.get('id')

        priority=request.form['priority']
        
        db.test.find_one_and_update({"id":id},
            {"$set":{
                "priority" : priority
            }}
        )
    
        flash("Task Updated Successfully")

        return redirect(url_for('Index'))




#This route is for deleting task
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):

    db.test.find_one_and_delete({"id":id})

    flash("Task Deleted Successfully")

    return redirect(url_for('Index'))






if __name__ == "__main__":
    app.run(debug=True)