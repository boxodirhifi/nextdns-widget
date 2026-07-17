import json
from datetime import datetime

def get_stats(data):

    total_queries=0
    blocked_queries=0

    for item in data["data"]:
        if item["status"]=="blocked":
            blocked_queries=item["queries"]

        if item["status"]=="default":
            total_queries=item["queries"]

    return total_queries, blocked_queries

def save_json(total_queries, blocked_queries):
    total = total_queries + blocked_queries
    percentage = (blocked_queries / total * 100) if total else 0

    data = {
        "allowed": total_queries,
        "blocked": blocked_queries,
        "total": total,
        "percentage": round(percentage, 2),
        "updated": datetime.now().strftime("%H:%M:%S")
    }

    with open("stats.json", "w") as file:
        json.dump(data, file)
