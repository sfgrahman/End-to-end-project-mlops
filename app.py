from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    logging.info("Testing logging method in the pipelines")
    return "welcome to machine learning end to end project pipeline-Explore MLOPs"

if __name__=="__main__":
    app.run(debug=True)