#!/usr/bin/python3

import os
from argparse import ArgumentParser
from requests import post


# Set up arguments
parser = ArgumentParser(description='A very simple OpenContest command line client written in Python')
parser.add_argument('command', choices=['save', 'about', 'info', 'statement', 'solves',
                    'history', 'register', 'submit', 'status', 'submissions', 'code'], type=str)
parser.add_argument('-C', '--config', help='Config file path', default='~/.config/occ/config', type=str)
parser.add_argument('-U', '--username', help='Your username', type=str)
parser.add_argument('-H', '--homeserver', help='URL of your registration server', type=str)
parser.add_argument('-P', '--password', help='Your username', type=str)
parser.add_argument('-N', '--name', help='Your name for registering an account', type=str)
parser.add_argument('-E', '--email', help='Your email for registering an account', type=str)
parser.add_argument('-s', '--server', help='URL of the server you are connecting to', type=str)
parser.add_argument('-c', '--contest', help='Contest to query', type=str)
parser.add_argument('-p', '--problem', help='Problem to query', type=str)
parser.add_argument('-f', '--file', help='File for code submission', type=str)
parser.add_argument('-n', '--number', help='Submission number to query', type=str)
args = parser.parse_args()


# Use HTTPS
if args.server != None:
    args.server = 'https://' + args.server
if args.homeserver != None:
    args.homeserver = 'https://' + args.homeserver


# Process config file
args.config = os.path.expanduser(args.config)
if os.path.exists(args.config):
    # Read in values from file
    with open(args.config, 'r') as f:
        lines = f.readlines()
        if args.username == None:
            args.username = lines[0][:-1]
        if args.homeserver == None:
            args.homeserver = lines[1][:-1]
        if args.password == None:
            args.password = lines[2][:-1]


if args.command == 'save':
    # Save values to config file
    os.makedirs(os.path.dirname(args.config), exist_ok=True)
    with open(args.config, 'w') as f:
        f.write(args.username + '\n' + args.homeserver + '\n' + args.password + '\n')
    exit()


# Construct request fields based on the OpenContest standard
# https://laduecs.github.io/OpenContest/
probleminfo = ['contest', 'problem']
userinfo = ['username', 'homeserver', 'token']
requests = {
    'about': [],
    'info': probleminfo,
    'statement': probleminfo,
    'solves': probleminfo,
    'history': probleminfo,
    'register': ['name', 'email', 'username', 'password'],
    'submit': userinfo + probleminfo + ['language', 'code'],
    'status': userinfo + probleminfo,
    'submissions': userinfo + probleminfo,
    'code': userinfo + probleminfo + ['number']
}


# Create the request body
body = { 'type': args.command }
for field in requests[args.command]:
    if field == 'problem' and args.problem == None:
        continue
    elif field == 'token':
        body['token'] = post(args.server, json={
            'type': 'authenticate',
            'username': args.username,
            'homeserver': args.homeserver,
            'password': args.password
        }).text
    elif field == 'language':
        body['language'] = os.path.splitext(args.file)[1][1:]
    elif field == 'code':
        body['code'] = open(args.file, 'r').read()
    else:
        body[field] = eval('args.' + field)  # Yay, eval!


# Send the POST request
r = post(args.server, json=body)
print(r.reason)
if args.command == 'statement':
    os.makedirs(args.contest, exist_ok=True)
    # Save problem statments to file
    filename = 'problems' if args.problem == None else args.problem
    with open(os.path.join(args.contest, filename + '.pdf'), 'wb') as f:
        f.write(r.content)
else:
    print(r.text)
exit()
