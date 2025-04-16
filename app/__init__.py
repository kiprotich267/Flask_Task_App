from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']='c2ebfa0eb82b22723909d6a5940fca15ff7533928d69947b92192843be4e1e63'





from app import routes
