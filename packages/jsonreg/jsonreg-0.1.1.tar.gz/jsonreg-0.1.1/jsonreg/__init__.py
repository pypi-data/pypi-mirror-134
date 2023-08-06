def read(key):
    import json

    with open(key) as f:
        data = json.load(f)
    return data["data"],data["id"],data["name"]
def write(key,regdata):
    import json

    with open(key) as f:
        data = json.load(f)
    data["data"] = regdata
    with open(key, 'w') as outfile:
        json.dump(data, outfile)
def create(key,name,regdata):
    import json
    import random
    data = {}
    data["name"] = name
    data["id"] = random.randint(100000000000,999999999999)
    data["data"] = regdata
    with open(key, 'w') as outfile:
        json.dump(data, outfile)
    return data["id"]
class find:
    def name(location,name):
        import json
        import os
        keys = []
        dir_list = os.listdir(location)
        for i in dir_list:
            if i.endswith(".json"):
                if location.endswith("/"):
                    i = location+i
                else:
                    i = location+"/"+i
                with open(i) as f:
                    data = json.load(f)
                if data["name"] == name:
                    keys.append(i)
        return keys
    def id(location,id):
        import json
        import os
        keys = []
        dir_list = os.listdir(location)
        for i in dir_list:
            if i.endswith(".json"):
                if location.endswith("/"):
                    i = location+i
                else:
                    i = location+"/"+i
                with open(i) as f:
                    data = json.load(f)
                if data["id"] == id:
                    keys.append(i)
        return keys