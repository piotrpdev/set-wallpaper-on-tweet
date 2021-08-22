import requests
import os
import json
import time

import ctypes

from secrets import bearer_token

testing = False
user_id = 3466569498 # Twitter UserID of the person you're listening to
wait_time = 3600 # 1 Hour

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )

    return response.json()

def get_testing_data(type):
    if type == "new":
        path = "/testing_data/new.json"
    else:
        path = "/testing_data/old.json"
    
    with open(os.path.dirname(__file__) + path) as jsonFile:
        jsonObject = json.load(jsonFile)
        jsonFile.close()

    return jsonObject

def download_wallpaper(url):
    with open(os.path.dirname(__file__) + "/" + "wallpaper.jpg", 'wb') as handle:
        response = requests.get(url, stream=True)

        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

def set_wallpaper():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.dirname(__file__) + "/" + "wallpaper.jpg", 0)

def main():
    url = "https://api.twitter.com/2/users/{}/tweets".format(user_id)
    params = {"tweet.fields": "created_at,attachments", "media.fields": "url", "max_results": 5, "exclude": "retweets,replies", "expansions": "attachments.media_keys"}

    while True:
        if testing:
            json_response = get_testing_data("new")
        else:
            json_response = connect_to_endpoint(url, params)

        with open(os.path.dirname(__file__) + "/" + "current_wallpaper.txt", "r+") as current_wallpaper_file:
            current_wallpaper = current_wallpaper_file.read()
            print("Current wallpaper url: " + current_wallpaper)

            newest_tweeted_wallpaper = json_response["includes"]["media"][0]["url"]

            if current_wallpaper == newest_tweeted_wallpaper:
                print("Newest wallpaper matches the current one")
            else:
                print("New wallpaper tweeted with url: " + newest_tweeted_wallpaper)

                print("Downloading wallpaper...")
                download_wallpaper(newest_tweeted_wallpaper)

                print("Setting wallpaper...")
                set_wallpaper()    
        
                print("Updating record...")
                current_wallpaper_file.seek(0)
                current_wallpaper_file.write("https://pbs.twimg.com/media/E9ajfO0VIAAMQXl.jpg")
                current_wallpaper_file.truncate()

        print(f"Sleeping... (for {wait_time}s)")
        time.sleep(wait_time)

        #print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()