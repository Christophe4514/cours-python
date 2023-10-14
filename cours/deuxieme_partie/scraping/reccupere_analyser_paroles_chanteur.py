# en utilisant le site genius qui poste des lyrics des chanssons
# chanssons de patrick bruel

import collections
import json
from pprint import pprint
import requests
from bs4 import BeautifulSoup

def is_valid(word, word_length):
    if len(word) < word_length:
        return False

    return "[" not in word and "]" not in word


def extract_lyrics(url, word_length=10):
    r = requests.get(url)
    print(r.status_code)
    if r.status_code != 200:
        print("page impossible a chargé")
        return []

    soup = BeautifulSoup(r.content, 'html.parser')
    lyrics = soup.find("div", class_="Lyrics__Container-sc-1ynbvzw-1 kUgSbL")
    if not lyrics:
        return extract_lyrics(url, word_length=word_length)

    all_words = []

    for sentence in lyrics.stripped_strings:
        sentence_words = [word.strip(",").strip(".").lower() for word in sentence.split() if is_valid(word, word_length)]
        all_words.extend(sentence_words)
        # print(sentence.split())

    # counter = collections.Counter(all_words)
    # pprint(counter.most_common(10))
    # print(lyrics)
    # pprint(all_words)

    return all_words


def get_all_url():
    page_number = 1
    links = []
    while True:
        r = requests.get(f"https://genius.com/api/artists/29743/songs?page={page_number}&sort=popularity")
        # print(r.status_code)
        # pprint(r.json().get("response"))
        if r.status_code == 200:
            print(f"fetching page {page_number}")
            # return
            response = r.json().get("response", {})
            next_page = response.get("next_page")

            songs = response.get("songs")
            links.extend([song.get("url") for song in songs])
            # pprint(links)
            # print(next_page)
            page_number += 1

            if not next_page:
                print("pas de next_page_number à appeler")
                break

        # pprint(links)
        # print(len(links))

    return links


def get_all_words():
    urls = get_all_url()
    words = []
    for url in urls:
        lyrics = extract_lyrics(url=url)
        words.extend(lyrics)

    with open("data.json", "w") as f:
        json.dump(words, f, indent=4)

    # with open("data.json", "r") as f:
    #     words = json.load(f)

    counter = collections.Counter(words)
    most_common_word = counter.most_common(15)

    pprint(most_common_word)


# get_all_url()
# extract_lyrics(url="https://genius.com/Patrick-bruel-musique-vieille-lyrics")

get_all_words()
