from flask import Flask,redirect,render_template,url_for,request
import cv2
import numpy as np
import os
import glob
import time
from werkzeug.utils import secure_filename
s='static/images/'

app=Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def home():
    l = glob.glob('static/images/*')
    l=len(l)
    if request.method == 'POST':
        f = request.files['file']
        l = l+1
        f.save(s+secure_filename(str(l)+'.jpg'))
        print(s+str(l)+'.jpg')
        time.sleep(0.5)
        return redirect('/pred2')
    #print(img)
    t=l+1
    return render_template('index1.html',i=1,l1=t)
@app.route('/<name>')
def pred(name):
    c=s+name+'.jpg'
    print(c)
    img = cv2.imread(c,0)
    img = np.array(img)
    img=img/255
    #img = img.reshape(img.shape[0],img.shape[1],1)
    #img=np.array([img,img])
    img = img.reshape(1,img.shape[0],img.shape[1],1)
    img = np.array(img).tolist()
    return render_template('index.html',im=img,s=c)
@app.route('/pred2')
def pred3():
    l = glob.glob('static/images/*')
    l=len(l)
    c=s+str(l)+'.jpg'
    print(c)
    img = cv2.imread(c,0)
    img = np.array(img)
    img=img/255
    #img = img.reshape(img.shape[0],img.shape[1],1)
    #img=np.array([img,img])
    img = img.reshape(1,img.shape[0],img.shape[1],1)
    img = np.array(img).tolist()
    return render_template('index.html',im=img,s=c)
if __name__=='__main__':
    app.run(debug=True)
