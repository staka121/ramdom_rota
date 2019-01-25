import os
import yaml
import random

# pip install slackclient
from slackclient import SlackClient

rota_config = open('config/rota.yml', "r")
rota = yaml.load(rota_config)

members = rota['members']

random.shuffle(members)
member = members[0]
send_text = "Today is %s turn!" % (member['name'])

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel="YOUR_CHANNEL_NAME",
  text=send_text
)
