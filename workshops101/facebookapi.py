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
