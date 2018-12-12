from botbuilder.schema import CardImage

class adaptive_list:

    room_card = {
                  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                  "type": "AdaptiveCard",
                  "version": "1.0",
                  "body": [
                            { "type": "TextBlock", "text": "Book a Room", "weight": "bolder",  "size": "medium"},
                            { "type": "TextBlock", "text": "Fill in the correct details","wrap": True},
                            { "type": "TextBlock", "text": "Your Name", "isSubtle": True, "wrap": True},
                            { "type": "Input.Text", "id": "myName"},
                            { "type": "TextBlock", "text": "Phone Number (with code)", "isSubtle": True},
                            { "type": "Input.Text", "id": "myTel", "style": "tel","placeholder": "91xxxxxxxxxx" },
                            { "type": "TextBlock", "text": "E-mail", "isSubtle": True},
                            { "type": "Input.Text", "id": "myEmail", "style": "email", "placeholder": "youremail@example.com"},
							{ "type": "TextBlock", "text": "No.of Rooms (in numbers)", "isSubtle": True},
                            { "type": "Input.Text", "id": "rooms", "placeholder": "Eg: 2"}, 
                            { "type": "TextBlock", "text": "Check in Date (dd/mm/yyyy format only)", "isSubtle": True, "wrap": True,"placeholder": "dd/mm/yyyy"},
                            { "type": "Input.Text", "id": "indate"},
                            { "type": "TextBlock", "text": "Check out Date (dd/mm/yyyy format only)", "isSubtle": True, "wrap": True,"placeholder": "dd/mm/yyyy"},
                            { "type": "Input.Text", "id": "outdate"},
							{ "type": "TextBlock", "text": "No.of Adults (in numbers) -12yrs and above", "isSubtle": True},
                            { "type": "Input.Text", "id": "adults", "placeholder": "Eg: 2"}, 
							{ "type": "TextBlock", "text": "No.of Children (in numbers)", "isSubtle": True},
                            { "type": "Input.Text", "id": "child", "placeholder": "Eg: 2"}, 
							{ "type":"TextBlock", "text":"Kindly verify your info again before submitting","weight":"bolder"},
                        ],
                    "actions": [{ "type": "Action.Submit", "title": "Submit" }]
                }
    
    
    dine_card = {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.0",
                    "body": [
                                {"type": "TextBlock", "text": "Wining and Dining","weight": "bolder","size": "medium"},
                                {"type":"ImageSet", "imageSize":"medium", "images":""},
                                {"type": "TextBlock", "text": "", "wrap": True},
                                {"type": "TextBlock", "text": "[Sample Text]", "isSubtle": True, "wrap": True},
                                {"type": "TextBlock", "text": "Phone Number (with code)"},
                                {"type": "Input.Text","id": "myTel","placeholder": "91xxxxxxxxxx", "style": "tel"},
                                {"type": "TextBlock", "text": "Your email", "wrap": True},
                                {"type": "Input.Text","id": "myEmail","placeholder": "youremail@example.com", "style": "email"},

                            ],
                    "actions": [{"type": "Action.Submit", "title": "Submit"}]
                }
    
    event_card = {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.0",
                    "body": [
                                {"type": "TextBlock", "text": "Plan an Event", "weight": "bolder", "size": "medium"},
                                { "type":"ImageSet", "imageSize":"medium", "images":""},
                                { "type": "TextBlock", "text": "[Sample Text]", "isSubtle": True, "wrap": True},
                                { "type": "TextBlock", "text": "Your Destination", "wrap": True},
                                { "type": "Input.Text", "id": "dest"},
                                {"type": "TextBlock", "text": "Phone Number (with code)"},
                                {"type": "Input.Text","id": "myTel","placeholder": "91xxxxxxxxxx", "style": "tel"},
                                {"type": "TextBlock", "text": "Your email", "wrap": True},
                                {"type": "Input.Text","id": "myEmail","placeholder": "youremail@example.com", "style": "email"},
                            ],
                    "actions": [{"type": "Action.Submit", "title": "Submit"}]
                }
    
    package_card = {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.0",
                    "body": [
                                {"type": "TextBlock", "text": "Book a Package", "weight": "bolder", "size": "medium"},
                                { "type":"ImageSet", "imageSize":"medium", "images":""},
                                { "type": "TextBlock", "text": "[Sample Text]", "isSubtle": True, "wrap": True},
                                { "type": "TextBlock", "text": "Your Destination", "wrap": True},
                                { "type": "Input.Text", "id": "dest"},
                                {"type": "TextBlock", "text": "Phone Number (with code)"},
                                {"type": "Input.Text","id": "myTel","placeholder": "91xxxxxxxxxx", "style": "tel"},
                                {"type": "TextBlock", "text": "Your email", "wrap": True},
                                {"type": "Input.Text","id": "myEmail","placeholder": "youremail@example.com", "style": "email"},
                            ],
                    "actions": [{"type": "Action.Submit", "title": "Submit"}]
                }
    
    
    hotel_card = {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                    "type": "AdaptiveCard",
                    "version": "1.0",
                    "body": [
                        {"type": "TextBlock", "text": "", "size": "medium", "wrap": "true"},
                        { "type":"ImageSet", "imageSize":"medium","images":""},
                            ]
                }
    
    guest_card = {
                  "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                  "type": "AdaptiveCard",
                  "version": "1.0",
                  "body": [
                            { "type": "TextBlock", "text": "Enter your details", "weight": "bolder",  "size": "medium"},
                            { "type": "TextBlock", "text": "Fill in the correct details","wrap": True},
                            { "type": "TextBlock", "text": "Your Name", "isSubtle": True, "wrap": True},
                            { "type": "Input.Text", "id": "myName"},
                            { "type": "TextBlock", "text": "Phone Number (with code)", "isSubtle": True},
                            { "type": "Input.Text", "id": "myTel", "style": "tel","placeholder": "91xxxxxxxxxx" },
                            { "type": "TextBlock", "text": "E-mail", "isSubtle": True},
                            { "type": "Input.Text", "id": "myEmail", "style": "email", "placeholder": "youremail@example.com"},
							{ "type":"TextBlock", "text":"Kindly verify your info again before submitting","weight":"bolder"},
                        ],
                    "actions": [{ "type": "Action.Submit", "title": "Submit" }]
                }

   
 

