from flask import Flask, request, session
from twilio.twiml.messaging_response import (
    MessagingResponse,
    Message,
    Body,
    Media
    )
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import get_data

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': 'anthelp-3f78a'
})

db = firestore.client()


app = Flask(__name__)
SECRET_KEY = 'nAKBEUkukYLzgu1t3nhccrdsxV5IT5IC'
account_sid = 'SK4a387eefcebc18b161c694ceca40448f'
app.config.from_object(__name__)

# Standard messages
default_msg = "Sorry, we didn't understand your request (or don't have any answers!) :("
greeting = """\n\nHello! Welcome to Anthelp!\n\nSend a text in the following format: [adjective noun], for example "good food", and we'll try to answer!\n\n"""

# text ZOTZOT TO 1-626-427-3513 to begin
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        resp = MessagingResponse()
        query = request.form['Body'].lower()
        create_message(query, resp)
        #return "post"
    return str(resp)


def create_message(query, resp):
    if query == "zot zot":
        resp.message(greeting)
    elif any(x in query for x in ["hi", "hello", "what's up"]):
        msg = resp.message("Hiya! Welcome to UCI!")
        msg.media("https://www.parking.uci.edu/AT/images/UCI-wazer-4.png")
    elif any(x in query for x in ["thank you", "thanks", "ty", "thx"]):
        resp.message("You're welcome! Have a good one!")
    else:
        words = query.split()
        if len(words) != 2:
            default_response(resp)
        else:
            adj, noun = words
            if any(noun in query for noun in ["food", "hungry", "eat"]):
                create_response("food", adj, resp)
            elif any(noun in query for noun in ["study", "library", "quiet"]):
                create_response("Study Spaces", adj,resp)
            else:
                default_response(resp)

def create_response(cat, adj,resp):
    items = get_data.search_by_adjective(adj, get_data.get_info(cat, db))
    if len(items) == 0:
        default_response(resp)
        return
    return_message = "\n\nThanks for asking. Here's what we got!\n"
    for i in items:
        return_message += str(i[0]) + " - " + ", ".join(i[1]["Locations"]) +  "\n"
    resp.message(return_message)


def default_response(resp):
    resp.message(default_msg)

if __name__ == "__main__":
    app.run()
