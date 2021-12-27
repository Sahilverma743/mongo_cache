from flask import Flask, request, render_template
import pymongo
import urllib 
import sqlite3
from bson.json_util import dumps

# Flask Application
app = Flask(__name__)

# one time initial connection to mongoDB
mongo_connection_url = "mongodb+srv://jija:" + urllib.parse.quote("Mongo@99") + "@cluster0.2mwcj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo_client = pymongo.MongoClient(mongo_connection_url)
mongo_database = mongo_client["sample_airbnb"]

# one time initial connection to mysqlite
mysqlite_client = sqlite3.connect('data_store.db', check_same_thread=False)
# mysqlite_cursor = mysqlite_client.cursor()


@app.route("/")
def base_page():
    return render_template('search.html')


@app.route("/search", methods = ['POST'])
def search_mongo():
    if request.method == 'POST':
        search_query = request.form['search_query']
        # condition to check if exists in cache storage or not
        from_store = mysqlite_client.execute("SELECT DOCUMENT FROM STORE WHERE KEY=?", (search_query,))
        from_store_all = from_store.fetchall()
        if len(from_store_all) != 0 :
            document_dumps = from_store_all
        else :
            # condition to fetch it from the mongoDB cloud
            mongo_collection = mongo_database["listingsAndReviews"]
            mongo_query = { "property_type" : search_query }
            documents = mongo_collection.find(mongo_query)
            document_dumps = dumps(documents)
            insert_into_cache(search_query, document_dumps)
            
    return render_template('display_results.html', search_query = search_query, documents=document_dumps)


def insert_into_cache(search_query, document_dumps):
    mysqlite_client.execute("INSERT INTO STORE(KEY, DOCUMENT) VALUES(?,?);", (search_query, document_dumps))


if __name__ == "__main__":
    app.run()