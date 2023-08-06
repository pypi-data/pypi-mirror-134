# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reddist', 'reddist.cachers', 'reddist.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles==0.6.0', 'aioredis>=2.0.1,<3.0.0', 'asyncpraw>=7.5.0,<8.0.0']

setup_kwargs = {
    'name': 'reddist',
    'version': '0.1.2',
    'description': 'Just a simple library for caching reddit posts',
    'long_description': '# Reddist\n\nJust a python library to make reddit post caching easier.\n\n\n## Caching Options\n1. In Memory Caching\n2. Redis Caching\n3. Pickle Caching\n\n## Usage\n\n### Installation:\n\n- Developement\n```sh\npoetry add git+https://github.com/CaffeineDuck/reddist\n```\n\n- Stable\n```sh\npoetry add reddist\n```\n\n### Pickle Usage:\n\n```py\nimport asyncio\nimport random\nfrom dataclasses import asdict\n\nasync def main():\n    reddit_cacher = PickleRedditCacher(\n            Reddit(\n                user_agent="dpydit",\n                client_id="CLIENT_ID",\n                client_secret="CLIENT_SECRET",\n            ),\n            \'cache.pickle\',\n            cached_posts_count=100,\n        )\n\n    reddit_cacher.start_caching()\n    posts = await reddit_cacher.get_subreddit_posts("pics")\n    print(asdict(random.choice(posts)))\n\nif __name__ == "__main__":\n    loop = asyncio.get_event_loop()\n    loop.run_until_complete(main())\n```\n\n### Memory Usage:\n\n```py\nimport asyncio\nimport random\nfrom dataclasses import asdict\n\nasync def main():\n    reddit_cacher = MemoryRedditCacher(\n            Reddit(\n                user_agent="dpydit",\n                client_id="CLIENT_ID",\n                client_secret="CLIENT_SECRET",\n            ),\n            cached_posts_count=100,\n        )\n\n    reddit_cacher.start_caching()\n    posts = await reddit_cacher.get_subreddit_posts("pics")\n    print(asdict(random.choice(posts)))\n\nif __name__ == "__main__":\n    loop = asyncio.get_event_loop()\n    loop.run_until_complete(main())\n```\n\n### Redis Usage:\n\n```py\nimport asyncio\nimport random\nfrom dataclasses import asdict\n\nimport aioredis\n\nasync def main():\n    redis = aioredis.from_url(\n        "redis://localhost"\n    )\n    async with redis.client() as conn:\n        reddit_cacher = RedisRedditCacher(\n            Reddit(\n                user_agent="dpydit",\n                client_id="CLIENT_ID",\n                client_secret="CLIENT_SECRET",\n            ),\n            conn,\n            cached_posts_count=100\n        )\n        posts = await reddit_cacher.get_subreddit_posts("pics")\n        print(asdict(random.choice(posts)))\n\nif __name__ == "__main__":\n    loop = asyncio.get_event_loop()\n    loop.run_until_complete(main())\n```\n\n## WIP (Expect Breaking Changes)',
    'author': 'CaffieneDuck',
    'author_email': 'samrid.pandit@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
