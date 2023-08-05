Google scholar scraper is a python library to scrape for a google scholar result using browser automation. 
It currently runs only on windows.

### Example
In this example we first import library, then we provide the keyword to be scraped instead of "science".
```sh
from scrape-google-scholar import *
response = google.scholar_scraper(search="science")
#response = {
#  {
#  "body": [
#    {
#      "Description": "This article assesses how the tension between centripetal forces (such as forward and backward linkages in production and increasing …",
#      "Link": "https://journals.sagepub.com/doi/abs/10.1177/016001799761012307",
#      "Title": "The role of geography in development"
#    },....]}

```

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product will be bought. To buy first login will need to be done. Login can be done either with credentials or via cookies


### Installation

```sh
pip install scrape-google-scholar
```

### Import
```sh
from scrape-google-scholar import *
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

