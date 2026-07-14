import requests


def get_data(api_key,profile_id):

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
