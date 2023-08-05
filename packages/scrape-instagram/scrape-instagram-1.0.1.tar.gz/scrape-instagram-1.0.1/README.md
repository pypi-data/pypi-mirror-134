Instagram search scraper is a python library to scrape for a instagram search profile, followers, posts etc. using browser automation. 
It currently runs only on windows.

### Example 1 : Instagram scraper to scrape profile, followers, posts, etc. using url link
In this example we first import library, then provide the instagram url to be scraped instead of "url" provided.
```sh
from scrape_instagram import *
response =instagram.profile_scraper(profile_link="url")
#response = {
#  "body": {
#      "profile_name": "ashliemolstad",
#      "posts": "5,259",
#      "followers": "213k",
#      "following": "1,098",
#      "bio": "Life Coach & Podcast Host @youcansipwithus \u2063\u2063Passionate about helping women live a life they love, without waiting on the.....",
#      "followed_by": "1,098"
#    },........]}

```

### Example 2 : Instagram scraper to scrape comments using url link
In this example we first import library, then provide the instagram url to be scraped instead of "url" provided.
```sh
from scrape_instagram import *
response =instagram.comment_scrape(url_link="url")
#response = {
#  "body": {
#      {
#        "title": "__vineetha_",
#        "comment": "Now, don't touch it."
#      },....]}

```



#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product will be bought. To buy first login will need to be done. Login can be done either with credentials or via cookies


### Installation

```sh
pip install scrape-instagram
```

### Import
```sh
from scrape-instagram import *
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

