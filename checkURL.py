def checkURL(url):
    import requests
    # Check if the URL is accessible
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.ConnectionError:
        return False