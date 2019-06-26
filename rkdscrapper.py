# -*- coding: utf-8 -*-
"""Do install
!pip install unsync==1.2
!pip install aiohttp==3.5.4
!pip install aiofiles==0.4.0
"""

from urllib.request import urlopen
import json
import aiohttp
import aiofiles
from unsync import unsync
import asyncio
from fastprogress import progress_bar
import os
import sys

nums = json.loads(
    urlopen((
        f'https://api.rkd.nl/api/search/images?filters[iconclass_code]=73*&format=json&language=en&filters[periode]=1400||1735&fieldset=detail&start=0'
    )).read().decode('utf-8'))['response']['numFound']
data = []
os.mkdir('images')


@unsync
async def download_images(task):
    im, id = task.result()
    async with aiohttp.ClientSession() as session:
        url = f'https://images.rkd.nl/rkd/thumb/650x650/{im}.jpg'
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f'images/{id}.jpg', mode='wb')
                await f.write(await resp.read())
                await f.close()


@unsync
async def get_info(offset):
    url = f'https://api.rkd.nl/api/search/images?filters[iconclass_code]=73*&format=json&language=en&filters[periode]=1400||1735&fieldset=detail&start={offset}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                q = await resp.json()
                return q['response']['docs'][0]


@unsync
def extract(task):
    resp = task.result()
    imgl = resp['picturae_images'][-1]
    permalink = resp['permalink']
    q = [st.split('@') for st in resp['iconclass_tekst_search']]
    id = permalink.rsplit('/', 1)[-1]
    for sq in q:
        t, c = sq
        if c.startswith('73'):
            data.append((c, t, imgl, permalink, id))  # keeping it at 1NF
    return imgl, id


pgb = progress_bar(range(nums))
tasks = [get_info(i).then(extract).then(download_images).result() for i in pgb]
df = pd.DataFrame(
    data, columns=["Iconclass", "Text", "Download-Hash", "Permalink", "Id"])
<<<<<<< Updated upstream
df.to_csv("rkd_keys.csv")

=======
df.to_csv("rkd_keys.csv")
>>>>>>> Stashed changes
