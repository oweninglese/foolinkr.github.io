#! /usr/bin/python

import fileinput
import frontmatter as fm
from datetime import date
import os

artdir = '/mastervault/'
TAGS: str = ''
tfile = 'TAGS.csv'
base_dir = os.path.abspath(os.path.dirname(__file__))
arts = base_dir + artdir


def check_file(file, tag, folder=''):
    """
    cheek single file for single tag
    """
    print(f"Checking :  {tag}")
    for line in fileinput.input(folder + file, inplace=True):
        if line.filelineno() < 9:
            continue
        line = line.replace(tag, "[[" + tag + "]]")
        print(line, end='')


def load_folder(artdir):
    """ load all md in TESTDIR and append Post object to files dict list
Args:
    TESTDIR (folder): folder containing md files
Returns:
    list: [list of dicts] --> [filename]: [Post object]"""
    for filename in os.listdir(arts):
        if filename.endswith(".md"):
            afile = filename
            post = fm.load(arts + afile)
            post['author'] = 'ohmanfoo'
            post['source'] = '#todo'
            post['tags'] = ''
            post['created'] = str(date.today())
            post['title'] = afile
            with open(arts + afile, 'w') as text:
                text.write(fm.dumps(post))


def art():
    return 'British North America and a Continent in Dissolution.md'


afile = art()

# print(i)


def check_tags(afile, tag):
    post = fm.load(arts + afile)
    if tag in post.content:
        post['tags'] += f"#{tag} "
        with open(afile, 'w') as text:
            text.write(fm.dumps(post))
            with open(tfile, "r") as tagfile:
                j = tagfile.read()
                h = j.split(",")
                for i in h:
                    check_file(text, i, arts)


load_folder(artdir)
with open(tfile, "r") as tagfile:
    j = tagfile.read()
    h = j.split(",")
    for i in h:
        check_tags(afile, i)
