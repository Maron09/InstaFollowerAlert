from instagram_private_api import Client
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import time
import json
import requests
import os

username = "Your instagram username"
password = "Password"
target_username = "Target Username"
webhook_url = "https://ba9c-102-89-41-217.ngrok-free.app/" # Reaplae with you webhook URl
json_file = "followers.json"


api = Client(username, password)


user_id = api.username_info(target_username)["user"]["pk"]
prev_follower_count = api.user_info(user_id)["user"]["follower_count"]


if not os.path.exists(json_file):
    with open(json_file, "w") as f:
        json.dump([], f)


while True:
    
    results = api.user_info(user_id)
    follower_count = results["user"]["follower_count"]
    print(f"Current follower count: {follower_count}")

    
    if follower_count > prev_follower_count:
        print("New follower detected!")
        followers = api.user_followers(user_id, rank_token=api.generate_uuid())["users"]
        new_follower = None
        with open(json_file, "r") as f:
            prev_followers = json.load(f)
        for follower in followers:
            if follower["username"] not in prev_followers:
                new_follower = follower["username"]
                break
        if new_follower is None:
            print("No new followers")
            continue
        print(f"New follower username: {new_follower}")

        
        with open(json_file, "w") as f:
            json.dump([follower["username"] for follower in followers], f)

        
        output = f'{{"username": "{target_username}", "New_follower": "{new_follower}"}}'
        with open("output.json", "a") as f:
            f.write(output + "\n")
        
        payload = {"text": f"New follower detected: {new_follower}"}
        headers = {"Content-type": "application/json"}
        response = requests.post(webhook_url, json=payload, headers=headers)
        if response.status_code != 200:
            print(f"Failed to send webhook: {response.text}")

    else:
        print("No new followers")

    prev_follower_count = follower_count
    time.sleep(60) 
