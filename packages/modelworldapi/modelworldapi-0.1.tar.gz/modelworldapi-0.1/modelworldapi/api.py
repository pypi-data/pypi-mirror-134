import requests
import ast
import base64

class OjasDetector:
    """
    Class: OjasDetector
    The Official API for ModelWorld
    Usually you create a class and pass the required variables like this:
    detector = OjasDetector(data_url = data_url, api = api_key, conf = custom_confidence_level)
    :param url: (Not required): It is the URL of request
    :param data_url: (required): The URL of the image stored on a web server
    :param api: (required): The 32 bit long API key that you get from registering it on the website
    :param conf: (not required): Default is 0.7. The amount of confidence that model has on its prediction. If given less, can detect more objects, but may give poor results too.
    """

    def __init__(self, data_url=None, api=None, conf=0.7, url="https://modelworld.herokuapp.com/"):
        self.URL = url
        self.API = api
        self.CONF = conf
        f = open(data_url, "rb")
        da = f.read()
        f.close()
        self.DATA_URL = base64.urlsafe_b64encode(da)
        self.RESULT = None
        del f
        del da

    def detect(self):
        if self.DATA_URL is not None and self.API is not None:
            data_dict ={"data": str(self.DATA_URL),"conf": str(self.CONF), "api": str(self.API)}
            r = requests.post(self.URL + "detect", json=data_dict)
            r = r.content
            r = r.decode()
            try:
                r = ast.literal_eval(r)
            except:
                raise TypeError("There is some error either in the server or in your code. Please recheck the code and try agin")
            self.RESULT = r
            del r
            return self.RESULT
        else:
            raise Exception('''DATA AND API ERROR: 
Either no Data or no API key is found''')
    def save(self, fname="image.jpg"):
        if self.RESULT is not None:
            res =self.RESULT
            byte = ast.literal_eval(res.get("image_bytes"))
            f = open(fname, "wb")
            f.write(byte)
            f.close()
            del f
            del res
            del byte
        else:
            raise NotImplementedError("No Data to work on. Maybe you forgot to call the '.detect()'")
if __name__=="__main__":
    """
    :::Example:::
    """
    detector = OjasDetector(data_url="YOUR IMAGE FILE PATH", api="YOUR API KEY YOU GET FROM MODELWORLD", conf="AMOUNT OF CONFIDENCE THE MODEL HAVE IN FLOAT")
    detector.detect() # Returns A Dictionary Object containing "rendered_result","image_array", "image_bytes", "time_taken" as a string.
    #You are advised to use ast.literaleval() to convert the datatype of the values of dictionary for further use
    detector.save("IMAGE NAME.jpg") # Without running detect() would result in error
