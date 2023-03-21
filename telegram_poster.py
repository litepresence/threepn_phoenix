"""
 ╔════════════════════════════╗
 ║ ╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╗ ╔═╗╔╦╗ ║
 ║  ╠╣ ║║╠═╝╠╣ ╠═╣  ╠╩╗║ ║ ║  ║
 ║ ╚═╝╚╩╝╩  ╚  ╩ ╩  ╚═╝╚═╝ ╩  ║
 ╚════════════════════════════╝

Telegram Poster

WTFPL litepresence 2021
"""

# STANDARD MODULES
import time

# THIRD PARTY MODULES
import requests

# 3DPFA MODULES
from config import BOT_CHANNEL, CHANNELS, MAIN_CHANNEL, TOKEN


def channel_post(channel, message):
    """
    post a message to telegram
    """
    time.sleep(2)
    endpoint = "/sendMessage"
    params = {
        "chat_id": channel,
        "text": message,
        "Markdown": True,
    }
    url = f"https://api.telegram.org/bot{TOKEN}{endpoint}"
    return requests.get(url, params=params).json()


def get_raw_data(room, post_id):
    """
    make an external request to telegram's web preview
    for one room at some post_id in history
    returns html for up to 20 posts counting back in time from post_id
    """
    url = f"https://t.me/s/{room}/{post_id}"
    print(url)
    time.sleep(2)
    return requests.get(url).text



def get_latest_data_raw(room):
    """
    returns html from the 10 most recent posts
    """
    return get_raw_data(room, 99999999999)


def get_last_post_number(room):
    """
    count of highest post number from a room
    """
    ret = get_latest_data_raw(room)
    return int(
        ret.split(f'<a class="tgme_widget_message_date" href="https://t.me/{room}/')[
            1
        ].split('">')[0]
    )


def get_posts_from(room, post_id):
    """
    last 20 of all tgme_widget_message_link_preview
    """
    ret = get_raw_data(room, post_id)
    posts = ret.split('<div class="tgme_widget_message_text js-message_text" dir="auto">')
    posts = [
        i.split('>')[0].split('" target="_blank"')[0][9:]
        if "http://" in i.split(">")[0] or "https://" in i.split(">")[0]
        else i.split(">")[0][:-5]
        for i in posts
    ]

    # print(posts)
    posts.pop(0)
    return posts


def get_forwards_from(room, post_id):
    """
    last 20 of all tgme_widget_message_link_preview's that have been forwarded
    """
    try:
        ret = get_raw_data(room, post_id)
        # print(ret)
        posts = ret.split("tgme_widget_message_forwarded_from")
        posts = [i.split("</time>")[0] for i in posts]
        posts.pop(0)
        posts = [i for i in posts if "_name" in i]
        posts = [
            i.split('<a class="tgme_widget_message_link_preview" href="')[1] for i in posts
        ]
        posts = [i.split('">')[0] for i in posts]
    except:
        posts = []
    return posts


def get_recent_posts(depth, room, post_type="all"):
    """
    scan through last depth of posts from a room
    return all of them
    (or only forwarded messages; "whitelisted")
    """
    if post_type == "all":
        get_posts_by_type = get_posts_from
    elif post_type == "whitelisted":
        get_posts_by_type = get_forwards_from
    last_post = get_last_post_number(room)
    print(room, "last post number", last_post)
    recent_posts = []
    for i in range(last_post - depth, last_post + 40, 19):
        if i > 0:
            latest_posts = get_posts_by_type(room, i)
            recent_posts.extend(latest_posts)
            recent_posts = sorted(list(set(recent_posts)))
            # print(i, json.dumps(recent_posts, indent=4))
    return recent_posts


def backup(id_from, id_to):
    """
    backup all "from" links in the "to" room
    """
    for message in get_all_posts(id_from):
        channel_post(id_to, message)


def get_all_posts(room):
    """
    make several calls to get the latest post number and all posts up to that number
    """
    return get_recent_posts(get_last_post_number(room), room)


def unit_test():
    """
    backup the main channel to the bot channel
    """
    backup(CHANNELS[MAIN_CHANNEL], CHANNELS[BOT_CHANNEL])


if __name__ == "__main__":

    unit_test()
