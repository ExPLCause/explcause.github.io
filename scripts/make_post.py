import datetime
import os
import yaml

with open('mkdocs.yml', 'r') as stream:
    meta = yaml.load(stream, Loader=yaml.Loader)

today = datetime.datetime.today()
year  = str(today.year)
month = str(today.month).zfill(2)
day   = str(today.day).zfill(2)

def make_post_path(fname):
    return os.path.sep.join([
        meta['docs_dir'],
        [p['blog'] for p in meta['plugins'] if 'blog' in p][0]['blog_dir'],
        'posts',
        fname])

print(f'Short title (this will be appended to the date as the file name):')
shorttitle = input()

post = make_post_path(f'{year}{month}{day}{"_" + shorttitle if shorttitle else ""}.md')

while os.path.exists(post):
    print(f'Post {post} already exists. Please provide differentiating suffix:')
    shorttitle = input()
    post = make_post_path(f'{year}{month}{day}_{shorttitle}.md')

print(f'Full title:')
title = input()

content = f"""---
date: {year}-{month}-{day}
title: {title}
categories:
tags:
authors:
---
"""

with open(post, 'w') as f:
    f.write(content)

print(f'New blog post initialized at {post}')
