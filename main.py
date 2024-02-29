
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lesson/<lesson_id>')
def lesson(lesson_id):
    return render_template('lesson.html', lesson_id=lesson_id)

@app.route('/quiz/<quiz_id>')
def quiz(quiz_id):
    return render_template('quiz.html', quiz_id=quiz_id)

@app.route('/quiz-submit', methods=['POST'])
def quiz_submit():
    answers = request.form.getlist('answers')
    # evaluate answers and display result
    return render_template('result.html', answers=answers)

if __name__ == '__main__':
    app.run(debug=True)
