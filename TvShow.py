import requests
import json

class TvShow:
    """Definition of the class TvShow, it contains the following attributes :
       - id of the tvshow
       - name
       - overview : the description of the tvshow
       - nb_season : number of seasons in the tvshow
       - in_production : if set to True, the tvshow is still in production ; if set to False, it's been over"""
    def __init__(self,id):
        url = "https://api.themoviedb.org/3/tv/" + str(self.id)
        url_content = json.loads(requests.get(url, params={"api_key":"3b8efb3a7bff18de4e8641510c6352a5"}).content.decode())
        self.id = id
        self.name = url_content["name"]
        self.overview = url_content["overview"]
        self.nb_season = url_content["number_of_seasons"]
        self.in_production = url_content["in_production"]

