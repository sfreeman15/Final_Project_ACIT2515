import json

class User:
    def __init__(self,filename):
        self.filename = filename
        
        self.users = []
        self.scores = []
        self.load_from_json()
        self.myList = []
        self.dict_users = {}
        self.player = ""
        # self.get_user()

    def load_from_json(self):
        with open(self.filename, "r") as fp:
            data = json.load(fp)
        for score in data.values():
            score.sort(reverse=True)
        self.users = sorted(data.items(), key=lambda x: x[1], reverse=True)
        
        
    
        # for user in data.keys():
        #     self.users.append(user)

        for scores in data.values():
            self.scores.append(max(scores))

    def get_user(self,user):
        yes = 0
        for player in self.users:
            if player in self.users[yes][0]:
                return player
            yes += 1
        return None