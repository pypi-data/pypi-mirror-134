Flipkart product scraper is a python library to scrape for a flipkart product using browser automation. 
It currently runs only on windows.

### Example
In this example we first import library, then we provide the keyword to be scraped instead of "clothes".
```sh
from flipkart_product_scraper import *
response = flipkart.product_data(keyword="clothes")
#response = {
#  "body": [
#    {
#      "Link":"/idisi-clothes-polycotton-printed-shirt-fabric/p/itmcf8133404aff4?pid=FABGA864JWDFRZXH&lid=LSTFABGA864JWDFRZXHINYCFJ&marketplace=FLIPKART...",
#      "Price": "₹289",
#      "Title": "Polycotton Printed Shirt Fabric"
#    },....]}

```

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product will be bought. To buy first login will need to be done. Login can be done either with credentials or via cookies


### Installation

```sh
pip install flipkart-product-scraper
```

### Import
```sh
from flipkart-product-scraper import *
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

