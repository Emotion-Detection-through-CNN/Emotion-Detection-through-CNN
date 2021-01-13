from flask import Flask,redirect,render_template
import cv2
import numpy as np
import os
s='static/images/'
app=Flask(__name__)
@app.route('/')
def home():
    #print(img)
    return render_template('index1.html',i=1)
@app.route('/<name>')
def pred(name):
    c=s+name+'.jpg'
    print(c)
    img = cv2.imread(c,0)
    img = np.array(img)
    print(np.shape(img))
    #img = img.reshape(img.shape[0],img.shape[1],1)
    #img=np.array([img,img])
    img = img.reshape(1,img.shape[0],img.shape[1],1)
    img = np.array(img).tolist()
    return render_template('index.html',im=img,s=c)
if __name__=='__main__':
    app.run(debug=True)
