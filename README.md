# Slack-Bot
A web application to help Professor maintain grades given in the class and allow students to access the grades at any time.

To run this application from local machine Ngrok can be used. It is a tunneling tool which tunnels local host to the internet.

How to use Ngrok:

Download, Install and set up Path variables for Ngrok.
Run the Ngrok.
Enter the command: Ngrok http 5000 #where 5000 is the port our server is running on.
Go to slack select your application, select the API you want to use and enter the Ngrok URI (You will have your own URI) http://1e640e27.Ngrok.io/slack/ which tunnel your local host to the network. Similarly, you can add following URI http://1e640e27.Ngrok.io/slack/display_score/ for using the bot.