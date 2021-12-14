# post2discord.py

A simple Python script to post/update a message on Discord via Webhook

usage: post2discord.py [-h] [--id ID] [--username USERNAME] url message

post or update a message on a Discord webhook, returns message.id on success

positional arguments:
  url                  webhook URL
  message              "the message contents"

optional arguments:
  -h, --help           show this help message and exit
  --id ID              message.id to update
  --username USERNAME  override the default username of the webhook, will be ignored by Discord if we are updating

examples:
  post2discord.py https://discord.com/api/123456789098765432/xx_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxx "Hello world!"
  post2discord.py --username Mr.X https://discord.com/api/123456789098765432/xx_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxx "Hello world!"
  post2discord.py --id 234567890987654321 https://discord.com/api/123456789098765432/xx_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxxxx "Hello updated world!"
