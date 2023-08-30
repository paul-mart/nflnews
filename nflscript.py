import requests
import re
from twilio.rest import Client
import keys
from bs4 import BeautifulSoup
#filters <p> text from content


def remove_tags(text):
  pattern = r"<[^<>]+>"
  return re.sub(pattern, "", text)

client = Client(keys.account_sid, keys.auth_token)








url = 'https://www.yardbarker.com/nfl/teams/arizona_cardinals/47'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

top_story_div = soup.find('div', class_='grid-x rfi-module-top_story_pin rfi-module yb_module')
content = top_story_div.find('h2')
content_p = top_story_div.find('p')
print(remove_tags(str(content_p)))



headline = remove_tags(str(content))
paragraph = remove_tags(str(content_p))
text_msg = f'''Paul's Cardinals News: {headline}. {paragraph}'''
client.messages.create(body=text_msg, from_=keys.twilio_number, to=keys.target_number)