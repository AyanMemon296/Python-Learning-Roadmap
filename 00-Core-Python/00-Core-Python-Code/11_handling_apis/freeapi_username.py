import requests

def fetch_randome_user_freeapi():
    """
    Fetch a random user from the Free API.
    
    Returns:
        dict: A dictionary containing user information.
    """
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data from Free API")
    
def main():
    try:
        username, country = fetch_randome_user_freeapi()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()