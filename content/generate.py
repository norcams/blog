#!/usr/bin/env python
"""
Generates random articles containing loremipsum to
test Pelican site generation.

Requires the loremipsum Python module:

    pip install loremipsum


This work is licensed under a Creative Commons
Attribution-ShareAlike 3.0 Unported License.

http://creativecommons.org/licenses/by-sa/3.0/deed.en_GB

Copyright 2013 James Brotchie <brotchie@gmail.com>, @brotchie

"""

from loremipsum import get_sentence, get_paragraph, get_paragraphs
from random import randint, sample

TAGS = ['matlab', 'python', 'open source']
AUTHOR = 'Firstname Lastname <example@example.com>'

randyear  = lambda: randint(2013, 2015)
randmonth = lambda: randint(1, 12)
randday   = lambda: randint(1, 28)

randtitle = lambda: get_sentence(False)
randsummary = lambda: get_paragraph(False)
randtag = lambda: sample(TAGS, 1)[0]
randcontent = lambda: '\n\n'.join(get_paragraphs(randint(3,4)))

def generate_date():
    return '{}-{:02}-{:02}'.format(randyear(), randmonth(), randday())

def generate_article():
    title = randtitle()
    slug = title.replace('.', '').replace(' ', '-')
    info = dict(
        title=title,
        slug=slug,
        date=generate_date(),
        tags=randtag(),
        author=AUTHOR,
        summary=randsummary()
    )

    return ('\n'.join('{}: {}'.format(k.capitalize(), v) for k,v in info.iteritems()) + '\n\n' + randcontent(), slug)

def main():
    for i in range(16):
        (content, slug) = generate_article()
        file(slug + '.md', 'w+').write(content)

if __name__ == '__main__':
    main()
