from flask import Flask
from flask import request
#from SlavePi import *

app = Flask(__name__)


@app.route("/translate",methods=['POST'])
def translate():
    try:
        data=request.get_json()
        if('text' not in data):
            return buildResponse(400,"invalid request missing text field")
        text=data['text']
        print(text);
        #sendText(text)
        
        #put your translate service here
        return buildResponse(200,"sucess translating text: "+text)
    except Exception as e:
        return buildResponse(500,str(e))

@app.route("/clear",methods=['POST'])
def clear():
    try:
        sendText(" ");
        #put your clear service here
        return buildResponse(200,"sucess")
    except Exception as e:
        return buildResponse(500,str(e))


def buildResponse(code,message):
    return {"code":code,"message":message}

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=8181)