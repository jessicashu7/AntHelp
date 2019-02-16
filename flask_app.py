from flask import Flask, request, session
from twilio.twiml.messaging_response import (
    MessagingResponse,
    Message,
    Body,
    Media
    )

app = Flask(__name__)
SECRET_KEY = 'nAKBEUkukYLzgu1t3nhccrdsxV5IT5IC'
account_sid = 'SK4a387eefcebc18b161c694ceca40448f'
app.config.from_object(__name__)

# Standard messages
default_msg = "Sorry, we didn't understand your question (or don't have any answers!) :("
greeting = """\n\nHello! Welcome to Anthelp!\n\nText us a question, and we'll try to answer!\n\nFor example, try 'I'm hungry', or 'Where can I park?'"""

# text ZOTZOT TO 1-626-427-3513 to begin

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    counter = session.get('counter', 0)
    ### GREETING MESSAGE
    if counter == 0:
        # create greeting
        greetResp = MessagingResponse()
        # insert greeting message
        greetResp.message(greeting)
        # return greeting message
        counter += 1
        session['counter'] = counter
        return str(greetResp)

    # create next message
    resp = MessagingResponse()
    if request.method == 'POST':
        # get message body
        query = request.form['Body']
        ## process query here
        parse_message(query, resp)

    return str(resp)

def parse_message(query, resp):
    # determine what type of response to send based off of text content
    if any(x in query for x in ["food", "hungry", "eat"]):
        food_response(query, resp)
    else:
        default_response(query, resp)

def food_response(query, resp):
    # for food related responses
    resp.message("How about Panda Express?")

def default_response(query, resp):
    # if it doesn't match anything :(
    resp.message(default_msg)

if __name__ == "__main__":
    app.run(debug=True)