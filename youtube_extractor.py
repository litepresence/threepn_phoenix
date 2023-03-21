# _*_coding: utf-8_*_

from json_ipc import json_ipc
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import json
from traceback import print_exc

def get_vids(n_posts=10, username="3d printed guns"):
    posts = []
    ret = get_data(int(n_posts), username)
    for url in ret:
        n_post = {
            "id": ret[url][2],
            "unix": ret[url][1],
            "images": ret[url][0],
            "url": url,
        }
        posts.append(n_post)
    print(posts)
    return posts


def get_data(pages=1, search="3d printed guns"):
    op = Options()
    op.add_argument("--headless")
    # start web browser
    browser = webdriver.Firefox(options=op)

    vids = {}

    # get source code
    browser.get(
        f"https://www.youtube.com/results?search_query={search.replace(' ', '+')}&sp=CAISBAgEEAE%253D"
    )
    print("loading youtube...")
    for h in range(0, 1000 * pages, 1000):
        browser.execute_script(f"window.scrollTo(0,{h})")
        time.sleep(2)
        html = browser.page_source

        for i in html.split("<ytd-video-renderer")[1:-1:]:
            try:
                # extract the url for the video
                url = (
                    "www.youtube.com"
                    + i.split("yt-simple-endpoint inline-block style-scope ytd-thumbnail")[
                        1
                    ]
                    .split("href=")[1]
                    .split(">")[0][1:-1]
                )
                if "shorts" in url:
                    continue
                # extract the unix time
                user = (
                    i.split(
                        '<div id="tooltip" class="hidden style-scope tp-yt-paper-tooltip" style-target="tooltip">'
                    )[1]
                    .strip("\n ")
                    .split("\n")[0]
                )
                user_handle = (
                    i.split(
                    '<a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/@'
                    )[1]
                    .split('" dir="auto"')[0]
                )

                print(user, user_handle)

                users = json_ipc("tubers.txt", default="[]")

                users.append(user_handle)
                users = list(set(users))[-1000:]
                json_ipc("tubers.txt", json.dumps(users))



                agos = (
                    i.split(
                        '<yt-formatted-string class="style-scope ytd-video-renderer" aria-label="'
                    )[1]
                    .split('">')[0]
                    .split(f"by {user}")[1]
                    .split("views")[0]
                    .split()[:2]
                )
                if agos[0] == "Streamed":
                    # FIXME: There should be SOME way to deal with these
                    continue
                    # print(agos)
                    # agos.pop(0)
                ago_lookup = {
                    "seconds": 1,
                    "minutes": 60,
                    "hours": 3600,
                    "days": 86400,
                    "weeks": 86400 * 7,
                    "months": 86400 * 30,
                    "years": 86400 * 365,
                }
                # Allow for indexing with and without 's', i.e. 'days' or 'day'
                for k, v in ago_lookup.copy().items():
                    ago_lookup[k[:-1]] = v
                ago = (
                    int(agos[0])
                    * ago_lookup[agos[1]]
                )
                unix = time.time() - ago
                # extract the thumbnail image
                try:
                    img = (
                        i.split("<img")[1].split('src="')[1].split('"')[0].split(".jpg?")[0]
                        + ".jpg"
                    )
                except Exception as e:
                    continue
                # add the video with thumbnail and timestamp to the dict
                vids[url] = [img, unix, url.split("?v=")[1]]
                print("found video! url:", url)
            except Exception as e:
                print(e)
                print_exc()
    # close web browser
    browser.close()
    return vids


if __name__ == "__main__":
    print(json.dumps(get_vids(10), indent=4))
