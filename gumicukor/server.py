from flask import *
from json import *
from model import *

app = Flask("gumicukor")


@app.route('/api/', methods=['GET'])
def api():
    if request.method == "GET":
        people_list = Person.get_serialized_persons()
        return jsonify(*people_list)


@app.route('/api/id/<id>', methods=['GET'])
def api_id(id):
    if request.method == "GET":
        pelda = Person.get_person_by_id(id)
        return jsonify(pelda)


@app.route('/api/name/<name>', methods=['GET'])
def api_name(name):
    if request.method == "GET":
        pelda = Person.get_person_by_name(name)
        return jsonify(pelda)


@app.route('/', methods=['GET'])
def root():
    if request.method == "GET":
        return render_template('index.html')


app.run(debug=True)
