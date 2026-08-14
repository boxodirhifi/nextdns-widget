import json
import os
from datetime import datetime
from pathlib import Path


def get_stats(data):
    total_queries = 0
    blocked_queries = 0

    for item in data["data"]:
        if item["status"] == "blocked":
            blocked_queries = item["queries"]

        if item["status"] == "default":
            total_queries = item["queries"]

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

    data_dir = Path(
        os.environ.get("XDG_DATA_HOME", Path.home() / ".local/share")
    ) / "nextdns-widget"

    data_dir.mkdir(parents=True, exist_ok=True)

    with open(data_dir / "stats.json", "w") as file:
        json.dump(data, file)
