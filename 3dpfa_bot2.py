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
from traceback import print_exc

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
)
from gun_detector import detect_gun, download
from json_ipc import json_ipc
from telegram_poster import channel_post, get_recent_posts, get_last_post_number
from tweet_extractor import get_tweets
from youtube_extractor import get_vids as get_tubes


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
    latest_tubes = json_ipc("latest_tubes.txt")
    json_ipc("main_queue.txt", "[]")
    for user in USERS:
        if user not in latest_tweets:
            latest_tweets[user] = 1
        if "unix" not in latest_tweets:
            latest_tweets["unix"] = int(time.time()) - DAYS * 86400
    json_ipc("latest_tweets.txt", json.dumps(latest_tweets))

    json_ipc("latest_tubes.txt", json.dumps(latest_tubes))


def collector():
    """
    gather recent posts from each whitelisted twitter user containing images
    check if posts contain gun images and we have not posted it yet
    if so, upload to telegram
    """
    if DEV:
        channel_post(CHANNELS["test"], "*** NEW SESSION **" + 3 * "*\n")
    posted_tubes = []
    hashed_images = []
    while True:
        print("\033c")
        print(LOGO)
        print(time.ctime())
        now = int(time.time())
        # fetch the database of most recent tweet id's for each user
        print("fetching previous posts and users... (note, if this hangs, check json_ipc)")
        posted_tubes = json_ipc("posted_tubes.txt", default="[]")
        users = json_ipc("tubers.txt", default='["3d printed gun"]')
        if "3d printed gun" not in users:
            users.append("3d printed gun")
        print("done initializing")
        shuffle(users)

        try:
            print(time.ctime())
            for user in users:
                print("Getting latest tubes with search term", user)
                tubes = get_tubes(5, user)
                print(f"Found {len(tubes)} tubes!")
                print([t["id"] for t in tubes])
                # iterate through the user's tubes
                for tube in tubes:
                    tube_id = tube["id"]
                    # prevent duplicates
                    if tube_id in posted_tubes:
                        print("tube_id repeat")
                        continue

                    posted_tubes.append(tube_id)
                    posted_tubes = posted_tubes[-1000:]
                    json_ipc(
                        "posted_tubes.txt", json.dumps(posted_tubes)
                    )
                    image_url = tube["images"]
                    print(f"Checking tube image url {image_url} for a gun...")
                    time.sleep(2)
                    # upon finding a gun in twitter post upload to telegram channel
                    (is_gun, hashed_img, _, _, _, _,) = detect_gun(
                        download(image_url), use_meme=False
                    )
                    if hashed_img in hashed_images:
                        print("hashed image repeat")
                        continue
                    hashed_images.append(hashed_img)
                    hashed_images = hashed_images[-1000:]
                    json_ipc(
                        "collected_images.txt", json.dumps(hashed_images)
                    )
                    if is_gun:
                        print("Gun found!")

                        ret = ""
                        if DEPLOY:
                            ret = channel_post(
                                CHANNELS["test"],
                                tube["url"],
                            )
                        print("tube:\n", json.dumps(tube, indent=4))
                        print("Image Url:", image_url)
                        print(ret)
                        print("\n\n")
                        time.sleep(DELAY)
        except Exception as e:
            print(e.args, e)
            print_exc()
        print("loop finished, waiting 30mins for more posts")
        time.sleep(1800)


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
    posted = []
    while True:
        try:
            # what the bot has posted AND
            # anything recently posted by external call
            posted = list(
                set(posted + get_recent_posts(200, MAIN_CHANNEL, post_type="all"))
            )
            # the previous queue is in queue
            queue = list(set(json_ipc("main_queue.txt", default="[]")))
            # anything recently whitelisted in the bot channel is new
            new = list(
                set(get_recent_posts(200, BOT_CHANNEL, post_type="whitelisted"))
            )
            # queue is then updated:
            # any new new posts are added to those already in queue
            # any known to have been posted are removed
            # /vx  will allow for autoplay of video content in telegram
            queue.extend(new)
            queue = list(
                {
                    i.replace("/twitter", "/vxtwitter")
                    for i in queue
                    if i not in posted
                }
            )
            # get the most recent post number in the main rooom:
            last_post = get_last_post_number(MAIN_CHANNEL)
            # format a message to post in the main channel
            msg = f"{MSG.split('/t.me/s/')[0]}/t.me/s/{MAIN_CHANNEL}/{last_post + 1}"
            # shuffle the queue
            shuffle(queue)
            # if anything remains in queue pop one off the list and post it
            if queue:
                this_post = queue.pop()
                # ensure the bot knows it just posted this
                posted.append(this_post)
                # format a message with the post and boilerplate
                message = this_post + "\n\n" + msg
                # extract and normalize the username
                user = this_post.split(".com/")[1].split("/status")[0].lower()
                if user not in users:
                    # announce the new user to main channel
                    message += f"\n\nFollowing New 3PN Gunsmith on Twitter: {user}"
                    # update and sort the user list
                    users.append(user)
                    users = sorted(set(users))
                    # edit the configuration file with the new user list
                    with open("./config.py", "r", encoding="utf-8") as handle:
                        data = handle.read()
                        handle.close()
                    users_1 = data.split("USERS = ")[0]
                    users_2 = json.dumps(users, indent=4)
                    users_3 = data.split("USERS = ", maxsplit=1)[1].split("]", maxsplit=1)[1]
                    users_tw = f"{users_1}# {time.ctime()} {user}\nUSERS = {users_2}{users_3}"
                    with open("./config.py", "w", encoding="utf-8") as handle:
                        data = handle.write(users_tw)
                        handle.close()
                    # edit the inter process communication file with the new user list
                    json_ipc("users.txt", json.dumps(users))
                channel_post(CHANNELS[MAIN_CHANNEL], message)
            else:
                this_post = ""
                message = ""
            # either way update the queue with the latest queue
            json_ipc("main_queue.txt", json.dumps(queue))
            print("\033c")
            print("last post", last_post)
            print("queue:\n", len(queue), queue)
            print("new:\n", len(new), new)
            print("posted:\n", len(posted), posted)
            print("message:\n", message)
            print(message)
            print(time.ctime())
            time.sleep(REPOST)
        except:
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
    """

    """

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
