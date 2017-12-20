# python 3
import subprocess
import time

import requests
import pyperclip  # The name you have the file


def check404(link):
    # time.sleep(1)  # delays for 1  seconds. You can Also Use Float Value.

    link = 'https://truyenyy.com' + link

    print("******** checking {}".format(link))

    try:

        r = requests.get(link)

        # print (r.content)
        if r.content.find(b"url.value = window.location.href") > 0:
            with open("error.txt", "a") as myfile:
                myfile.write('\n\r')
                myfile.write(link)

    except Exception as e:
        with open("error.txt", "a") as myfile:
            myfile.write('\n\r {}'.format(e))
            myfile.write(link)

        # print('Error: {}'.format(link))


def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data


def get_links_from_file():
    # f = open('links.txt', 'r')
    with open('links.txt') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


def readlinks():
    r = input('Please paste all links in links.txt (line by line, e.g: /truyen-sac-hiep/ ) then press enter, error links will be in error.txt')

    links = get_links_from_file()
    r = input('Total links are {} . Press enter to continue!'.format(len(links)))

    return links  # .split(b'\n')#.split(b'\n')


# check404(b'/doc-truyen/vu-dong-can-khon/chuong-567/\n\n/doc-truyen/thieu-gia-bi-bo-roi/chuong-8/')

links = readlinks()
i = 1
for link in links:
    i += 1
    print(i)
    check404(link)
