from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Message {self.name}>"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    if not name or not message:
        flash('Please enter your name and message.', 'error')
        return redirect('/')

    new_message = Message(name=name, message=message)
    db.session.add(new_message)
    db.session.commit()

    flash('Thank you for your submission!', 'success')
    return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
