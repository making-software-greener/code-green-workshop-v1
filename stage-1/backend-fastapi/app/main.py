''' Shakespeare API '''
'''
TODO:
1. make plays & players case insensitive for the search
'''
import re
from collections import Counter

from typing import Optional

from fastapi import FastAPI
from tinydb import TinyDB, Query


db = TinyDB('/app/app/db/shakespearedb.json')
Plays = Query()


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/plays")
def get_play_names():
    plays = [play.get('Play') for play in db.search(Plays.Play.exists())]
    plays = list(set(plays))
    plays.sort()
    return {"plays": plays}

@app.get("/players")
def get_player_names():
    players = [play.get('Player') for play in db.search(Plays.Player.exists())]
    players = list(set(players))
    players.sort()
    return {"players": players}


@app.get("/plays/{play_name}/players")
def get_play_players(play_name: str):
    players = [player.get("Player") for player in db.search((Plays.Player.exists()) & (Plays.Play == play_name))]
    players = list(set(players))
    players.sort()
    return {"players": players}

def raw_words(query_results):
    words = [re.sub('[\W_]', ' ', line.get("PlayerLine")).lower().split() for line in query_results]
    words_flattened = [item for sub_list in words for item in sub_list]
    return words_flattened

@app.get("/words")
def get_words():
    words = raw_words(db.search(Plays.PlayerLine.exists()))
    words2 = list(Counter(words).keys())
    words2.sort()
    return {"words": words2}

@app.get("/words/counts")
def get_words_counts():
    words = raw_words(db.search(Plays.PlayerLine.exists()))
    counter = Counter(words)
    words2 = list(zip(counter.keys(), counter.values()))
    words2.sort(key = lambda x: x[0])
    return {"word_counts": words2}

@app.get("/words/play/{play_name}")
def get_play_words(play_name: str):
    words = raw_words(db.search((Plays.PlayerLine.exists()) & (Plays.Play == play_name)))
    words2 = list(Counter(words).keys())
    words2.sort()
    return {"words": words2}

@app.get("/words/play/{play_name}/count")
def get_play_words_count(play_name: str):
    words = raw_words(db.search((Plays.PlayerLine.exists()) & (Plays.Play == play_name)))
    counter = Counter(words)
    words2 = list(zip(counter.keys(), counter.values()))
    words2.sort(key = lambda x: x[0])
    return {"play_word_counts": words2}

@app.get("/words/player/{player_name}")
def get_player_words(player_name: str):
    words = raw_words(db.search((Plays.PlayerLine.exists()) & (Plays.Player == player_name)))
    words2 = list(Counter(words).keys())
    words2.sort()
    return {"words": words2}

@app.get("/words/player/{player_name}/count")
def get_player_words_count(player_name: str):
    words = raw_words(db.search((Plays.PlayerLine.exists()) & (Plays.Player == player_name)))
    counter = Counter(words)
    words2 = list(zip(counter.keys(), counter.values()))
    words2.sort(key = lambda x: x[0])
    return {"player_word_counts": words2}


