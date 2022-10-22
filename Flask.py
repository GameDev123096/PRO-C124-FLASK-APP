from ast import JoinedStr
from crypt import methods
from re import U
from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [{
    'id' : 1,
    'title' : u'Buy groceries',
    'discription' : u'Milk, Cheese, Pizza, Fruit, Tylenol',
    'done' : False
},
{   'id' : 2,
    'title' : u'Learn Python',
    'discription' : u'Need to find a good Python tutorial on the web',
    'done' : False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status" : "error",
            "message" : "Please provide the data!"
        },400)

task = {
    'id' : tasks[-1]['id'] + 1,
    'title' : request.json['title'],
    'discription' : request.json.get('discription', ""),
    'done' : False
}

tasks.append(task)
    return jsonify({
    "status" : "success",
    "message": "Task added succesfully"
})

@app.route("/get-data")
def get_task():
    return JoinedStr({
        "data" : tasks
    })
    
    if(__name__=="__main__"):
        app.run(debug=True)
