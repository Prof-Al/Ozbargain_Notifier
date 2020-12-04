import requests
from bs4 import BeautifulSoup
import datetime
import time
from notification_sender import SendNotification


def send_notification(message):
    SendNotification("1407892120:AAFbCeviLIjiglgTgEl_UUYnHInD_odilso", 1472327697, message)


OZBARGAIN_URL = "https://www.ozbargain.com.au"
OZBARGAIN_DEALS_URL = "https://www.ozbargain.com.au/deals"
response = requests.get(OZBARGAIN_DEALS_URL)

soup = BeautifulSoup(response.content, 'html.parser')

# Retrieve all 30 deal's votes
votes = soup.select(".nvb.voteup span")
votes = [int(vote.text) for vote in votes]

# Retrieve all 30 deal's titles
titles = soup.select(".title")
titles = [title.text for title in titles]

# Retrieve all 30 deal's time of posting
posted = soup.select(".submitted")
posted = [datetime.datetime.strptime(" ".join(date.text.split()[-4:-1]), "%d/%m/%Y - %H:%M") for date in posted]

# Compute all 30 deal's time since posting
time_since_posted = [int((datetime.datetime.now() - time).total_seconds() // 60) for time in posted]

# Locate all links for posted deals
links = [deal["href"] for deal in soup.select(".title a[href]")]

# Finds all deals that have been posted in the last 10 minutes
relevant_deals = [[title, post_time, vote, link]
                  for title, post_time, vote, link in zip(titles, time_since_posted, votes, links)
                  if 0 < post_time < 11]

# Loops through all relevant deals to calculate whether the deal is especially good
for deal in relevant_deals:

    if deal[1] < 5 and deal[2] > 4:
        send_notification("New Deal '{}'".format(deal[0]))
        send_notification("{} Upvotes in {} minutes!".format(deal[2], deal[1]))
        send_notification(OZBARGAIN_URL + deal[3])

    elif deal[2] >= deal[1] > 4:
        send_notification("New Deal '{}'".format(deal[0]))
        send_notification("{} Upvotes in {} minutes!".format(deal[2], deal[1]))
        send_notification(OZBARGAIN_URL + deal[3])
