"""Copy and paste using the internet"""

__version__ = '0.1'

import argparse

import pyperclip as clipboard
import requests
from bs4 import BeautifulSoup
from colorama import Fore


def create_clip(l, m, u):
    """Create clip """
    url = u + l
    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, 'html.parser')
    clipContent = soup.find("div", {"id": "cl1pContent"})
    if clipContent is not None:
        action = soup.find("input", {"name": "action"})['value'].strip()
        pageHash = soup.find("input", {"name": "pageHash"})['value'].strip()
        seqHash = soup.find("input", {"name": "seqHash"})['value'].strip()

        data = {'content': m,
                'action': action,
                'pageHash': pageHash,
                'seqHash': seqHash}

        r = requests.post(url=url, data=data)
        pastebin_url = r.text
        print("")
        print(Fore.BLUE + "The cl1p URL is : %s" % url)
        print("")

    else:
        print("")
        print(Fore.RED + "" + url + " is already in use please use different url . Use \'-l\' flag to specify url ")
        print("")


def get_clip(l, c, u):
    """get clip from cl1p.net"""
    url = u + l
    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, 'html.parser')
    contentRead = soup.find("div", {"class": "contentRead"})
    if contentRead is not None:
        textContetnt = soup.find("textarea", {"name": "content"})
        if c:
            clipboard.copy(textContetnt.text)
            print("")
            print(Fore.BLUE + "Content copied to clipboard")
            print("")
        else:
            print(" ")
            print(Fore.BLUE + "*************************************")
            print(Fore.BLUE + "\t\tClip data")
            print(Fore.BLUE + "*************************************")
            print(Fore.RESET + "")
            print(textContetnt.text)
            print(" ")
    else:
        print("  ")
        print(Fore.RED + "No clip is present at " + url + ".")
        print("  ")


def run():
    parser = argparse.ArgumentParser(
        description="cl1p.net lets you move information between computers using your internet")
    parser.add_argument("-c", "--c",
                        action='store_true',
                        help='Copy clip content directly to clipboard',
                        required=False)
    parser.add_argument("-d", "--d",
                        action='store_true',
                        help='Create clip directly from clipboard',
                        required=False)
    parser.add_argument("-l", "--l",
                        action='store',
                        help='Set link to clipboard name',
                        type=str,
                        required=True)
    parser.add_argument("-m", "--m",
                        action='store',
                        help='Set clip message',
                        type=str,
                        required=False)
    parser.add_argument("-u", "--url",
                        action='store',
                        default='https://cl1p.net/'
                        help='Set backend URL',
                        type=str,
                        required=False)
    args = parser.parse_args()
    if args.m is not None:
        create_clip(args.l, args.m, args.u)
    elif args.d:
        text = clipboard.paste()
        create_clip(args.l, text, args.u)
    else:
        get_clip(args.l, args.c, args.u)


if __name__ == '__main__':
    run()
