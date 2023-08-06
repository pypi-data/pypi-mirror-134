Investing world indices is a python library to scrape world indices from investing.com, using browser automation. 
It currently runs only on windows.

## World Indices Scraper
In this, we first import library to scrape world indices.
```sh
from investing_world_indices_scraper import *
response = investing.com_world_indices()
```

### Response Data
```json
        "stock_name": "Dow Jones",
        "stock_link": "/indices/us-30",
        "last_price": "36.67%",
        "change": "+183.15",
        "change_percent": "+0.51%",
        "adv.": "19",
        "dec.": "11"
```


#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which investing website will be loaded and scrapes the data from the website.


### Installation

```sh
pip install investing-world-indices-scraper
```

### Import
```sh
from investing_world_indices_scraper import *
```

### Get World Indices Data
```sh
response = investing.com_world_indices()
data=response['body']
```

### Run bot on cloud
You can run bot on [Cloud](https://datakund.com/products/investing-com-world-indices-scraper).

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

