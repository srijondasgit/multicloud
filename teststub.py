import json

class stubs:

    def aws_teststub(self):
        with open('dict1') as f:
            data = f.read()
        js = json.loads(data)
        return js
