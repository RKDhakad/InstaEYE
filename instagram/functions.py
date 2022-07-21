import os
import json

def profile_data(username):
    try:
        os.system(f'python -m instagram_scraper.app "{username}" --profile-metadata  --media-metadata  --media-types none')
    except:
        pass


if __name__ == "__main__":
    # profile_data("ravidhakad02")
    # print("DOne")
    pass