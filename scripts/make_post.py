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

post = make_post_path(year+month+day+'.md')

while os.path.exists(post):
    print(f'Post {post} already exists. Please provide differentiating suffix:')
    suffix = input()
    post = make_post_path(f'{year}{month}{day}_{suffix}.md')

content = f"""---
date: {year}-{month}-{day}
categories:
tags:
authors:
---
"""

with open(post, 'w') as f:
    f.write(content)

print(f'New blog post initialized at {post}')
