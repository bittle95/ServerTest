from flask import Flask, request, render_template, jsonify, session, redirect
from src.testData import NRCData

APP = Flask(__name__)
APP.secret_key = "secretKey"
Data = NRCData()

class NRCServer:
    def __init__(self, host: str, port: float):
        self.HOST = host
        self.PORT = port

    def Start(self):
        global APP
        print(self.HOST)
        APP.run(host=self.HOST, port=self.PORT, threaded=True, debug=False)
@APP.route("/", methods=["GET"])
def test():
    print("test")
    return "test"
@APP.route("/GetWebPage", methods=["GET", "POST"])
def GetWebPage():
    global Data
    if request.method == "GET":
        return render_template("WebPage.html")
    else:
        user_id = request.form["patient_id"] if request.form["patient_id"] is not None else ""
        user_stride = request.form["patient_stride"] if request.form["patient_stride"] is not None else ""
        user_width = request.form["patient_width"] if request.form["patient_width"] is not None else ""
        overlapping_area = request.form["overlapping_area"] if request.form["overlapping_area"] is not None else ""
        user_footsize = request.form["foot_size"] if request.form["foot_size"] is not None else ""
        content_check = request.form.get("chk_info") if request.form.get("chk_info") is not None else ""
        if user_id == "" or user_stride == "" or user_width == "" or overlapping_area == "" or user_footsize == "":
            return "입력을 제대로 하시지 않으셨습니다"
        else:
            Data.id = user_id
            Data.stride = user_stride
            Data.width = user_width
            Data.area = overlapping_area
            Data.size = user_footsize
            Data.content = content_check
            return redirect("/PrintWebPage")

@APP.route("/PrintWebPage", methods=["GET"])
def PrintData():
    global Data
    return str(Data.content)
           #+ Data.id + "\n" + \
           #str(Data.stride) + \
           #"\n" + str(Data.width) + \
           #"\n" + str(Data.area) + \
           #"\n" + str(Data.size) + \
           #"\n" + str(Data.content)