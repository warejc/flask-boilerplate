from pymongo import MongoClient

#put this string in a config file
client = MongoClient('mongodb://adm:admpassword@ds141454.mlab.com:41454/')
db = client.dev_jw #replace test wiht name of acutal db or cluster

class TeamDBC():

    def get_teams(self, team_ids=None):

        teams = db.team.find({})

        for doc in teams:
            pprint(doc)
        import ipdb; from pprint import pprint; ipdb.set_trace();

        return True
