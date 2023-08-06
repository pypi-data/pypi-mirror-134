Facebook Scraper in is a python library to scrape Facebook friends list, using browser automation. 
It currently runs only on windows.

## Facebook Login
In this, we first login Facebook. Replace **"Email_address_or_phone_number"** with your email or phone number and **"abc@123"** with password.
```sh
from facebook_scraper_in import *
facebook.login_password(Email_address_or_phone_number="Email_address_or_phone_number",Password="abc@123")
```

## Facebook login with cookies
In this, we will login Facebook with the help of cookies. Replace **"cookies"** with Facebook cookies.
```sh
from facebook_scraper_in import *
facebook.login_cookies(cookies="cookies")
```

## Scrape Facebook Friends list 
In this example we will scrape friends list in the facebook account. Replace the **"url"** with your url. 
```sh
from facebook_scraper_in import *
response =facebook.friendlist_scraper(profile_link="url")
```
### Response Data
```json
        "name": "Vishal Katnawar",
        "profile_links":"https://www.facebook.com/vishal.katnawar.3"      
```

#### BotStudio
[Bot_Studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which Facebook page will load and logs in Facebook with your credentials and scrape all the Facebooks friends for the entered URL.


### Installation

```sh
pip install facebook-scraper-in
```

### Import
```sh
from facebook_scraper_in import *
```
### Login with Credentials and get Friends List
```sh
facebook.login_password(Email_address_or_phone_number="Email_address_or_phone_number",Password="abc@123")
response =facebook.friendlist_scraper(profile_link="url")
data=response['body']
```

### Login with Cookies and get Friends List
```sh
facebook.login_cookies(cookies="cookies")
response =facebook.friendlist_scraper(profile_link="url")
data=response['body']
```

### Run bot on cloud
You can run bot on [Cloud](https://datakund.com/products/facebook-friend-list-scraper-bot?_pos=3&_sid=487244d87&_ss=r).


### Cookies

To login with cookies [Edit this Cookie Extension](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en) can be added to browser. Please check [this](https://abhishek-chaudhary.medium.com/how-to-get-cookies-of-any-website-from-browser-22b3d6348ed2) link how to get cookies to login to your amazon.


### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```
### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

