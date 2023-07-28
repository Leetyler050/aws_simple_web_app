from flask import Flask, jsonify,render_template

app = Flask(__name__)

@app.route('/hello')
# def hello():
#     return jsonify(message='Hello from Flask on AWS Lambda!')

def index():
    #return '<h1> Hello Puppy!</h1>'
    return render_template('basic.html')

if __name__ == '__main__':
    app.run(debug=True)


# import pandas as pd
# import json
# import plotly
# import plotly.express as px


# @app.route('/report')
# def notdash():
#    df = pd.DataFrame({
#       'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 
#       'Bananas'],
#       'Amount': [4, 1, 2, 2, 4, 5],
#       'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
#    })
#    fig = px.bar(df, x='Fruit', y='Amount', color='City', 
#       barmode='group')
#    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#    return render_template('notdash.html', graphJSON=graphJSON)