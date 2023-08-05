Google search result scraper is a python library to scrape for a google search result using browser automation. 
It currently runs only on windows.

### Example
In this example we first import library, then we provide the keyword to be scraped instead of "doctor".
```sh
from scrape_google_results import *
response = google.search_result_scraper(Search="doctor")
#response = {
#  {
#  "body": [
#    {
#      "description": "Autism spectrum disorder (ASD) is a developmental disorder that affects communication and behavior. Although autism can be diagnosed at any age, ...",
#      "title": "NIMH » Autism Spectrum Disorder"
#    }

```

#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product will be bought. To buy first login will need to be done. Login can be done either with credentials or via cookies


### Installation

```sh
pip install scrape-google-results
```

### Import
```sh
from scrape-google-results import *
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

