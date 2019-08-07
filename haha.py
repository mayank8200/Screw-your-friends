import webbrowser
import random
import time
while True:
 sites=random.choice(['google.com','amazon.in','flipkart.com','youtube.com'])
 visit="http://{}".format(sites)
 webbrowser.open(visit)
 seconds=random.randrange(0,2)
 time.sleep(seconds)
