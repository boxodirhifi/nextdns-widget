def get_stats(data):

    total_queries=0
    blocked_queries=0

    for item in data["data"]:
        if item["status"]=="blocked":
            blocked_queries=item["queries"]

        if item["status"]=="default":
            total_queries=item["queries"]

    return total_queries, blocked_queries
