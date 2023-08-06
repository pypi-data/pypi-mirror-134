Scrape Google trends is a python library to scrape google trends search results using browser automation. 
It currently runs only on windows.

### Example
In this example we first import library, then we provide the "keyword" to be scraped instead of "doctor".
```sh
from scrape_google_trends import *
response = google.trends(keyword="doctor")
#response = {
#    "errors": [],
#    "body": [
#      {
#        "state": "Kansas",
#        "trend": "100"
#      },
#      {
#        "state": "New York",
#        "trend": "70"
#      }.......]}

```

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product will be bought. To buy first login will need to be done. Login can be done either with credentials or via cookies


### Installation

```sh
pip install scrape-google-trends
```

### Import
```sh
from scrape-google-trends import *
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

