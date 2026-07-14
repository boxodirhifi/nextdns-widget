from dotenv import load_dotenv
from datetime import datetime
import requests
import os
import json
import time

load_dotenv()

api_key=os.getenv("NEXTDNS_API_KEY")
profile_id=os.getenv("NEXTDNS_PROFILE_ID")


def get_data():

    url = f"https://api.nextdns.io/profiles/{profile_id}/analytics/status"

    headers={
        "X-Api-Key": api_key
    }

    try:
        response=requests.get(url, headers=headers, timeout=10)

    except requests.exceptions.RequestException:
        return None


    if response.status_code!=200:
        print(f"API request failed: {response.status_code}")
        return None

    return response.json()


def get_stats(data):

    total_queries=0
    blocked_queries=0

    for item in data["data"]:
        if item["status"]=="blocked":
            blocked_queries=item["queries"]

        if item["status"]=="default":
            total_queries=item["queries"]

    return total_queries, blocked_queries



def show_stats(total_queries,blocked_queries):
    total=total_queries+blocked_queries
    percentage=blocked_queries/total*100
    current_time=datetime.now().strftime("%H:%M:%S")

    print("====== NextDNS Stats ======")
    print(f"Last updated: {current_time}")
    print(f"Allowed: {total_queries}")
    print(f"Blocked: {blocked_queries}")
    print(f"Total queries: {total}")
    print(f"Blocked percentage: {percentage:.2f}%")

while True:
    data=get_data()
    if data:
        total_queries,blocked_queries=get_stats(data)
        show_stats(total_queries,blocked_queries)

    else:
        print("Unable to fetch NextDNS data")

    time.sleep(60)
