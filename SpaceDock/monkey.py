import requests
import json

class GbMod():
    def __init__(self, id, name, description, screenshots, render, file_path):
        self.id = id
        self.name = name
        self.description = description
        self.screenshots = screenshots
        self.render = render
        self.file_path = file_path
        pass
    @staticmethod
    def load_from_url(url):
        url_split = url.split("/")
        try:
            mod_id = url_split[-1]
            mod_type = url_split[-2]
            mod_type = mod_type[:-1]
            mod_type = mod_type.title()
        except:
            raise(Exception("Malformed gamebanana URL"))
        return GbMod.load(mod_id, mod_type)
    @staticmethod
    def load(mod_id, mod_type):
        mod = None
        request = requests.post("http://gamebanana.com/api?request=" + mod_type + "." + mod_id + ".[\"name\", \"text\", \"screenshots\", \"file\"]")
        #checkity checks
        if request.status_code == 200:
            if "sError" in request.text:
                if not "Unrecognized ItemType" in request.text and not "doesn't exist" in request.text:
                    raise Exception(request.text)
            else:
                #Gamebanana's shitty JSON encoding breaks so many standards I don't even know where to start
                request_render = requests.post("http://gamebanana.com/api?request=" + mod_type + "." + mod_id + ".[\"render\"]")
                render = None
                if request.status_code == 200:
                    if not "sError" in request.text:
                        result2 = json.loads(request.text, strict=False)
                        render = result2[0]
                result = json.loads(request.text, strict=False)
                result = result[0]
                name = result[0]
                text = result[1]
                screenshots = result[2].split('&&')
                file_path = result[3]
                mod = GbMod(mod_id, name, text, screenshots, render, file_path)
        return mod
