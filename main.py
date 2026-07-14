from dotenv import load_dotenv
from datetime import datetime
from nextdns import get_data
from stats import get_stats
from display import show_stats
import requests
import os
import time

load_dotenv()

api_key=os.getenv("NEXTDNS_API_KEY")
profile_id=os.getenv("NEXTDNS_PROFILE_ID")



def main():
    while True:
        data=get_data(api_key,profile_id)
        if data:
            total_queries,blocked_queries=get_stats(data)
            show_stats(total_queries,blocked_queries)

        else:
            print("Unable to fetch NextDNS data")

        time.sleep(60)

if  __name__=="__main__":
    main()
