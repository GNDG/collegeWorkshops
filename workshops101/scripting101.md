1. Twitter script in python for posting tweets, url and images

import tweepy
import requests
import uuid


TWITTER_CONSUMER_KEY = XXXXXX
TWITTER_CONSUMER_SECRET = XXXXXX
TWITTER_ACCESS_KEY = XXXXXX
TWITTER_ACCESS_SECRET = XXXXXX


def twitter_api_authentication():
    """Return authentication for twitter using tweepy, authenticated via
       TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY and
       TWITTER_ACCESS_SECRET.

    """
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
    return tweepy.API(auth)


twitter_api = twitter_api_authentication()


def save_image_from_url(image_url):
    """ Extract a image from the image_url

    Args:
        -image_url: Url of the attachment to be posted

    """
    fextn = image_url.rsplit('.')[-1]
    filename = uuid.uuid4().hex + '.' + fextn
    request = requests.get(image_url, stream=True)
    with open(filename, 'wb') as image:
        for chunk in request:
            image.write(chunk)
    return filename


def tweet_to_twitter(message, image_url=None):
    """ Posts a message to the Twitter page using twitter_api, an instance for
        twitter_api_authentication.

        Args:
            - message: str. The content of the message to be posted on Twitter.
            - image_url: (Optional) Url of the attachment to be posted along
              with message.

        Returns:
            - None

    """
    if image_url is not None:
        filename = save_image_from_url(image_url)
        twitter_api.update_with_media(filename, status=message)

    else:
        twitter_api.update_status(message)


image_url = "https://in.pycon.org/2016/images/logosm.png"
message = "testing my code"
tweet_to_twitter(message, image_url)
print("posted")


2. Facebook script in python for posting status, url and images

import facebook
#message=input("Please enter the message to be displayed: ")
def post_to_page(message_entered):
    graph = facebook.GraphAPI(access_token='FACEBOOK_TOKEN')
    #message_entered=input("Please enter the message to be displayed: ")

    attachment =  {
    'name': 'Pic',
    'link': 'https://conference.pydelhi.org/img/logo.png',   #must be same as picture
    'caption': 'Testing code',
    'description': 'PIC',
    'picture': 'https://conference.pydelhi.org/img/logo.png'  #must be same as link
    }

    return graph.put_wall_post(message=message_entered, attachment=attachment)
