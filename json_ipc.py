"""
 ╔════════════════════════════╗
 ║ ╔═╗╔╦╗╔═╗╔═╗╔═╗  ╔╗ ╔═╗╔╦╗ ║
 ║  ╠╣ ║║╠═╝╠╣ ╠═╣  ╠╩╗║ ║ ║  ║
 ║ ╚═╝╚╩╝╩  ╚  ╩ ╩  ╚═╝╚═╝ ╩  ║
 ╚════════════════════════════╝

JSON IPC - Concurrent Interprocess Communication via Read and Write JSON

features to mitigate race condition:
    open file using with statement
    explicit close() in with statement
    finally close()
    json formatting required
    postscript clipping prevents misread due to overwrite without erase
    read and write to the text pipe with a single definition
    growing delay between attempts prevents cpu leak
to view your live streaming database, navigate to the pipe folder in the terminal:
    tail -F your_json_ipc_database.txt
:dependencies: os, traceback, json.loads, json.dumps
:warn: incessant read/write concurrency may damage older spinning platter drives
:warn: keeping a 3rd party file browser pointed to the pipe folder may consume RAM
:param str(doc): name of file to read or write
:param str(text): json dumped list or dict to write; if empty string: then read
:return: python list or dictionary if reading, else None

litepresence.com 2021
"""
# DISABLE SELECT PYLINT TESTS
# pylint: disable=broad-except, too-many-branches, too-many-statements
#
# STANDARD PYTHON MODULES
import os
import time
import traceback
from json import dumps as json_dumps
from json import loads as json_loads


def json_ipc(doc="", text="", initialize=False, default="[]"):
    """
    JSON IPC
    Concurrent Interprocess Communication via Read and Write JSON
    features to mitigate race condition:
        open file using with statement
        explicit close() in with statement
        finally close()
        json formatting required
        postscript clipping prevents misread due to overwrite without erase
        read and write to the text pipe with a single definition
        growing delay between attempts prevents cpu leak
    to view your live streaming database, navigate to the pipe folder in the terminal:
        tail -F your_json_ipc_database.txt
    :dependencies: os, traceback, json.loads, json.dumps
    :warn: incessant read/write concurrency may damage older spinning platter drives
    :warn: keeping a 3rd party file browser pointed to the pipe folder may consume RAM
    :param str(doc): name of file to read or write
    :param str(text): json dumped list or dict to write; if empty string: then read
    :return: python list or dictionary if reading, else None
    wtfpl2020 litepresence.com
    """
    # initialize variables
    data = default
    msg = "writing"
    tag = "<<< JSON IPC >>>"
    # determine where we are in the file system; change directory to pipe folder
    path = f"{os.path.dirname(os.path.abspath(__file__))}/pipe"
    # ensure we're writing json then add prescript and postscript for clipping
    text = tag + json_dumps(json_loads(text)) + tag if text else text
    # create the pipe subfolder
    if initialize:
        os.makedirs(path, exist_ok=True)
    if doc:
        doc = f"{path}/{doc}"
        # race read/write until satisfied
        iteration = 0
        while True:
            time.sleep(0.01 * iteration ** 2)
            try:
                if text:
                    # write to file operation
                    with open(doc, "w+") as handle:
                        handle.write(text)
                        handle.close()
                        break
                else:
                    msg = "reading"
                    # read from file operation
                    try:
                        with open(doc, "r") as handle:
                            # only accept legitimate json
                            data = json_loads(handle.read().split(tag)[1])
                            # print(data)
                            handle.close()
                            break
                    except FileNotFoundError:
                        data = json_loads(default)
                        with open(doc, "w+") as handle:
                            handle.write(tag + json_dumps(json_loads(default)) + tag)
                            handle.close()
                            break
            except Exception:
                if iteration == 1:
                    print(  # only if it happens more than once
                        f"{iteration}: json_ipc race condition while {msg} {doc}\n",
                    )
                elif iteration == 5:
                    print(traceback.format_exc())
                continue
            # deliberately double check that the file is closed
            finally:
                try:
                    handle.close()
                except Exception:
                    pass
            iteration += 1
    return data

