from flask import Flask

# flask is class

app = Flask(__name__) # building a flask app object using __init__()

@app.post('/hello') # if any user sent get req to /hellp resource run this
def gett_hello(): # the return of this func will be the response
    return 'world !'

app.run() # run the app
