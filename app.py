from flask import Flask 
import os
app=Flask(__name__)

@app.route('/')
def version():
    return {'version':'0.001'}
if __name__=='__main__':
    app.run(port=int(os.getenv('PORT')), host="0.0.0.0")