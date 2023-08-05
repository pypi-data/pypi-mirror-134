from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
from transactions_scraper import Bball_Scraper


app = Flask(__name__)
api = Api(app)

class Transactions(Resource):
    def __init__(self):

        #Initialize webscrapper class
        self.b = Bball_Scraper()

    def get(self):
        parser = reqparse.RequestParser()
        
        #Initialize user arguments
        parser.add_argument('team', required=True)  # add args
        parser.add_argument('start', required=True)
        parser.add_argument('end', required=False)

        #Parse args to dictionary 
        args = parser.parse_args()
        
        if args['team'] not in self.b.nba_teams:
            return 'Team Not Found', 404

        try:
            result = self.b.run(**args) #Runs Scraper
        except AttributeError:
            return 'Bad Request', 400

        return result.to_dict('records'), 200


    def post(sel):
        pass

    def put(self):
        pass

api.add_resource(Transactions, '/')  # added endpoint

if __name__ == '__main__':
    app.run()