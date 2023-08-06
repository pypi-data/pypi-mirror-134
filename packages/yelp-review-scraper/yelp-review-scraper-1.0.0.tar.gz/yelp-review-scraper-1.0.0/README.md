


Yelp Review Scraper is a python library to scrape yelp reviews, using browser automation. 
It currently runs only on windows.

## Scrape Yelp Reviews
* In this example we first import library, then we fetched data using simple function. 
* Replace **"url"** with **"yelp product url"**.

```json
from yelp_review_scraper import *
response=yelp.review(yelp_link="url")
```
### Response Data
```json
      "review_by": "Eimi O.",
      "address": "Laurel Heights, San Francisco, CA",
      "reviewed": "0",
      "review": "My partner and I LOVE saffron grill. We used to order takeout from them at least twice a month (and the only reason why we stopped is bc we left sf). It was probably our favorite place in the city. To this day I've never had a better fish masala. When/if we ever come back to sf, we're coming for ya first thing, Saffron Grill! \u00a0sincerely, your biggest fans",
      "date": "12/21/2021"
```


#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which it first logins twitter and then scrapes twitter followers.

#### Installation
```sh
pip install yelp-review-scraper
```

#### Import
```sh
from yelp_review_scraper import *
```
#### Get Yelp Reviews
```sh
yelp.review(yelp_link="url")
```

#### Run bot on cloud
You can run bot on [cloud](https://datakund.com/products/yelp-review?_pos=2&_sid=3ef0d8047&_ss=r).

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

