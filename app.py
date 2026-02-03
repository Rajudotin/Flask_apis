from flask import Flask ,jsonify ,request
app=Flask(__name__)

students=[
    {"id":1,"name":"Raju","age":22},
    {"id":2,"name":"Sai","age":19},
]

@app.route("/",methods=["GET"])

def home():
    return "Flask APIs Calls"


@app.route("/students",methods=["GET"])
def all_students():
    return jsonify(students)

@app.route("/students/<int:id>",methods=["GET"])
def id_students(id):
    student = next((s for s in students if s["id"]==id),None)
    if not student:
        return {"message":"id not found"} ,404
    else:
        return (student)
    
@app.route("/students",methods=["POST"])
def add_students():
    data=request.get_json()
    if not data or "id" not in data:
        return jsonify({"message":"invalid data"}),400
    if any(s["id"]==data["id"] for s in students):
        return jsonify({"message":"already exists"}),400
    students.append(data)
    return {"message":"student is added", "student":data}
    
@app.route("/students/<int:id>",methods=["PUT"])
def update_students(id):
    student=next((s for s in students if s["id"]==id),None)
    if not students:
        return jsonify({"message":"id not exists"}) ,404
    data=request.get_json()
    students[id-1]["name"]=data["name"]
    return jsonify({"message":"updated succesfull","students":students[id-1]}) ,200

    
@app.route("/students/<int:id>",methods=["DELETE"])
def delete_students():
    return

if __name__=="__main__":
    app.run(debug=True)
    