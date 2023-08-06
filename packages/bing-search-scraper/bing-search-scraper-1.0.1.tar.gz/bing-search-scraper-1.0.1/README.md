Bing search scraper is a python library to scrape for a bing search result using browser automation. 
It currently runs only on windows.

## Scrape Search Results
We first import library, then provide the keyword to be scraped instead of "dog" provided.
```sh
from bing_search_scraper import *
response=bing.search_result_scraper(q="dog")
```
### Response Data
```json
     "description": "or domestic dog, (Canis familiaris   or Canis lupus familiaris ) is a domesticated descendant of the wolf which is characterized by an upturning tail.",
     "link": "https://en.wikipedia.org/wiki/Dog",
     "title": "Dog - Wikipedia"
```

#### Bot Studio
[Bot_Studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product will be bought. To buy first login will need to be done. Login can be done either with credentials or via cookies


### Installation

```sh
pip install bing-search-scraper
```

### Import
```sh
from bing-search-scraper import *
```

### Run bot on cloud
You can run bot on [Cloud](https://datakund.com/products/bing-search-result-scraper-1?_pos=1&_sid=6dbce9525&_ss=r).

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

