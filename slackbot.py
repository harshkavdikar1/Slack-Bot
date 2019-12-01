from flask import Flask, redirect, url_for, request, Response
import logging, pickle, requests

app = Flask(__name__)

score = {}

slack_api_token = ""

@app.route('/slack/display_score/', methods=['GET','POST'])
def display_score():
	app.logger.info(request.form['user_id'])
	return Response(str(score[request.form['user_id']]))

@app.route('/slack/', methods=['GET','POST'])
def enable_event_api_slack():
	data = request.get_json()
	app.logger.info(data)
	if data['type']=='event_callback':
		if 'subtype' not in data['event'] or data['event']['subtype'] != "bot_message":
			input = data['event']['text'].split(' ')
			user = input[0].rstrip('>').lstrip('<@')
			try:
				score[user] = score.get(user, 0) + int(input[1])
				file = open("data.txt", "wb")
				pickle.dump(score, file)
				file.close()
				post_reply("Score Recorded for student")
			except:
				post_reply("Sorry something is wrong with message")
			app.logger.info(score)
		return Response()
	elif data['type']=='url_verification':
		return Response(data['challenge'])

def post_reply(res):
	data = {
		"token": slack_api_token,
		"channel": "CMXD72WUE",
		"text": res
	}
	requests.post(url='https://slack.com/api/chat.postMessage', data=data)

if __name__ == '__main__':
	file = open("data.txt", "rb")
	score = pickle.load(file)
	file.close()
	app.run(debug = True)
