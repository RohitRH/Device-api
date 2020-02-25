from flask import Flask,request
from flask_restful import Api,Resource
from user_agents import parse


app = Flask(__name__)
api = Api(app)


class Device(Resource):
    def get(self):
        try:
            string = request.user_agent.string
            ustring = parse(string)
            data={
                "OS": ustring.os.family,
                "OS version": ustring.os.version_string,
                "browser": ustring.browser.family,
                "string": string,
                "mobile": ustring.is_mobile,
                "Tablet": ustring.is_tablet,
                "PC": ustring.is_pc,
                "touch available": ustring.is_touch_capable
            }
            return data
        except KeyError as e:
            print("key error "+str(e))
            return {'error':True},400


api.add_resource(Device,'/device')

