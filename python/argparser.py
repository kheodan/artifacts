import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--token", help="token to bot auth")
parser.add_argument("-c", "--channel", help="ID for RO channel on server")
parser.add_argument("-e", "--exclude", help="roles to exclude for serve")

token = args.token if args.token else input('Token: ')
channel_id = args.channel if args.channel else input('RO channel ID: ')
exclude = args.exclude if args.exclude else input('Exclude: ')
