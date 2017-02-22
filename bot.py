import tweepy, requests, random
from secrets import *

class Volume:
    def __init__(self, name, plural, ml):
        self.name = name
        self.plural = plural
        self.ml = float(ml)

class Duration:
    def __init__(self, name, plural, s):
        self.name = name
        self.plural = plural
        self.s = float(s)

class Area:
    def __init__(self, name, plural, m3):
        self.name = name
        self.plural = plural
        self.m3 = float(m3)

with open("volumes.csv") as f:
    volumes = [Volume(*[c.strip() for c in l[:-1].split(",")]) for l in f]
    
with open("durations.csv") as f:
    durations = [Duration(*[c.strip() for c in l[:-1].split(",")]) for l in f]
    
with open("areas.csv") as f:
    areas = [Area(*[c.strip() for c in l[:-1].split(",")]) for l in f]

choice = random.choice(["volume", "duration", "area"])

choice = "volume"

if choice == "volume":
    a = random.choice(volumes)
    b = a
    while b.ml * 2 > a.ml:
        a = random.choice(volumes)
        b = random.choice(volumes)

    message = "Approximately " + str(int((a.ml / b.ml))) + " " + b.plural + " fit into " + a.name + "."

if choice == "duration":
    a = random.choice(durations)
    b = a
    while b.s * 2 > a.s:
        a = random.choice(durations)
        b = random.choice(durations)

    if len(b.plural) == 0:
        message = b.name[0].upper() + b.name[1:] + " fits into " + a.name + " approximately " + str(int((a.s / b.s))) + " times."
    else:
        message = "Approximately " + str(int((a.s / b.s))) + " " + b.plural + " fit into " + a.name + "."

if choice == "area":
    a = random.choice(areas)
    b = a
    while b.m3 * 2 > a.m3:
        a = random.choice(areas)
        b = random.choice(areas)

    message = "Approximately " + str(int((a.m3 / b.m3))) + " " + b.plural + " fit into " + a.name + "."

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status(message)

print message
