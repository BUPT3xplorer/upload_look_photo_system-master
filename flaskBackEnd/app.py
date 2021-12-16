import os
import sys
import flask
from datetime import timedelta
# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from keras.applications.resnet import ResNet50

# Some utilites
import numpy as np
from util import base64_to_pil
from my_spider import spider_fun
# about os_file
import os



# Declare a flask app
app = Flask(__name__)
app.send_file_max_age_default = timedelta(seconds=1)

# You can use pretrained model from Keras
# Check https://keras.io/applications/

from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
model = MobileNetV2(weights='imagenet')
# model = keras.models.load_model("models/my_transfer_learning")
# model = ResNet50(weights = 'imagenet')

print('Model loaded. Check http://127.0.0.1:5000/')


# Model saved with Keras model.save()
# MODEL_PATH = 'models/your_model.h5'

# Load your own trained model
# model = load_model(MODEL_PATH)
# model._make_predict_function()          # Necessary
# print('Model loaded. Start serving...')


def model_predict(img, model):
    # img = img.resize((180, 180))
    # img.save("image/img.jpg")
    # img = keras.preprocessing.image.load_img("image/img.jpg", target_size=(180, 180))
    img = img.resize((224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = tf.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='tf')

    preds = model.predict(x)
    return preds

    # regard and update the total num of pics and save 
def pic_save(img,result):
    with open("global_total.txt",'r') as f:
        s_temp=f.read()
    #pic_dir="./uploads/"+result
    pic_dir="/var/www/html/photo/pic_find/"+result
    if(not os.path.exists(pic_dir)):
        os.mkdir(pic_dir)
    
    pic_path=pic_dir+"/"+s_temp.replace('/n','')+'.png'
    img.save(pic_path)

    with open("global_total.txt",'w') as f:
        f.write(str(int(s_temp)+1))



# def prepare_image(image, target):
# 	# if the image mode is not RGB, convert it
# 	if image.mode != "RGB":
# 		image = image.convert("RGB")

# 	# resize the input image and preprocess it
# 	image = image.resize(target)
# 	image = img_to_array(image)
# 	image = np.expand_dims(image, axis=0)
# 	image = imagenet_utils.preprocess_input(image)

# 	# return the processed image
# 	return image


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index1.html')
@app.route('/pachong',methods=['GET','POST'])
def index2():
    #Spider page
    if request.method=='POST':
        print("有POST请求输入")
        key_word=request.form.get('key')
        print("\n有参数传入"+key_word)
        spider_fun(key_word)
        
    #爬取图片爬虫
    return render_template('my_spider_wait.html')
'''
图片查询模块已整合
@app.route('/pic_search',methods=['GET','POST'])
def pic_select():
    print(request)
    return redirect('http://localhost',code=301)
'''



@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        img = base64_to_pil(request.json)

        # Save the image to ./uploads
        # img.save("./uploads/image.png")
        # Make prediction
        preds = model_predict(img, model)

        # Process your result for human
        pred_proba = "{:.3f}".format(np.amax(preds))    # Max probability
        pred_class = decode_predictions(preds, top=1)   # ImageNet Decode

        result = str(pred_class[0][0][1])               # Convert to string
        result = result.replace('_', ' ').capitalize()
        pic_save(img,result)

        # Serialize the result, you can add additional fields
        with open("./test.txt",'a+') as f:
            f.write("0")
        return jsonify(result=result, probability=pred_proba)
        # # Get the image from post request
        # img = base64_to_pil(request.json)

        # # Save the image to ./uploads
        # # img.save("./uploads/image.png")
        # # Make prediction
        # preds = model_predict(img, model)
        # templete = {'0' : 'Butterfly', '1' : 'Cat', '2' : 'Chicken', '3' : 'Cow', '4' : 'Dog',
        #     '5' : 'Elephant', '6' : 'Horse', '7' : 'Sheep', '8' : 'Spider', '9' : 'Squirrel'}


        # # Process your result for human
        # data = {}
        # prob = preds[0]
        # print(prob)
        # for i in range(10):
        #     data[templete[str(i)]] = '{:.1f}'.format(prob[i] * 100) + '%'

        # data = sorted(data.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
        # result = str(data[0][0]) # Convert to string
        # print(data)
        # result = result.replace('_', ' ').capitalize()
        # proba = data[0][1]
        # pic_save(img,result)

        # # Serialize the result, you can add additional fields
        # with open("./test.txt",'a+') as f:
        #     f.write("0")
        # return jsonify(result=result, probability=proba)
        

    return render_template('index1.html')

	# initialize the data dictionary that will be returned from the
	# view
	# data = {"success": False}


	# # ensure an image was properly uploaded to our endpoint
	# if flask.request.method == "POST":
	# 	# if flask.request.files.get("image"):
	# 		# read the image in PIL format
	# 		image = flask.request.files["image"].read()
	# 		image = Image.open(io.BytesIO(image))

	# 		# preprocess the image and prepare it for classification
	# 		image = prepare_image(image, target=(224, 224))

	# 		# classify the input image and then initialize the list
	# 		# of predictions to return to the client
	# 		preds = model.predict(image)
	# 		results = imagenet_utils.decode_predictions(preds)
	# 		data["predictions"] = []

	# 		# loop over the results and add them to the list of
	# 		# returned predictions
	# 		for (imagenetID, label, prob) in results[0]:
	# 			r = {"label": label, "probability": float(prob)}
	# 			data["predictions"].append(r)

	# 		# indicate that the request was a success
	# 		data["success"] = True
			


	# # return the data dictionary as a JSON response
    
	# return flask.jsonify(data)



if __name__ == '__main__':
    # app.run(port=5002, threaded=False)
    app.run(host='0.0.0.0',port=5000,debug=True)
    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
