import requests
import csv

SERVER_URL = "http://34.71.138.79:9090/"
ENDPOINT = "/sybil/{binary_or_affine}/{home_or_defense}"
URL = SERVER_URL + ENDPOINT

TEAM_TOKEN = "DdE56eC1EvRwWcuy"


def sybil_attack(ids, home_or_defense: str, binary_or_affine: str = "affine"):
    if home_or_defense not in ["home", "defense"] or binary_or_affine not in ["binary", "affine"]:
        raise "Invalid endpoint"

    ids = ids = ",".join(map(str, ids))

    response = requests.get(
        URL.format(binary_or_affine=binary_or_affine, home_or_defense=home_or_defense),
        params={"ids": ids},
        headers={"token": TEAM_TOKEN}
    )

    if response.status_code == 200:
        return response.content["representations"]
    else:
        raise Exception(f"Request failed. Status code: {response.status_code}, content: {response.content}")


output_file = "out.csv"

fieldnames = ["img_id", "type", "response"]
writer = csv.DictWriter(output_file, fieldnames=fieldnames)


COMMON_IDS = list(range(1000))

response =