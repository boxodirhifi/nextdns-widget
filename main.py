from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

api_key=os.getenv("NEXTDNS_API_KEY")
profile_id=os.getenv("NEXTDNS_PROFILE_ID")

url = f"https://api.nextdns.io/profiles/{profile_id}/analytics/status"

headers={
    "X-Api-Key": api_key
    }

response=requests.get(url,headers=headers)

if response.status_code!=200:
    print("API request failed")
    exit()

print(response.status_code)

data=response.json()
print(json.dumps(data, indent=4))




total_queries = 0
blocked_queries = 0



for item in data["data"]:
    if item["status"] == "blocked":
        blocked_queries = item["queries"]

    if item["status"] == "default":
        total_queries = item["queries"]


total= total_queries+blocked_queries
percentage=blocked_queries/total*100



print(f"Allowed: {total_queries}")
print(f"Blocked: {blocked_queries}")

print(f"Total queries: {total}")
print(f"Blocked percentage: {percentage:.2f}%")
