from flask import Flask, jsonify,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField

app = Flask(__name__)

app.config['SECRET_KEY'] ='mysecretkey'

class InfoForm(FlaskForm):
    
    breed = StringField("What Breed are you? ")
    submit = SubmitField("Submit")

@app.route('/hello',methods=['GET','POST'])
def index():

    breed = False
    times_ten = False
    form = InfoForm()

    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ''

    return render_template('index_form.html',form=form,breed=breed)

if __name__ == '__main__':
    app.run(debug=True)