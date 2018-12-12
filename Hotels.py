class Hotels():
    
    def path():
        return "https://poppysbot.azurewebsites.net/Photos/poppys-photos/"
    
    def data():      
        hotel_data = {
		
		    'Chennai': { 'Mahalaya Residency':
                {
                    'info': 'Welcome to Mahalaya Residency, Chennai!',
                    'img': [Hotels.path()+"mahalaya-residency-chennai/g"+str(i)+".jpg" for i in range(1,9)],
                    'Wine':False,
                    'Dine':False,
					'Event':False,
					'Package':False,
					'Book':True,
					'FAQ':False,
					'Call':False,
					'PropertyCode' : "ZIRI0202"
                }
            },

			'Coimbatore': { 'Poppy\'s Coimbatore':
                {
                    'info': 'Vanakamungo Poppys Hotel! Nestled in the busy streets of the Manchester of south, Poppys is just 5 minutes from Coimbatore North railway station, centrally located with easy access to all the major business centers in the city.',
                    'img': [Hotels.path()+"poppys-hotel-coimbatore/g"+str(i)+".jpg" for i in range(1,9)],
                    'Wine':True,
                    'Dine':True,
					'Event':True,
					'Package':True,
					'Book':True,
					'FAQ':True,
					'Call':False,
					'PropertyCode' : "ZCRE0520"
                }
            },
			
            'Kochi':{ 'Aquatic Island':
                {
                    'info': 'Swagatham Aquatic Island! Man made paradise in God’s own country. Just 15 kilometers from Fort Kochi, the floating resort is tucked in the backwaters of Kumbalangi village.',
                    'img': [Hotels.path()+"aquatic-islands/"+str(i)+".jpg" for i in range(1,9)],
                    'Wine':False,
                    'Dine':True,
					'Event':False,
					'Package':True,
					'Book':True,
					'FAQ':True,
					'Call':False,
					'PropertyCode':"IXCV0422"
                }
            },
			
			'Kumbakonam': { 'Poppy\'s SET Residency':
                                {
                                    'info': 'Vanakam Poppys Hotel! Step out and Check in from the Kumbakonam Bus stand Poppys hotel is charming, while you explore this land of temples everywhere donning the colorful gopurams abode of lords. Not to miss two magnificent World Heritage–listed Chola temples nearby, it\'s worth staying the night.',
                                    'img': [Hotels.path()+"poppys-set-residency-kumbakonam/g"+str(i)+".jpg" for i in range(1,9)],
                                    'Wine':False,
									'Dine':True,
									'Event':True,
									'Package':True,
									'Book':True,
									'FAQ':False,
									'Call':False,
									'PropertyCode' : "IRXX0801"
                                },
                            'Hotel Vinayaga':
                                {
                                    'info': 'Vanakam Vinayaga Hotel! Step out and Check in from the Kumbakonam railway station Vinayaga hotel is welcoming while you explore this land of temples everywhere donning the colorful gopurams abode of lords. Not to miss two magnificent World Heritage–listed Chola temples nearby, it\'s worth staying the night.',
                                    'img': [Hotels.path()+"hotel-vinayaga-kumbakonam/g"+str(i)+".jpg" for i in range(1,9)],
                                    'Wine':False,
									'Dine':True,
									'Event':False,
									'Package':True,
									'Book':True,
									'FAQ':True,
									'Call':False,
									'PropertyCode' : "IZEI1105"
                                }
            },
			
			'Madurai': { 'Poppy\'s Madurai':
                {
                    'info': 'Vanakam Poppys Hotel! A vibrant hotel dotted in the ancient metropolis of south just 20 minutes drive from the Madurai Airport and a short drive to the most celebrated among Indias top ranked Meenakshi amman temple.',
                    'img': [Hotels.path()+"poppys-hotel-madurai/g"+str(i)+".jpg" for i in range(1,9)],
                    'Wine':True,
                    'Dine':True,
					'Event':True,
					'Package':True,
					'Book':True,
					'FAQ':False,
					'Call':False,
					'PropertyCode' : "IZEE1105"
                }
            },
			
			'Ooty': { 'Vinayaga Inn':
                {
                    'info': 'Vanakam Vinayaga Inn! A charming hotel amidst the magnificent sights of the awe-inspiring Nilgiri hills, tea gardens, and serene waterfalls, Just a stone throw distance from the world renowned botanical garden which hosts thousands of exotic and indigenous species of plants and a 20 million year old fossilized tree trunk too.',
                    'img': [Hotels.path()+"hotel-vinayaga-inn-ooty/g"+str(i)+".jpg" for i in range(1,9)],
                    'Wine':False,
                    'Dine':True,
					'Event':True,
					'Package':True,
					'Book':True,
					'FAQ':True,
					'Call':False,
					'PropertyCode' : "IZEZ1105"
                }
            },
			
			
            'Puducherry': { 'Mango-Hills':
                {
                    'info': 'Bonjour Mango Hill by Poppys! a French resort in the quiet countryside near Auroville. An \'ecofriendly\' haven of serenity just 6 kilometres outside the city, where Parisian savior-faire meets the charm of the Indian countryside.',
                    'img': [Hotels.path()+"mango-hill-by-poppys-pondicherry/g"+str(i)+".jpg" for i in range(1,9)],
                    'Wine':False,
                    'Dine':True,
					'Event':True,
					'Package':True,
					'Book':True,
					'FAQ':False,
					'Call':False,
					'PropertyCode' : "ZIRG0202"
                }
            },

            'Rameshwaram': { 'Hotel Vinayaga':
                {
                    'info': 'Namaskar! Vinayaga Hotel! Get greeted by the clean sea breeze in this island city with sacred ponds and one of the Char dhams of India. Hop out of the Rameswaram railway station and hop in to Vinayaga hotel to explore the nooks and crannies of Rameswaram, experience both its religious sites and tourist attractions with unparalleled natural beauty.',
                    'img': [Hotels.path()+"hotel-vinayaga-rameshwaram/g"+str(i)+".jpg" for i in range(1,9)],
                    'Wine':False,
                    'Dine':True,
					'Event':False,
					'Package':True,
					'Book':True,
					'FAQ':True,
					'Call':False,
					'PropertyCode' : "IZEG1105"
                }
            },            

            'Tirupur': { 
						'Hotel Vinayaga':
                                {
                                    'info': 'Vanakam! Vinayaga Hotel. Check into budget friendly hotel in India’s textile city, fondly known as the Manchester of South India. Tirupur offers a strategic blend of nature, history and industry and it exports its knitted textiles to major countries worldwide - shopping here can be a pocket-friendly and delightful experience. Walk around the town and shop!',
                                    'img': [Hotels.path()+"hotel-vinayaga-tirupur/"+str(i)+".jpg" for i in range(1,9)],
                                    'Wine':False,
									'Dine':False,
									'Event':False,
									'Package':False,
									'Book':False,
									'FAQ':False,
									'Call':True,
									'PropertyCode' : ""
                                },
			
						'Hotel Vinayaga Excellency':
                                {
                                    'info': 'Vanakam! Hotel Vinayaga Excellency. Check into budget friendly hotel in India’s textile city, fondly known as the Manchester of South India. Tirupur offers a strategic blend of nature, history and industry and it exports its knitted textiles to major countries worldwide - shopping here can be a pocket-friendly and delightful experience. Walk around the town and shop!',
                                    'img': [Hotels.path()+"hotel-vinayaga-excellency-tirupur/g"+str(i)+".jpg" for i in range(1,9)],
                                    'Wine':False,
									'Dine':False,
									'Event':False,
									'Package':False,
									'Book':True,
									'FAQ':False,
									'Call':False,
									'PropertyCode' : "ZVZR0824"
                                },
                        'Le Pebble by Poppy\'s':
                                {
                                    'info': 'Vanakam! Le Pebble by Poppy\'s. Check into budget friendly hotel in India’s textile city, fondly known as the Manchester of South India. Tirupur offers a strategic blend of nature, history and industry and it exports its knitted textiles to major countries worldwide - shopping here can be a pocket-friendly and delightful experience. Walk around the town and shop!',
                                    'img': [Hotels.path()+"hotel-le-pebble-by-poppys-tirupur/g"+str(i)+".jpg" for i in range(1,9)],
                                    'Wine':False,
									'Dine':False,
									'Event':False,
									'Package':False,
									'Book':True,
									'FAQ':False,
									'Call':False,
									'PropertyCode' : "ZZIE0327"
                                }
            },
			
			'Vellore': { 'Anukula Residency':
                {
                    'info': 'Vanakam! Poppys Hotel! Check in to the city famous for its grand forts, royal temples, and natural wonders. Hop off the Vellore’s main bus stand and lodge in to Poppys Hotel and experience the princely city ruled by many prosperous dynasties over the years contributing to its mixed and interesting cultural heritage.',
                    'img': [Hotels.path()+"mango-hill-by-poppys-pondicherrypoppys-anukula-residency-vellore/g"+str(i)+".jpg" for i in range(1,9)],
                    'Wine':False,
                    'Dine':True,
					'Event':True,
					'Package':True,
					'Book':True,
					'FAQ':True,
					'Call':False,
					'PropertyCode' :"IXZZ0523"
                }
            }
        }     
        return hotel_data