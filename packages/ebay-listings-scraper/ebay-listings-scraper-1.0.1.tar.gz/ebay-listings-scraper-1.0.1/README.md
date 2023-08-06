eBay listing scraper is a python library to scrape for a eBay listings(listing title, rating, condition, price, shipping and listing link), Using browser automation. 
It currently runs only on windows.

### Scrape eBay Listings
 * In this example we first import library, then we fetched data using simple function.
 * Replace **"mobiles"** with **"your keyword"**.

```sh
from ebay_listings_scraper import *
response =ebay.listings_scraper(Search_for_anything="mobiles")
```

### Response Data
```json
{
        "listing title": "Details about  \u00a0Apple iPhone 12 64GB t-mobil Unlocked Smartphone -open box",
        "rating": "",
        "condition": "Open box",
        "price": "US $599.99",
        "shipping": "$22.00",
        "listing link": "https://www.ebay.com/itm/125097522656?epid=13042891112&hash=item1d2064b5e0:g:lJEAAOSwj~Rh33ZU"
}
```

#### BotStudio
[Bot_Studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product will be bought. To buy first login will need to be done. Login can be done either with credentials or via cookies


### Installation

```sh
pip install ebay-listings-scraper
```

### Import
```sh
from ebay_listings_scraper import *
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```
### Scrape eBay Listings
```sh
response =ebay.listings_scraper(Search_for_anything="mobiles")
```

### Run Bot on Cloud
You can run bot on [Cloud](https://datakund.com/products/ebay-product-and-listing-data-scraper-bot?_pos=1&_sid=f54101153&_ss=r).

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

