
# with open('keys.json') as json_file:
#     data = json.load(json_file)

# user_id = 2715311622 #@drilippi
# bearer_oauth = data['bearertoken']
import requests
import os
import json
import pandas

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'

with open('keys.json') as json_file:
    data = json.load(json_file)
bearer_oauth = data['bearertoken']
#bearer_token = os.environ.get("BEARER_TOKEN")
bearer_token = bearer_oauth



def create_url():
    # Replace with user ID below
    user_id = 2715311622
    return "https://api.twitter.com/2/users/{}/followers".format(user_id)


def get_params():
    # return {"user.fields": "created_at", "max_results": 100, "pagination_token" : "" }
    return {"user.fields": "created_at", "max_results": 1000 }


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FollowersLookupPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    return json_response
    #print(json.dumps(json_response, indent=4, sort_keys=True))




if __name__ == "__main__":
    results = main()
    with open('followers1.json', 'w') as outfile:
        json.dump(results, outfile)