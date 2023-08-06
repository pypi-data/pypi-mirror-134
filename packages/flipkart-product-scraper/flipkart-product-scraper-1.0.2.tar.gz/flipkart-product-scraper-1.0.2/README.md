Flipkart product scraper is a python library to scrape for a Flipkart product using browser automation. 
It currently runs only on windows.

### Scrape Title, Price and Link of Flipkart Product
We first import library, then we provide the keyword to be scraped instead of **"clothes"**.
```sh
from flipkart_product_scraper import *
response=flipkart.product_data(keyword="clothes")
```

### Response Data
```json
      "Link":"/idisi-clothes-polycotton-printed-shirt-fabric/p/itmcf8133404aff4?pid=FABGA864JWDFRZXH&lid=LSTFABGA864JWDFRZXHINYCFJ&marketplace=FLIPKART...",
      "Price": "₹289",
      "Title": "Polycotton Printed Shirt Fabric"
```

#### BotStudio
[Bot_Studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up and searches a keyword in Flipkart website and scrapes data from the search result.


### Installation

```sh
pip install flipkart-product-scraper
```

### Import
```sh
from flipkart_product_scraper import *
```

### Get Flipkart Scraper
```sh
flipkart.product_data(keyword="clothes")
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Run bot on cloud
You can run bot on [Cloud](https://datakund.com/products/flipkart-product-result-scraper).

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

