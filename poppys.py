import http.server, time,requests,json,asyncio
from botbuilder.schema import Activity, ActivityTypes, ChannelAccount, HeroCard, Attachment, CardImage, SigninCard, CardAction
from botbuilder.schema import ActionTypes, ThumbnailCard
from botbuilder.core import BotFrameworkAdapter, CardFactory
from botframework.connector import ConnectorClient
from botframework.connector.auth import MicrosoftAppCredentials, JwtTokenValidation, SimpleCredentialProvider
from Hotels import Hotels
from adaptive_cards import adaptive_list
import webbrowser

APP_ID=''
APP_PASSWORD=''
WELCOME = "Hi! My name is Poppys. May I know your name? (Eg: Mr(s).Amit)"
wlc = "Thank you for taking your time out to chat with me, "


class Bot(http.server.BaseHTTPRequestHandler):
    
    Name = ''
    city= ''
    hotel_name=''
    init = True
    query= False
    menu_opt= False
    sub = False
    flag_dict = {'book':False,'dine':False,'event':False,'package':False,'call':False}
    
    def __handle_authentication(self, activity):
        credential_provider = SimpleCredentialProvider(APP_ID, APP_PASSWORD)
        loop = asyncio.new_event_loop()
        try:
            loop.run_until_complete(JwtTokenValidation.authenticate_request(
                activity, self.headers.get("Authorization"), credential_provider))
            return True
        except Exception as ex:
            self.send_response(401, ex)
            self.end_headers()
            return False
        finally:
            loop.close()

    
    def __create_reply_activity(request_activity: Activity, text: str, attachment: Attachment = None) -> Activity:
        
        activity = Activity(
        type=ActivityTypes.message,
        channel_id=request_activity.channel_id,
        conversation=request_activity.conversation,
        recipient=request_activity.from_property,
        from_property=request_activity.recipient,
        text=text,
        service_url=request_activity.service_url)
    
        if attachment:
            activity.attachments = [attachment]    
        return activity
    
    
    def __handle_conversation_update_activity(self, activity):
        self.send_response(202)
        self.end_headers()
        if activity.members_added[0].id != activity.recipient.id:
            credentials = MicrosoftAppCredentials(APP_ID, APP_PASSWORD)
            Bot.init= True
            Bot.sub= False
            Bot.menu_opt= False
            Bot.query = False
            reply = Bot.__create_reply_activity(activity, WELCOME)
            connector = ConnectorClient(credentials, base_url=reply.service_url)
            connector.conversations.send_to_conversation(reply.conversation.id, reply)
    
    def __unhandled_activity(self):
        self.send_response(404)
        self.end_headers()
        
    def reset_flags():  #Reset menu options to false - for resetting and initialising the menu options everytime different hotel is chosen
        for key in Bot.flag_dict.keys():
            Bot.flag_dict[key] = False
            
    def choose_hotel(): # Main menu - show cities   
        Bot.menu_opt=False
        Bot.sub=False
        Bot.query=False
        locs = Bot.show_location()
        return locs

    def show_location():     
        Bot.init=False
        card = SigninCard(buttons=[
            CardAction(type=ActionTypes.im_back, title=i, value=i) for i in Hotels.data().keys()])   
        locs = CardFactory.signin_card(card)  
        return locs
  
    def book_room(): #Return room booking form
        card = adaptive_list.room_card
        return CardFactory.adaptive_card(card)

    def hotel_card(info,img): #Display hotel card - with pictures and hotel info message
        imgs = [{"type":"Image","url":i} for i in img]
        card = adaptive_list.hotel_card
        card['body'][0]['text'] = info
        card['body'][1]['images']=imgs
        return CardFactory.adaptive_card(card)
    
    def guest_info():
        card = adaptive_list.guest_card
        return CardFactory.adaptive_card(card)
    
    def menu_card(hotel):  #Hotel Menu
                       
        add = []
        check = {'Wine','Dine','Event','Package','Book','FAQ','Call'}
        keys = set(key for key in hotel.keys() if hotel.get(key)==True)

        res = check & keys
        #print(res)

        if 'Book' in res:
            add = add + ['Book a Room']
            
        if 'Dine' in res:
            if 'Wine' in res:
                add = add + ['Wine & Dine']
            else:
                add = add + ['Dining']
                
        if 'Event' in res:
            add = add + ['Plan an Event']
        
        if 'Package' in res:
            add = add + ['Book a Package'] 
            
        if 'FAQ' in res:
            add = add + ['Have any Questions?']
            
        if 'Call' in res:
            add = add + ['Request Callback']
        
        opt = add+['Main Menu']
        
        card = SigninCard(text=Bot.Name+", How may I help you?", buttons=[
            CardAction(type=ActionTypes.im_back, title=i, value=i) for i in opt])   
        locs = CardFactory.signin_card(card)                  
        return locs 
    
    def faq(q): #LUIS 
        
        out = "I am Sorry "+Bot.Name+", I don't understand this question, or do not know the answer. Kindly contact out management directly"   
        
        luis_url = "https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/fdee8e37-8608-4bbd-9dae-645861990663?subscription-key=233c1e029fe3457eb67e154db51eb1f3&timezoneOffset=-360&q="
        headers = {"Ocp-Apim-Subscription-Key": "233c1e029fe3457eb67e154db51eb1f3"}
                  
        
        response = requests.get(luis_url+q, headers=headers)
        result = response.json()

        intent = result['topScoringIntent']['intent']

        if intent == "None":
            return out
        
        print("Intent:",intent)
        host = "https://qnatestsuhan.azurewebsites.net/qnamaker/"
        endpoint_key = "fe854ef2-d465-49cf-bf0c-ca866bf7d2be"
        kb_id = "2014e26c-be56-480c-b4a5-6925b0250bad"
        route = "knowledgebases/" + kb_id + "/generateAnswer"
        
        headers = {
                    'Authorization': 'EndpointKey ' + endpoint_key,
                    'Content-Type': 'application/json',
                }
        question = {'question': intent}
        query = json.dumps(question)
                    
        response = requests.post(host+route, headers=headers, data=query)
        result = json.loads(response.content.decode('utf-8'))
        print("Result:",result)
        if len(result)>0:
            out = result['answers'][0]['answer']    
        if out == "No good match found in KB.":
            out = "I am Sorry "+Bot.Name+", I don't understand this question, or do not know the answer. Kindly contact out management directly"
                
        return out
    
    def __handle_initial_activity(self,activity):   # Initialization- Welcome msg, hotel info and pics
        
        Bot.init=False
        self.send_response(200)
        self.end_headers()
        credentials = MicrosoftAppCredentials(APP_ID, APP_PASSWORD)
        connector = ConnectorClient(credentials, base_url=activity.service_url)
        
        Bot.Name = activity.text
        locs = Bot.show_location()
        st = wlc+Bot.Name+". \nPlease choose which city you prefer."
        reply = Bot.__create_reply_activity(activity,st,locs)
        connector.conversations.send_to_conversation(reply.conversation.id, reply)
        
        
    def __handle_message_activity(self,activity): #Main logic to handle each reply
        self.send_response(200)
        self.end_headers()
        credentials = MicrosoftAppCredentials(APP_ID, APP_PASSWORD)
        connector = ConnectorClient(credentials, base_url=activity.service_url)
    
        if Bot.init: #Initial customization
            Bot.Name = activity.text
            locs = Bot.show_location()
            st = wlc+Bot.Name+" to chat with me. \nPlease choose which city you prefer."
            reply = Bot.__create_reply_activity(activity,st,locs)
            connector.conversations.send_to_conversation(reply.conversation.id, reply)
            Bot.init=False

        else:

            if not Bot.menu_opt:  # If it is not hotel menu

                if not Bot.sub:  #If it is not a sub-hotel menu (sub-hotel menu meaning - it is not clicked from the list of many hotels in a single city)

                    Bot.city = activity.text
                    hotel = Hotels.data().get(Bot.city)

                    if len(hotel.keys())==1: #  If there is only one hotel in the city, directly display the pics and info
                        Bot.hotel_name = list(hotel.keys())[0]
                        ht = list(hotel.values())[0]
                        info = ht['info']
                        img = ht['img']
                        card = Bot.hotel_card(info,img)
                        Bot.property_code = ht['PropertyCode']
                        reply = Bot.__create_reply_activity(activity,'',card)
                        connector.conversations.send_to_conversation(reply.conversation.id, reply)
                        time.sleep(1)
                        menu = Bot.menu_card(hotel.get(Bot.hotel_name))
                        reply = Bot.__create_reply_activity(activity,'',menu)
                        connector.conversations.send_to_conversation(reply.conversation.id, reply)
                        Bot.menu_opt = True

                    else:  #If there are more than one hotel in a city, show the hotels list and set Bot.sub as True
                        htlst = SigninCard(text="Choose a hotel in {}".format(Bot.city), buttons=[
                                        CardAction(type=ActionTypes.im_back, title=i, value=i) for i in hotel.keys()])   
                        card = CardFactory.signin_card(htlst) 
                        reply = Bot.__create_reply_activity(activity,'',card)
                        connector.conversations.send_to_conversation(reply.conversation.id, reply)
                        Bot.sub = True
                else: # For choosing one hotel from multiple hotels in single city, i.e it is a sub-hotel menu

                    Bot.hotel_name = activity.text
                    hotel = Hotels.data().get(Bot.city).get(Bot.hotel_name)
                    info = hotel.get('info')
                    img = hotel.get('img')
                    card = Bot.hotel_card(info,img)
                    Bot.property_code = hotel['PropertyCode']
                    reply = Bot.__create_reply_activity(activity,'',card)
                    connector.conversations.send_to_conversation(reply.conversation.id, reply)
                    time.sleep(1)
                    menu = Bot.menu_card(hotel)
                    reply = Bot.__create_reply_activity(activity,'',menu)
                    connector.conversations.send_to_conversation(reply.conversation.id, reply)
                    Bot.menu_opt = True

            else: #For rest of the inputs

                value = activity.text
                
                defmsg = "I am Sorry "+Bot.Name+", Kindly share your e-mail id. I will revert at the earliest."

                if value=="Book_Package":
                    msg = Bot.Name+", Your details have been submitted successfully. We will call you back shortly. Thanks for contacting us."
                    reply = Bot.__create_reply_activity(activity,msg,menu)
                    connector.conversations.send_to_conversation(reply.conversation.id, reply)

                    hotel = Hotels.data().get(Bot.city).get(Bot.hotel_name)
                    menu = Bot.menu_card(hotel)  #Display main menu
                    reply = Bot.__create_reply_activity(activity,'Is there anything else I can help you with?',menu)
                    connector.conversations.send_to_conversation(reply.conversation.id, reply)
                    Bot.menu_opt = True


                if Bot.query == True:  #If faq is clicked

                    out = Bot.faq(value)
                    reply = Bot.__create_reply_activity(activity,out)
                    connector.conversations.send_to_conversation(reply.conversation.id, reply)               
                    Bot.query = False
                    hotel = Hotels.data().get(Bot.city).get(Bot.hotel_name)
                    menu = Bot.menu_card(hotel)
                    reply = Bot.__create_reply_activity(activity,'Is there anything else I can help you with?',menu)
                    connector.conversations.send_to_conversation(reply.conversation.id, reply)
                    Bot.menu_opt = True

                else:

                    if value =='Book a Room':

                        Bot.reset_flags()
                        Bot.flag_dict['book'] = True
                        card = Bot.book_room() #show booking form
                        reply = Bot.__create_reply_activity(activity, '',card)
                        connector.conversations.send_to_conversation(reply.conversation.id, reply)

                    elif value == "Dining" or value == "Wine & Dine":
                        Bot.reset_flags()
                        Bot.flag_dict['dine'] = True
                        images = Hotels.data().get(Bot.city).get(Bot.hotel_name).get('img')
                        card = Bot.guest_info()
                        reply = Bot.__create_reply_activity(activity, '',card)
                        connector.conversations.send_to_conversation(reply.conversation.id, reply)

                    elif value == "Plan an Event": 
                        Bot.reset_flags()
                        Bot.flag_dict['event'] = True
                        images = Hotels.data().get(Bot.city).get(Bot.hotel_name).get('img')
                        card = Bot.guest_info()
                        reply = Bot.__create_reply_activity(activity, '',card)
                        connector.conversations.send_to_conversation(reply.conversation.id, reply)

                    elif value == "Book a Package":
                        Bot.reset_flags()
                        Bot.flag_dict['package'] = True
                        card = Bot.guest_info()
                        reply = Bot.__create_reply_activity(activity, '',card)
                        connector.conversations.send_to_conversation(reply.conversation.id, reply)


                    elif value == "Have any Questions?":
                        Bot.query = True
                        reply = Bot.__create_reply_activity(activity, 'Hey '+Bot.Name+',Type your question and I will try my best to answer for you..')
                        connector.conversations.send_to_conversation(reply.conversation.id, reply) 
                    
                    elif value == "Main Menu":
                        locs = Bot.choose_hotel()
                        reply = Bot.__create_reply_activity(activity,'Choose a city',locs)
                        connector.conversations.send_to_conversation(reply.conversation.id, reply)
                    else:

                        if value == None: #For all submit buttons, value is returned as None. So using that to differentiate inputs obtained through various submit buttons

                            success = "Your details have been submitted successfully "+Bot.Name+". You will soon be contacted back"
                           
                            if Bot.flag_dict.get('book'):  #Open resavenue booking page in browser

                                data = activity.value
                                indate = data['indate']
                                outdate = data['outdate']
                                #indate = indt[3:6]+indt[0:3]+indt[6:]
                                #outdate = otdt[3:6]+otdt[0:3]+otdt[6:]
                                
                                url = "http://www.resavenue.com/bookingNew/servlet/checkAvailable.resBookings?regCode={}&arr_date={}&dep_date={}&roomNo={}&adult_1={}&child_1={}&targetTemplate=3".format(Bot.property_code,indate,outdate,data['rooms'],data['adults'],data['child'])
                                print(url)
                                webbrowser.open_new(url)
                                reply = Bot.__create_reply_activity(activity,'You will now be redirected to the booking page')
                                connector.conversations.send_to_conversation(reply.conversation.id, reply)

                            if Bot.flag_dict.get('event'):

                                reply = Bot.__create_reply_activity(activity,success)
                                connector.conversations.send_to_conversation(reply.conversation.id, reply)

                            if Bot.flag_dict.get('dine'):
                                reply = Bot.__create_reply_activity(activity,success)
                                connector.conversations.send_to_conversation(reply.conversation.id, reply)

                            if Bot.flag_dict.get('package'):
                                reply = Bot.__create_reply_activity(activity,success)
                                connector.conversations.send_to_conversation(reply.conversation.id, reply)

                            Bot.reset_flags()

                        else:
                            reply = Bot.__create_reply_activity(activity,defmsg)
                            connector.conversations.send_to_conversation(reply.conversation.id, reply)

                        hotel = Hotels.data().get(Bot.city).get(Bot.hotel_name)
                        menu = Bot.menu_card(hotel)
                        reply = Bot.__create_reply_activity(activity,'Is there anything else I can help you with?',menu)
                        connector.conversations.send_to_conversation(reply.conversation.id, reply)
                        Bot.menu_opt = True
    
    
    def do_POST(self):
        body = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(str(body, 'utf-8'))
        activity = Activity.deserialize(data)
        if activity.type == ActivityTypes.conversation_update.value: #Initial call
            self.__handle_conversation_update_activity(activity)
        elif activity.type == ActivityTypes.message.value:   
            if Bot.init == True: # The first run 
                self.__handle_initial_activity(activity)
            else:
                self.__handle_message_activity(activity) #Handles rest of all the replies
        else:
            self.__unhandled_activity()


try:
    SERVER = http.server.HTTPServer(('localhost', 3978), Bot) #First initial message is displayed from handle_conversation_update_activity and after that all replies are handled by do_POST
    print('Started http server on localhost:3978')
    SERVER.serve_forever()
except KeyboardInterrupt:
    print('Interrupted. Server shutting down server')
    SERVER.socket.close()

