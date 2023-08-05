import requests
import random

def fetch_blogs():
    url = 'https://allround.club/blog/wp-json/wp/v2/posts'
    r = requests.get(url)
    return r.json()

def fetch_random_blog():
    links = fetch_blogs()
    random_blog = links[random.randint(0, len(links) - 1)]
    return random_blog["link"]
