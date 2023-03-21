"""
 ╔════════════════════════════╗
 ║ ╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╗ ╔═╗╔╦╗ ║
 ║  ╠╣ ║║╠═╝╠╣ ╠═╣  ╠╩╗║ ║ ║  ║
 ║ ╚═╝╚╩╝╩  ╚  ╩ ╩  ╚═╝╚═╝ ╩  ║
 ╚════════════════════════════╝

Tweet Extractor

WTFPL litepresence 2021
"""

# STANDARD MODULES
import json
import re
import time
from datetime import datetime

# THIRD PARTY MODULES
import requests

# 3DPFA MODULES
from config import USERS

# GLOBAL CONSTANTS
GUEST_TOKEN_ENDPOINT = "https://api.twitter.com/1.1/guest/activate.json"
STATUS_ENDPOINT = "https://twitter.com/i/api/graphql/"
CURSOR_PATTERN = re.compile(r'TimelineCursor","value":"([^"]+)"[^\}]+Bottom"')
ID_PATTERN = re.compile('"rest_id":"([^"]+)"')
COUNT_PATTERN = re.compile('"statuses_count":([0-9]+)')
ISSUE = "Please submit an issue including this information."
VARIABLES = {
    "count": 200,
    "withTweetQuoteCount": True,
    "includePromotedContent": True,
    "withQuickPromoteEligibilityTweetFields": False,
    "withSuperFollowsUserFields": True,
    "withUserResults": True,
    "withBirdwatchPivots": False,
    "withDownvotePerspective": False,
    "withReactionsMetadata": False,
    "withReactionsPerspective": False,
    "withSuperFollowsTweetFields": True,
    "withVoice": True,
    "withV2Timeline": False,
}


def send_request(url, session_method, headers, params=None):
    """
    make an external request to the twitter api backdoor
    """
    if params:
        response = session_method(
            url, headers=headers, stream=True, params={"variables": json.dumps(params)}
        )
    else:
        response = session_method(url, headers=headers, stream=True)
    if response.status_code != 200:
        print(response.request.url)
        print(response.status_code)
    assert (
        response.status_code == 200
    ), f"Failed request to {url}.  {response.status_code}.  {ISSUE}"
    result = [line.decode("utf-8") for line in response.iter_lines()]
    return "".join(result)


def search_json(j, target_key, result):
    """
    recursive search through json dictionary
    """
    if isinstance(j, dict):
        for key in j:
            if key == target_key:
                result.append(j[key])
            search_json(j[key], target_key, result)
        return result
    if isinstance(j, list):
        for item in j:
            search_json(item, target_key, result)
        return result
    return result


def filter_subset(tweet):
    """
    extract only the pertinent information from the tweet and reformat the dict()
    """
    # rename id_str and full_text to id and text; format text to remove newlines, etc.
    tweet["id"] = tweet["id_str"]
    tweet["text"] = tweet["full_text"].replace("\n", " ").replace("\\", "")
    # create a human readable and unix timestamp
    tweet["date"] = tweet["created_at"].replace("+0000 ", "").split(" ", maxsplit=1)[1]
    tweet["unix"] = int(
        time.mktime(datetime.strptime(tweet["date"], "%b %d %H:%M:%S %Y").timetuple())
    )
    # extract videos and preview thumbnails
    try:
        tweet["video"] = tweet["retweeted_status_result"]["result"]["legacy"][
            "extended_entities"
        ]["media"][0]["video_info"]["variants"][0]["url"].split("?")[0]
    except Exception:
        pass
    try:
        tweet["video_thumb"] = tweet["retweeted_status_result"]["result"]["legacy"][
            "extended_entities"
        ]["media"][0]["media_url_https"]
    except Exception:
        pass
    # extract youtube and preview thumbnails
    try:
        binding_values = tweet["retweeted_status_result"]["result"]["card"]["legacy"][
            "binding_values"
        ]
        tweet["youtube"] = [
            i["value"]["string_value"]
            for i in binding_values
            if i["key"] == "player_url"
        ][0]
        tweet["youtube_thumb"] = [
            i for i in binding_values if i["key"] == "player_image_large"
        ][0]
        tweet["youtube_thumb"] = tweet["youtube_thumb"]["value"]["image_value"]["url"]
    except Exception:
        pass
    # extract website preview thumbnails
    try:
        binding_values = tweet["retweeted_status_result"]["result"]["card"]["legacy"][
            "binding_values"
        ]
        tweet["web_thumb"] = [
            i for i in binding_values if i["key"] == "thumbnail_image_large"
        ][0]
        tweet["web_thumb"] = tweet["web_thumb"]["value"]["image_value"]["url"]
    except Exception:
        pass
    # slim down entities
    entities = tweet["entities"]
    items_to_pop = [
        "user_mentions",
        "symbols",
    ]
    for item in items_to_pop:
        try:
            entities.pop(item)
        except Exception:
            pass
    tweet["entities"] = entities
    # slim down entities/media
    if "media" in tweet["entities"]:
        tweet["media"] = [i["media_url_https"] for i in tweet["entities"]["media"]]
    else:
        tweet["media"] = []
    # create an images key and list all image files
    tweet["images"] = tweet["media"]
    additional_images = [
        "video_thumb",
        "web_thumb",
        "youtube_thumb",
    ]
    for image in additional_images:
        try:
            tweet["images"].append(tweet[image])
        except Exception:
            pass
    tweet["images"] = list(set(tweet["images"]))
    # remove everything else from the tweet dictionary
    items_to_pop = [
        "conversation_id_str",
        "in_reply_to_screen_name",
        "in_reply_to_status_id_str",
        "in_reply_to_user_id_str",
        "is_quote_status",
        "lang",
        "quote_count",
        "reply_count",
        "retweet_count",
        "retweeted",
        "source",
        "user_id_str",
        "id_str",
        "favorited",
        "favorite_count",
        "display_text_range",
        "full_text",
        "extended_entities",
        "possibly_sensitive",
        "possibly_sensitive_editable",
        "quoted_status_id_str",
        "quoted_status_permalink",
        "retweeted_status_result",
        "entities",
        "hashtags",
        "created_at",
        "web_thumb",
        "youtube_thumb",
        "video_thumb",
        "media",
    ]
    for item in items_to_pop:
        try:
            tweet.pop(item)
        except Exception:
            pass

    return tweet


def get_tweets(username, depth):
    """
    make request to api/graphql w/ user name to get tweets
    use a spoofed guest token to get a user's tweets and replies
    return only the most recent with image files
    """
    # create a backdoor guest token to the api and make an external request
    query_id, session, headers, variables = create_backdoor(username)
    resp = send_request(
        f"{STATUS_ENDPOINT}{query_id}/UserTweetsAndReplies",
        session.get,
        headers,
        variables,
    )
    j = json.loads(resp)
    all_tweets = search_json(j, "legacy", [])
    # ensure every tweet has full_text and id_str
    # and user_id_str matches variables["userId"]
    all_tweets = [
        tweet
        for tweet in all_tweets
        if "full_text" in tweet
        and "id_str" in tweet
        and "user_id_str" in tweet
        and "emb" not in json.dumps(tweet)
        and tweet.get("user_id_str", "") == variables["userId"]
    ]
    # clean up each tweet dictionary to only contain pertinent info
    all_tweets = [filter_subset(tweet) for tweet in all_tweets]
    # add the tweet url to each
    for tweet in all_tweets:
        tweet["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
    # filter out tweets without media content
    all_tweets = [i for i in all_tweets if "/t.co/" in i["text"]]
    # return only the most recent tweets
    return all_tweets[:depth:]


def get_user_id(session, headers, query_id, username):
    """
    make request to api/graphql w/ user name to get a user id
    ensure the user has a tweet count
    """
    resp = send_request(
        f"{STATUS_ENDPOINT}{query_id}/UserByScreenName",
        session.get,
        headers,
        params={
            "screen_name": username,
            "withSafetyModeUserFields": True,
            "withSuperFollowsUserFields": True,
        },
    )
    try:
        ids = ID_PATTERN.findall(resp)
        counts = COUNT_PATTERN.findall(resp)
        assert len(ids) == 1, f"Failed to find user id for {username}.  {ISSUE}"
        assert len(counts) == 1, f"Failed to find tweet count for {username}.  {ISSUE}"
        return ids[0]
    except Exception:
        return 0


def create_backdoor(username):
    """
    pirate a guest token to spoof an api session header
    """
    variables = dict(VARIABLES)
    session = requests.Session()
    headers = {}
    # one of the js files from original url holds the bearer token and query id
    container = send_request(f"https://twitter.com/{username}", session.get, headers)
    # find all the javascript files in container
    js_files = re.findall("src=['\"]([^'\"()]*js)['\"]", container)
    # search the javascript files for a bearer token and UserTweets queryId
    bearer_token = None
    query_id = None
    user_query_id = None
    for f in js_files:
        file_content = send_request(f, session.get, headers)
        bt = re.search("[\"'](AAA[a-zA-Z0-9%-]+%[a-zA-Z0-9%-]+)[\"']", file_content)
        ops = re.findall(
            r'\{queryId:"[a-zA-Z0-9_]+[^\}]+UserTweetsAndReplies"', file_content
        )
        query_op = [op for op in ops if "UserTweetsAndReplies" in op]
        if len(query_op) == 1:
            query_id = re.findall('queryId:"([^"]+)"', query_op[0])[0]
        if bt:
            bearer_token = bt[1]
        ops = re.findall(
            r'\{queryId:"[a-zA-Z0-9_]+[^\}]+UserByScreenName"', file_content
        )
        user_query_op = [op for op in ops if "UserByScreenName" in op]
        if len(user_query_op) == 1:
            user_query_id = re.findall('queryId:"([^"]+)"', user_query_op[0])[0]
    # confirm we have a bearer token, query_id, and user_query_id
    msg = f"Are you sure you used the right username? {username}"
    assert bearer_token, f"Did not find bearer token.  {msg}"
    assert query_id, f"Did not find query id.  {msg}"
    assert user_query_id, f"Did not find user query id.  {msg}"
    # get a guest token given a bearer token
    headers["authorization"] = f"Bearer {bearer_token}"
    guest_token_resp = send_request(GUEST_TOKEN_ENDPOINT, session.post, headers)
    guest_token = json.loads(guest_token_resp)["guest_token"]
    assert (
        guest_token
    ), f" Username {username} did not find guest token.  Script is broken.  {ISSUE}"
    headers["x-guest-token"] = guest_token

    if user_id := get_user_id(session, headers, user_query_id, username):
        variables["userId"] = user_id
    else:
        variables["userId"] = USERS[username]

    return query_id, session, headers, variables


def unit_test():
    """
    get ten latest tweets from a user with images
    """
    print("\033c")
    print(json.dumps(get_tweets("ffftechnology", 1), indent=4))

if __name__ == "__main__":

    unit_test()
