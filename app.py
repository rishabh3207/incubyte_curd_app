from flask import Flask,render_template,request,redirect,flash
from model import db, Words

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///words.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

@app.route('/' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        words = Words.query.all()
        return render_template('home.html',words = words)
 
    if request.method == 'POST':
        word = request.form['word']
        word_data = Words.query.filter_by(word=word).first()
        if word_data:
            message = 'Word Already Exists'
            words = Words.query.all()
            return render_template('home.html',words = words, message=message)
        elif word == "":
            message = 'Enter Valid word'
            words = Words.query.all()
            return render_template('home.html',words = words, message=message)
        else:
            word_data = Words(word=word)
            db.session.add(word_data)
            db.session.commit()
            message = 'Added Word Successfully'
            words = Words.query.all()
            return render_template('home.html',words = words, message=message)


@app.route('/update' , methods = ['GET','POST'])
def update():
    if request.method == 'GET':
        return render_template('update.html')
 
    if request.method == 'POST':
        word1 = request.form['word1']
        word2 = request.form['word2']
        word_data = Words.query.filter_by(word=word1).first()
        word2_data = Words.query.filter_by(word=word2).first()
        if word2_data:
            message = 'Word2 already exists'
            words = Words.query.all()
            return render_template('home.html',words = words, message=message)
        elif word_data:
            db.session.delete(word_data)
            db.session.commit()
            word_data = Words(word=word2)
            db.session.add(word_data)
            db.session.commit()
            message = 'Updated Word Successfully'
            words = Words.query.all()
            return render_template('home.html',words = words, message=message)
        elif word1 == "":
            message = 'Enter Valid word'
            words = Words.query.all()
            return render_template('home.html',words = words, message=message)
        else:
            message = 'Word does not exist!!'
            words = Words.query.all()
            return render_template('home.html',words = words, message=message)

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        word = request.form['word']
        word_data = Words.query.filter_by(word=word).first()
        if word_data:
            db.session.delete(word_data)
            db.session.commit()
            message = 'Deleted Word Successfully'
            words = Words.query.all()
            return render_template('home.html',words = words, message=message)
        else:
            message = 'Word does not exist!!'
            words = Words.query.all()
            return render_template('home.html',words = words, message=message)

app.run(host='localhost', port=5000)
