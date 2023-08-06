import random
import requests


base_url = "https://some-random-api.ml/"
aliases = {
    "dog": "dog",
    "cat": "cat",
    "panda": "panda",
    "fox": "fox",
    "kangaroo": "kangaroo",
    "raccoon": "raccoon",
    "bird": "birb",
    "red_panda": "red_panda",
    "koala": "koala",
}


def animal_data(animalname):
    res = requests.get(base_url + f"animal/{aliases[animalname]}")
    if res.status_code != 200:
        return "Invalid response from API"
    return res.json()


def rand_animals():
    rand_data = random.choice(
        [
            "dog",
            "cat",
            "panda",
            "fox",
            "kangaroo",
            "raccoon",
            "birb",
            "red_panda",
            "koala",
        ]
    )
    res = requests.get(base_url + f"animal/{rand_data}")
    if res.status_code != 200:
        return "Invalid response from API"
    return res.json()
