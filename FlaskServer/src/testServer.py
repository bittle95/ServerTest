from flask import Flask, request, render_template, jsonify, session, redirect
from src.dataBase_Basic import DataBase

APP = Flask(__name__)
APP.secret_key = "secretKey"
Data = DataBase()

class NRCServer:
    def __init__(self, host: str, port: float):
        self.HOST = host
        self.PORT = port

    def Start(self):
        global APP
        APP.run(host=self.HOST, port=self.PORT, threaded=False)

@APP.route("/GetWebPage", methods=["GET", "POST"])
def GetWebPage():
    global Data
    if request.method == "GET":
        return render_template("WebPage.html")
    else:
        user_id = request.form["id_username"] if request.form["id_username"] is not None else ""
        user_pw = request.form["id_password"] if request.form["id_password"] is not None else ""
        if user_id == "" or user_pw == "":
            return "문자열 반환 예시"
        else:
            Data.userID = user_id
            Data.userPW = user_pw
            return redirect("/PrintWebPage")

@APP.route("/PrintWebPage", methods=["GET"])
def PrintData():
    global Data
    return "POST 반환 예시:\n" + Data.ToString()