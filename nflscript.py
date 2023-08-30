import requests
import re
from twilio.rest import Client
import keys
from bs4 import BeautifulSoup

#filters html tags from text, returns desired headlines and paragraphs without HTML
def remove_tags(text):
  pattern = r"<[^<>]+>"
  return re.sub(pattern, "", text)

client = Client(keys.account_sid, keys.auth_token) #create client using acc id and token


url = 'https://www.yardbarker.com/nfl/teams/arizona_cardinals/47' #url for nfl team news page
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

top_story_div = soup.find('div', class_='grid-x rfi-module-top_story_pin rfi-module yb_module') #finds the top story from page
content = top_story_div.find('h2') #headline
content_p = top_story_div.find('p') #paragraph


headline = remove_tags(str(content)) #remove html tags
paragraph = remove_tags(str(content_p))
text_msg = f'''Paul's Cardinals News: {headline}. {paragraph}''' #create formatted string with headline and paragraph
client.messages.create(body=text_msg, from_=keys.twilio_number, to=keys.target_number) #sends SMS containing headline and paragraph
