# Flask App for Spam Notification Alerts
This repository contains a sample Python script that processes spam notification alerts and sends them to a Slack channel using the Slack API. The script is written in Python and uses the Flask framework to create a web application that receives webhook payloads from a third-party provider.

### Requirements
- Python
- Flask
- slack-sdk

### How to Use
Clone the repository to your local machine.

Make sure you have your Slack token and channel_id in a `.env` file that is located in this project, in addition to an Slack app
integrated to your Slack via admin panel.

Install the required packages by running the command `pip install -r requirements.txt` in your terminal.
Run the script using the command `flask run`
The Flask app will run on http://localhost:5000.
