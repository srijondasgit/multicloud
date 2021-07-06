import json

class stubs:

    def aws_teststub(self):
        with open('dict1') as f:
            data = f.read()
        js = json.loads(data)
        return js

    def aws_getIpstub(self):
        return ['192.168.32.64', '192.168.32.65', '192.168.32.66']
