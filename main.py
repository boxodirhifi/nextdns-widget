from dotenv import load_dotenv
from nextdns import get_data
from stats import get_stats, save_json
from display import show_stats
import argparse
import json
import os
import time

load_dotenv()

api_key=os.getenv("NEXTDNS_API_KEY")
profile_id=os.getenv("NEXTDNS_PROFILE_ID")




def output_json(total_queries,blocked_queries):
    total = total_queries+blocked_queries
    percentage=(blocked_queries/total*100) if total else 0.0

    data={
        "allowed": total_queries,
        "blocked": blocked_queries,
        "total": total,
        "percentage": round(percentage,2)
        }

    print(json.dumps(data))



def main():

    parser=argparse.ArgumentParser()
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()


    total_queries=0
    blocked_queries=0

    while True:
        data=get_data(api_key,profile_id)
        if data:
            total_queries,blocked_queries=get_stats(data)
            save_json(total_queries,blocked_queries)

        else:
            print("Unable to fetch NextDNS data")

        if args.json:
            output_json(total_queries,blocked_queries)
            return

        else:
            show_stats(total_queries,blocked_queries)

        time.sleep(60)

if __name__=="__main__":
    main()
