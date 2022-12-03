import json

class User:
    """
    A class for retrieving data from the json files and adding the data to the Flask API. 
    Attributes:
        -----------
        filename(str): 
            Name of the json file
    """
    def __init__(self,filename):
        '''
        Constructs the necessary attributes for the User class
        '''
        self.filename = filename
        self.users = []
        self.scores = []
        self.load_from_json()
        self.myList = []
        self.dict_users = {}
        self.player = ""

    def load_from_json(self):
        """
        Loads data from file, sorts the key's values from biggest to smallest number. Afterwards, it turns the dictionary into a list sorted by the key with the highest first value. Appends the highest value of each key into the scores list."""
        with open(self.filename, "r") as fp:
            data = json.load(fp)
        for score in data.values():
            score.sort(reverse=True)
        self.users = sorted(data.items(), key=lambda x: x[1], reverse=True)
        
        for scores in data.values():
            self.scores.append(max(scores))

    