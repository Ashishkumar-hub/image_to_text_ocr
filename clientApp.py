from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from ai_utils.utils import decodeImage
from wsgiref import simple_server
from predict import ocr

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        #modelPath = 'research/ssd_mobilenet_v1_coco_2017_11_17'
        self.objectDetection = ocr(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.objectDetection.getPrediction()
    return jsonify([result])

'''if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='127.0.0.1', port=8000, debug=True)
'''
if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    #port = int(os.getenv("PORT",6000))
    clApp = ClientApp()
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host,port=port, app=app)
    httpd.serve_forever()
