from flask import Flask, request, render_template, jsonify, session, redirect
import pandas
from io import StringIO
from src.testData import NRCData

APP = Flask(__name__)
APP.secret_key = "secretKey"
Data = dict()

class NRCServer:
    def __init__(self, host: str, port: float):
        self.HOST = host
        self.PORT = port

    def Start(self):
        global APP
        print(self.HOST)
        APP.run(host=self.HOST, port=self.PORT, threaded=True, debug=False)


@APP.route("/", methods=["GET"])
def GetMainPage():
    if request.method == "GET":
        return render_template("MainPage.html")

@APP.route("/config", methods=["POST"])
def ConfigContent():
    global Data
    Data = None
    return render_template("ContentConfigPage.html")

@APP.route("/config/fin", methods=["POST"])
def ConfigFinish():
    global Data
    Data = dict()
    user_id = request.form["patient_id"] if request.form["patient_id"] is not None else ""
    user_stride = request.form["patient_stride"] if request.form["patient_stride"] is not None else ""
    user_width = request.form["patient_width"] if request.form["patient_width"] is not None else ""
    overlapping_area = request.form["overlapping_area"] if request.form["overlapping_area"] is not None else ""
    user_footsize = request.form["foot_size"] if request.form["foot_size"] is not None else ""
    content_check = request.form.get("chk_info") if request.form.get("chk_info") is not None else ""
    if user_id == "" or user_stride == "" or user_width == "" or overlapping_area == "" or user_footsize == "":
        return "입력을 제대로 하시지 않으셨습니다"
    else:
        print("user_id: " + user_id)
        print("user_stride: " + user_stride)
        print("user_width: " + user_width)
        print("overlapping_area: " + overlapping_area)
        print("user_footsize: " + user_footsize)
        print("content_check: " + content_check)
        Data = {
            "type" : content_check,
            "id" : user_id,
            "stride" : user_stride,
            "width" : user_width,
            "area" : overlapping_area,
            "size" : user_footsize
        }
        return redirect("/")

@APP.route("/reset", methods=["POST"])
def ResetContent():
    global Data
    Data = None
    return redirect("/")

@APP.route("/content/information", methods=["POST"])
def GetContentInformation():
    global Data
    if Data is None:
        return "None"
    else:
        return jsonify(Data)

@APP.route("/content/finish", methods=["POST"])
def SaveResult():
    global Data
    try:
        request.form
        csv_txt = request.form["data"] if request.form["data"] is not None else ""
        csv_binary = StringIO(csv_txt)
        csv_data = pandas.read_csv(csv_binary)
        Data = None
        print(csv_data)
        return "True"
    except Exception as e:
        print(str(e))
        return "False"

