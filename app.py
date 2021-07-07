from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "Secret Key"


#This is the index route where we are going to query on all our todo list
@app.route('/')
def Index():
    # all_data = Data.query.all()

    return render_template("index.html", employees = "hello")
   



#this route is for inserting data to mongodb via html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        flash("Task Inserted Successfully")

        return redirect(url_for('Index'))


#this is our update route where we are going to update todo list
@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
    
        flash("Task Updated Successfully")

        return redirect(url_for('Index'))




#This route is for deleting task
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):

    flash("Task Deleted Successfully")

    return redirect(url_for('Index'))






if __name__ == "__main__":
    app.run(debug=True)