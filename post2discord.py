#!/usr/bin/env python3
# post2discord.py
# A smple Python script to post/update a message on Discord via Webhook
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

import json
import argparse
import requests

parser = argparse.ArgumentParser(description='post or update a message on a Discord webhook, returns message.id on success')
parser.add_argument ('url', help='webhook URL')
parser.add_argument ('message', help='"the message contents"')
parser.add_argument ('--id', help='message.id to update')
parser.add_argument ('--username', help='override the default username of the webhook, will be ignored by Discord if we are updating')
args = parser.parse_args()

data = { 'content': args.message }
if args.username:  data['username'] = args.username

if args.id is None:
	response = requests.post(args.url+'?wait=true',data)
else:
	response = requests.patch(args.url+'/messages/'+args.id+'?wait=true',data)

if response.ok:
	jsonres = response.json()
	print(jsonres['id'])
else:
	print('%s: %s',response.status_code, response.text)
