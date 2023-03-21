"""
 ╔════════════════════════════╗
 ║ ╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╗ ╔═╗╔╦╗ ║
 ║  ╠╣ ║║╠═╝╠╣ ╠═╣  ╠╩╗║ ║ ║  ║
 ║ ╚═╝╚╩╝╩  ╚  ╩ ╩  ╚═╝╚═╝ ╩  ║
 ╚════════════════════════════╝

Primary Event Loop

WTFPL litepresence 2021
"""

# STANDARD MODULES
import json
import time
from random import shuffle
from subprocess import call
from sys import argv
from threading import Thread

# 3DPFA MODULES
from config import (
    BOT_CHANNEL,
    CHANNELS,
    DAYS,
    DELAY,
    DEPLOY,
    DEPTH,
    DEV,
    FOLLOW,
    LOGO,
    MAIN_CHANNEL,
    MSG,
    PARROT,
    REPOST,
    RESTART,
    USERS,
    BAN_INTERVAL
)
from gun_detector import detect_gun, download
from json_ipc import json_ipc
from telegram_poster import channel_post, get_recent_posts
from tweet_extractor import get_tweets

# THIRD PARTY MODULES
from requests import get


def initialize_database():
    """
    initialize latest tweet id database
    """
    if RESTART:
        call("rm -r pipe".split())
        call("mkdir pipe".split())
    print("\033c")
    print(LOGO)
    print(time.time())
    latest_tweets = json_ipc("latest_tweets.txt")
    json_ipc("main_queue.txt", "[]")
    for user in USERS:
        if user not in latest_tweets:
            latest_tweets[user] = 1
        if "unix" not in latest_tweets:
            latest_tweets["unix"] = int(time.time()) - DAYS * 86400
    json_ipc("latest_tweets.txt", json.dumps(latest_tweets))


def edit_config(user, users):
    """
    edit the configuration file with the new user list
    create a concise updated user list to pass from scheduler to collector via ipc
    :param str(user): new user name to add to list
    :param list(users): old user list
    :return list(users): updated and sorted user list
    """
    users.append(user)
    users = sorted(set(users))
    # read config
    with open("./config.py", "r", encoding="utf-8") as handle:
        data = handle.read()
        handle.close()
    users_1 = data.split("USERS = ")[0]
    users_2 = json.dumps(users, indent=4)
    users_3 = data.split("USERS = ", maxsplit=1)[1].split("]", maxsplit=1)[1]
    users_tw = f"{users_1}# {time.ctime()} {user}\nUSERS = {users_2}{users_3}"
    # write to config
    with open("./config.py", "w", encoding="utf-8") as handle:
        data = handle.write(users_tw)
        handle.close()
    # provide updated user list to collector app
    json_ipc("users.txt", json.dumps(users))
    return users


def bannables():
    posts = list(set(get_recent_posts(max(BAN_INTERVAL+5, 200), BOT_CHANNEL)))
    for post in posts:
        print(post)
        if post.startswith("/ban"):
            banned = json_ipc("banned_users.txt", default="[]")
            banned.append(post.split("/ban ")[1])
            json_ipc("banned_users.txt", json.dumps(list(set(banned))))
        if post.startswith("/add"):
            users = json_ipc("users.txt", default="[]")
            users.append(post.split("/add ")[1])
            json_ipc("banned_users.txt", json.dumps(list(set(users))))


def scrape_reddit():
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language":"en-US,en;q=0.5",
        "Accept-Encoding":"gzip, deflate, br",
        "Referer":"https://duckduckgo.com/",
        "Cookie":"PHPSESSID=421a737e8472d0930c0599f28211772f",
    }
    data = get("https://www.reddit.com/r/fosscad/.rss", headers=headers).text
    data = ["https://www.reddit.com/r/fosscad/comments/" + "/".join(i.split("/")[1:3]) for i in data.split('fosscad/comments') if "www.w3.org" not in i]
    data = list(set(data))
    return data


def collector():
    """
    gather recent posts from each whitelisted twitter user containing images
    check if posts contain gun images and we have not posted it yet
    if so, upload to telegram
    """
    if DEV:
        channel_post(CHANNELS["threepn_bot"], "*** NEW SESSION **" + 3 * "*\n")

    collected_tweets = list(set(json_ipc("collected_tweets.txt", default="[]")))
    collected_images = list(set(json_ipc("collected_images.txt", default="[]")))

    n_posts = 0
    while True:
        print("\033c")
        print(LOGO)
        print(time.ctime())
        bannables()
        if DEPLOY:
            print("Collecting from reddit...")
            urls = scrape_reddit()
            print("done! found", len(urls), "posts.")
            for udx, url in enumerate(urls):
                if url not in collected_tweets:
                    channel_post(CHANNELS[BOT_CHANNEL], url)
                    collected_tweets.append(url)
                    json_ipc("collected_tweets.txt", json.dumps(collected_tweets))
                    time.sleep(DELAY)
                print(udx, "/", len(urls))
            collected_tweets = collected_tweets[-1000:]
        now = int(time.time())
        # fetch the database of most recent tweet id's for each user
        latest_tweets = json_ipc("latest_tweets.txt")
        users = list(USERS)
        # the scheduler process may have updated the user list
        users.extend(json_ipc("users.txt", default="[]"))
        users = list(set(users))
        shuffle(users)
        # iterate through whitelisted 3dpfa users on twitter
        for user in users:
            print("Checking if user", user, "is banned...")
            banned = json_ipc("banned_users.txt", default="[]")
            if user in banned:
                print("User", user, "is BANNED!")
                continue
            print("User is not banned!")
            try:
                print(time.ctime())
                print(f"Getting tweets from user `{user}`...")
                tweets = get_tweets(user, DEPTH)
                print(f"Found {len(tweets)} tweets!")
                # only consider tweets that have not been checked in the past
                tweets = [
                    tweet for tweet in tweets if int(tweet["id"]) > latest_tweets[user]
                ]
                print(f"Found {len(tweets)} latest tweets!")
                print([t["id"] for t in tweets])
                # iterate through the user's tweets
                for tweet in tweets:
                    tweet_id = int(tweet["id"])
                    # prevent duplicates
                    if tweet_id in collected_tweets:
                        print("tweet_id repeat")
                        continue

                    collected_tweets.append(tweet_id)
                    collected_tweets = collected_tweets[-1000:]
                    json_ipc("collected_tweets.txt", json.dumps(collected_tweets))

                    # update the latest tweet id for this user
                    if tweet_id > latest_tweets[user]:
                        latest_tweets[user] = tweet_id
                    # only consider recent tweets as defined by config DAYS
                    if tweet["unix"] > latest_tweets["unix"]:
                        print(f"{tweet} was recent enough!")
                        # check every image in the tweet for a gun
                        for image_url in tweet["images"]:
                            print(f"Checking tweet image url {image_url} for a gun...")
                            time.sleep(2)
                            # upon finding a gun in twitter post upload to telegram channel
                            (
                                is_gun,
                                hashed_img,
                                _,
                                _,
                                _,
                                _,
                            ) = detect_gun(download(image_url))
                            # if we've already seen this image break the loop
                            if hashed_img in collected_images:
                                print("hashed image repeat")
                                continue
                            # otherwise add the image to our collected images hashes
                            collected_images.append(hashed_img)
                            collected_images = collected_images[-1000:]
                            json_ipc(
                                "collected_images.txt", json.dumps(collected_images)
                            )
                            if is_gun:
                                print("Gun found!")
                                n_posts += 1
                                if n_posts % BAN_INTERVAL == 0:
                                    bannables()

                                ret = ""
                                if DEPLOY:
                                    ret = channel_post(
                                        CHANNELS[BOT_CHANNEL],
                                        tweet["url"].replace("/twitter", "/vxtwitter"),
                                    )
                                print("User:", user)
                                print("Tweet:\n", json.dumps(tweet, indent=4))
                                print("Image Url:", image_url)
                                print(ret)
                                print("\n\n")
                                time.sleep(DELAY)
                                break
            except Exception as e:
                print(e.args, e)

        # update the database
        latest_tweets["unix"] = now
        json_ipc("latest_tweets.txt", json.dumps(latest_tweets))
        time.sleep(900)


def scheduler():
    """
    queue, posted, and new are all web links from tgme_widget_message_link_preview

    queue: is client side cache database in json text file
    posted: links have recently been reposted to the main channel by bot or admin
    new: links have recently been forwarded to 3PN BOT; "whitelisted" by admin

    loop:
        add the pending to the queue; call this cache
        subtracting the already posted from the cache
        shuffle the cache and pop a post to post to the channel
        overwrite queue database with remaining cache
        wait
    """
    users = [u.lower() for u in USERS]
    json_ipc("users.txt", json.dumps(users))
    while True:
        try:
            # what the bot has posted AND
            # anything recently posted by external call
            posted = list(set(json_ipc("posted.txt", default="[]"))) 
            # the previous queue is in queue
            queue = list(set(json_ipc("main_queue.txt", default="[]")))
            print("1", queue)
            # anything recently whitelisted in the bot channel is new
            new = list(set(get_recent_posts(200, BOT_CHANNEL, post_type="whitelisted")))
            # any new new posts are added to those already in queue
            # any known to have been posted are removed
            print("1.5", new)
            queue.extend(new)
            queue = list({i for i in queue if i not in posted})
            shuffle(queue)
            # update the main queue database list
            json_ipc("main_queue.txt", json.dumps(queue))
            print("2", queue)
            time.sleep(1)
            # if anything remains in queue pop one off the list and post it
            if queue:
                this_post = queue.pop()
                # ensure the bot knows it just posted this
                posted.append(this_post) 
                # update the posted database list
                json_ipc("posted.txt", json.dumps(posted))
                # format a message with the post and boilerplate
                message = this_post + "\n\n" + MSG
                # extract and normalize the username
                user = this_post.split(".com/")[1].split("/status")[0].lower()
                if user not in users and "r/fosscad" not in user:
                    # announce the new user to main channel
                    message += f"\n\nFollowing New 3PN Gunsmith on Twitter: {user}"
                    # update and sort the user list
                    users = edit_config(user, users)
                # post this message to the main channel
                ret = channel_post(CHANNELS[MAIN_CHANNEL], message)
                if not ret["ok"]:
                    # If telegram says things are NOT ok, then try again and log
                    posted.pop(-1)
                    json_ipc("posted.txt", json.dumps(posted))
                    print("POSTING TO CHANNEL FAILED WITH ERROR:")
                    print(ret)
                    time.sleep(2)
                print(CHANNELS[MAIN_CHANNEL], message)
                # time.sleep(10)
            else:
                this_post = ""
                message = "WARN: NO POSTS IN QUEUE"
            # display bot status
            print("\033c")
            print("queue:\n", len(queue), queue)
            print("new:\n", len(new), new)
            print("posted:\n", len(posted), posted)
            print("message:\n", message)
            print(message)
            print(time.ctime())
            time.sleep(REPOST)
        except Exception as error:
            print(error.args)
            time.sleep(10)



def reposter(function):
    """
    post messages from one group of channels to another
    """
    print("reposter", function)
    if function == "parrot":
        rooms = PARROT
        endpoint = MAIN_CHANNEL
    elif function == "follow":
        rooms = FOLLOW
        endpoint = BOT_CHANNEL
    posted = []
    while True:
        bot_posts = get_recent_posts(200, CHANNELS[endpoint])
        for room in rooms:
            posts = get_recent_posts(50, CHANNELS[room])[-1]
            for post in posts:
                if post not in bot_posts and post not in posted:
                    posted.append(post)
                    channel_post(CHANNELS[endpoint], post)



def main():
    """."""

    if args := argv[1::]:
        dispatch = {
            "--scheduler": Thread(target=scheduler),
            "--collector": Thread(target=collector),
            "--parrot": Thread(target=reposter, args=("parrot",)),
            "--follow": Thread(target=reposter, args=("follow",)),
        }
        for arg in args:
            try:
                dispatch[arg].start()
            except KeyError:
                print(f"Invalid argument {arg}")
    else:
        initialize_database()
        # periodically posts to main channel
        scheduler_thread = Thread(target=scheduler)
        # collects images with ai from twitter
        collector_thread = Thread(target=collector)
        # reposts parrot telegram channels to main channel
        parrot_thread = Thread(target=reposter, args=("parrot",))
        # reposts follow telegram channels to bot channel
        follow_thread = Thread(target=reposter, args=("follow",))
        # start the threads concurrently
        scheduler_thread.start()
        parrot_thread.start()
        follow_thread.start()
        collector_thread.start()


if __name__ == "__main__":

    main()
