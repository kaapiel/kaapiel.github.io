from flask import Flask, request
import os

from brain.perfume_brain import PerfumeBrain

app = Flask(__name__)
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/perfumes')
def perfumes():
    return PerfumeBrain().get_all_perfumes()


@app.route('/perfumes/recommendation', methods=['POST'])
def recommendation():
    return PerfumeBrain().get_recommendation(request.get_json(force=True))


@app.route('/notes')
def notes():
    return PerfumeBrain().get_all_notes()


@app.route('/notes/categories')
def notes_categories():
    return PerfumeBrain().get_notes_categories()


@app.route('/notes/<category>')
def notes_by_type(category):
    return PerfumeBrain().get_notes_by_category(category)
