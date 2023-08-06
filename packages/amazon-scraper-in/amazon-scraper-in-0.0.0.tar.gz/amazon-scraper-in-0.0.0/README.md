Amazon Scraper in, is a python library to scrape price, description, reviews......., using browser automation. 
It currently runs only on windows.

## Scrape Price, Title, Rating of Amazon Products
* In this, we first import library, then we fetched data using simple function. 
* Replace **"shoes"** with **"your keyword"**.
```sh
          from amazon_scraper_in import *
          response = amazon.product_scraper(field_keywords="shoes")
```

### Response Data
```sh
          "link": "/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A07750533DB5H19IBKGZW&url=%2FOxygen-01-technology-sneakers-lightweight-trekking%2Fdp%2FB09C3YM7KW%2Fref%3Dsr_1_1_sspa%3Fcrid%3D2P6T84BH8UBOG%26keywords%3Dshoes%26qid%3D1641982789%26sprefix%3Dshoes%252Caps%252C197%26sr%3D8-1-spons%26psc%3D1&qualifier=1641982789&id=8000256934117296&widgetName=sp_atf",
          "title": "Oxygen-01 Running Shoes for Boys",
          "rating": "3.8 out of 5 stars",
          "price": "999"
```
## Scrape Reviews of Amazon Product
* In this, we first import library, then we fetched data using simple function. 
* Replace **"url_link"** with **"your amazon product link"**.
```sh
          from amazon_scraper_in import *
          response = amazon.product_review_scraper(url_link="url_link")
```

### Response Data
```sh
          "description": "* light weight shoes * Suitable for running and walking"  
```
## Scrape Price and Title of Amazon Products
* In this, we first import library, then we fetched data using simple function. 
* Replace **"shoes"** with **"your keyword"**.
```sh
          from amazon_scraper_in import *
          response=amazon.prices_scrape(field_keywords="shoes")
```

### Response Data
```sh
          "title": "Men's Wonder-13 Sports Running Shoes",
          "price": "499"
```

#### BotStudio
[Bot_Studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which keyword will be given as input. This keyword is searched in the amazon website or the amazon product URL is loaded, and scrapes the data.

### Installation
```sh
          pip install amazon-scraper-in
```

### Import
```sh
          from amazon_scraper_in import *
```

### Get Price, Title, Rating
```sh
          response=amazon.product_scraper(field_keywords="shoes")
          data=response['body']
```

### Get Product Reviews
```sh
          response=amazon.product_review_scraper(url_link="url_link")
          data=response['body']
```

### Get only Price and Title
```sh
          response=amazon.prices_scrape(field_keywords="shoes")
          data=response['body']
```

### Run bot on cloud
* Scrape Price, Title, Rating of Amazon Products - You can run bot on [Cloud](https://datakund.com/products/amazon-product-scraper-2?_pos=8&_sid=b74806d33&_ss=r).
* Scrape Reviews of Amazon Product - You can run bot on [Cloud](https://datakund.com/products/amazon-reviews-scraper?_pos=7&_sid=b74806d33&_ss=r).
* Scrape Price and Title of Amazon Products - You can run bot on [Cloud](https://datakund.com/products/amazon_price_scraper?_pos=1&_sid=57bc0259f&_ss=r).

### Send Feedback to Developers
```sh
          bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)


