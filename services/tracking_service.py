import pymongo


class TrackingService():
    self.client = pymongo.MongoClient()
    self.db = self.client.tracking
    @classmethod
    def get_tracking_data():
