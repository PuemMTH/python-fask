from flask import Flask, jsonify, request, render_template, redirect, url_for
# import {flask, jsonify, request} from 'flask'
import requests
import json
import pymysql
import os


# app = flask.Flask(__name__)
app = Flask(__name__)

connect = pymysql.connect(host="localhost", user="puemmth", passwd="mysql@xT54rNDN!", db="puem_store")

# color
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# end color

# working with database
class worning:
    DATABASE_ERROR = bcolors.FAIL + "Database error!" + bcolors.ENDC
    DATABASE_CONNECT_ERROR = bcolors.FAIL + "Database connect error!" + bcolors.ENDC
    DATABASE_CONNECT_SUCCESS = bcolors.OKGREEN + "Database connect success!" + bcolors.ENDC
    NO_DATA = bcolors.FAIL + "No data!" + bcolors.ENDC
    NO_DATA_IN_DB = bcolors.FAIL + "No data in database!" + bcolors.ENDC
    NO_DATA_IN_API = bcolors.FAIL + "No data in API!" + bcolors.ENDC
    NO_DATA_IN_API_DB = bcolors.FAIL + "No data in API and database!" + bcolors.ENDC
# end working tags

os.system('CLS')

with connect:
    with connect.cursor() as cursor:
        print(worning.DATABASE_CONNECT_SUCCESS)
        subreq = "/api/v1"

        @app.route(f"{subreq}/get", methods=["GET"])
        def all_inbase():
            cursor.execute("SELECT * FROM web_storeage")
            result = cursor.fetchall()
            if result:
                convertToArray = {}
                for i in result:
                    convertToArray[i[0]] = i[1]

            return jsonify(convertToArray) , 200, {"Content-Type": "application/json"}

        @app.errorhandler(404)
        def page_not_found(e):
            return {"error": "Page not found"}, 404

        app.run(host="localhost", port=5000, debug=True)