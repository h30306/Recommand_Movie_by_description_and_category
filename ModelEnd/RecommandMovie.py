import flask
from flask import request
from Model.model_predict.py import predict_vector


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False


@app.route('/RecommandWebsite', methods=['POST'])
def run():
    print('start')
    if request.method == 'POST':
        data = request.values
    demo = predict_vector(data['sentence'], data['dlm'])
    return demo

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
