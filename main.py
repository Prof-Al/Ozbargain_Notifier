import requests
from bs4 import BeautifulSoup
import datetime
import time

start = time.time()
URL = "https://www.ozbargain.com.au/deals"
response = requests.get(URL)

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

# Finds all deals that have been posted in the last 10 minutes
relevant_deals = [[title, post_time, vote]
                  for title, post_time, vote in zip(titles, time_since_posted, votes)
                  if 0 < post_time < 11]


# Loops through all relevant deals to calculate whether the deal is especially good
for deal in relevant_deals:
    if deal[1] < 5 and deal[2] > 4:
        pass
        # send notification
    elif deal[2] >= deal[1] > 4:
        # send notification
        pass

print(relevant_deals)

print(time.time() - start)
