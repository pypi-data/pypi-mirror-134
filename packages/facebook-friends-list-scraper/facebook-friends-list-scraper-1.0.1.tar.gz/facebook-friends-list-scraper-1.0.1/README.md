Facebook friends list scraper is a python library to scrape Facebook friends list, using browser automation. 
It currently runs only on windows.

### Example 1 : Facebook Login
In this example we first login facebook. Replace "Email_address_or_phone_number" with your email or phone number and "abc@123" with password.
```sh
from facebook_friends_list_scraper import *
response =facebook.login_password(Email_address_or_phone_number="Email_address_or_phone_number",Password="abc@123")
#response = {
#{
#    "bot": "facebook_login_password",
#    "user": "ampkdAT3PfT5kMoFVGuh5WqyGcD267      @R39R4MHV9YRL3W9",
#    "umail": "abcrs@gmail.com",
#    "cookies_data": {},
#    "run_type": "simple",
#    "outputdata": {
#      "Email_address_or_phone_number": "abc@gmail.com",
#      "Password": "abc@123",
#      "email_address_or_phone_number": "abc@gmail.com",
#      "password": "abc@123"
#    }.......}}
```

### Example 2 : Facebook login with cookies
In this example we will login facebook with the help of cookies. Replace "cookies" with facebook cookies.
```sh

from facebook_friends_list_scraper import *
response =facebook.login_cookies(cookies="cookies")
#response = {
#  "body": {
#      "bot": "facebook_login_cookies",
#    "user": "ampkdAT3PfT5kMoFVGuh5WqyGcD267      @PA1CTRNUKC7JD5W",
#    "umail": "abc@gmail.com",
#    "cookies_data": {},
#    "run_type": "simple",
#    "outputdata": {
#     "twitter_cookies": "[\n{\n    \"domain\": \".twitter.com\",\n  
#    },........]}
#   }.....}
```


### Example 3 : Scrape facebook friends list 
In this example we will scrape friends list in the facebook account. Replace the 'url' with your url. 
```sh
from facebook_friends_list_scraper import *
response =facebook.friendlist_scraper(profile_link="url")
#response = {
#  {
#        "name": "Vishal Katnawar",
#        "profile_links": "https://www.facebook.com/vishal.katnawar.3"
#      }.......}
```


#### BotStudio
[bot_studio](https://pypi.org/project/bot_studio/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product will be bought. To buy first login will need to be done. Login can be done either with credentials or via cookies


### Installation

```sh
pip install facebook-friends-list-scraper
```

### Import
```sh
from facebook-friends-list-scraper import *
```

### Send Feedback to Developers
```sh
bot_studio.send_feedback(feedback="Need help with this ......")
```

### Cookies
```sh
To login with cookies [Edit this Cookie Extension](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en) can be added to browser. Please check [this](https://abhishek-chaudhary.medium.com/how-to-get-cookies-of-any-website-from-browser-22b3d6348ed2) link how to get cookies to login to your amazon.
```
### Contact Us
* [Telegram](https://t.me/datakund)
* [Website](https://datakund.com)

