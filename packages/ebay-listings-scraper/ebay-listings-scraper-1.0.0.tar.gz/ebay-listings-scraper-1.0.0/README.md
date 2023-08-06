Ebay listing scraper is a python library to scrape for a ebay listings(listing title, rating, condition, price, shipping and listing link), Using browser automation. 
It currently runs only on windows.

### Example : Ebay listing scraper to scrape listing title, rating, condition, price, shipping and listing link.
In this example we first import library, then provide the keyword, replace "mobiles" with "your keyword".
```sh
from ebay_listings_scraper import *
response =ebay.listings_scraper(Search_for_anything="mobiles")
#response =  {
#    "errors": [],
#    "body": [
#      {
#        "listing title": "Details about  \u00a0OnePlus 7 Pro Grey 256GB T Mobile Unlocked Android Smartphone",
#        "rating": "",
#        "condition": "Used",
#        "price": "US $139.99",
#        "shipping": "$22.00",
#        "listing link": "https://www.ebay.com/itm/185247077763?epid=13033706096&_trkparms=ispr%3D1&hash=item2b21961583:g:Fp0AAOSwidVh2NuL&amdata=enc%3AAQAGAAACkPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsS7UXID%252BRPOSNsnm8kYPghtOQvMzn71Ze3c1eI8kOjV8CUTM6CRIElR2UPuukAW6yoGNjbJDRQsTVqgnlY%252FqPDmPPmRZGwiNuemveNELqbTqaNEzGabvenhQYoMQ7p7kh%252BDtD%252BpXNGKyCMWDZcIb0ETnsssMPqexq8p%252F90AEDnYib8VGrQ7LKMi0BeYNl%252B8MQH68UynHGD77hVnBh8ZW6anGzoGmNab3UUq8b6emBf1fr%252Ffg6k2nXuH%252FfmL8jGr4nM33bwB1Dd0ZSk5clVFkIA2U1C2we9KpSoWmaWLmI8sjv7GPIO72ucdEqQHGBd6zCSNTEBrtnUhwyKn1Q8Bksn0IM1knVXA%252FQTnZtr%252BfeXlVR8u6RID822IjCKug8h5BjmkxCbSUyh%252FOxle%252BO6jdT2YlWUELVxTXWQPNqwqYsg%252B8S9h43C1kiLPgTlL7QcL9xflTH0se8RJqpu0Nkfs0y2%252B9dZLun4ilkTHZSoGJC3ocm3PepKLDJqRTZKPqgc45XcYVR90Cg4A27CYZTT5UQB3vuIESh%252FWNxdI9tB7nio3gPXhbRA47BBCrj7GyjIUi6NDDfavMI41f581f0w849ewGSN2tHujbVYdoIjA2XFicKtmJmehEzsGJtltOHu3eau45mp5ENuMprzO85mptAIY30hP%252BNBGigJpRoAoijrCina8b7G8QCxmGUX%252FsagZJ2SHibj2hf12ptN6dkjcFFGLZT515eU%252B%252Fkxt2K7iMqlVHOevbiba0JKBro6KSQD58yaIJas09zWeBgHuNQuhNkjEJYSX7qDLSXLNsM02HMPx%252BijPo11T3DT9L%252FCRjwEz6sE%7Cclp%3A2334524%7Ctkp%3ABFBMnqPIqcpf"
#      },....]}

```

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product will be bought. To buy first login will need to be done. Login can be done either with credentials or via cookies


### Installation

```sh
pip install ebay-listings-scraper
```

### Import
```sh
from ebay-listings-scraper import *
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

