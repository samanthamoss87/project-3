def select_asset():
    vehicle_asset_types = {
        1: {
            "label": "Car",
            "result": {
                1: ("Direct to Question regarding S5+ or S7 and display the "
                    "relevant result"),
                2: ("We would recommend our Barra Egde device, \nplease "
                    "contact a member of our team \nto discuss this further"),
                3: ("We would recommend our Barra Egde device, \nplease "
                    "contact a member of our team \nto discuss this further "
                    "on 08000 82 82 00"),
                4: ("We would recommend a Video-bvased \nsolution such as "
                    "the AD Lite S, \nplease contact a member of our \nteam "
                    "to discuss this further on 08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        2: {
            "label": "Van",
            "result": {
                1: ("Direct to Question regarding S5+ or S7 and display the "
                    "relevant result"),
                2: ("We would recommend our Barra Egde device, \nplease "
                    "contact a member of our team \nto discuss this further "
                    "on 08000 82 82 00"),
                3: ("We would recommend our Barra Egde device, \nplease "
                    "contact a member of our team \nto discuss this further "
                    "on 08000 82 82 00"),
                4: ("We would recommend a Video-bvased \nsolution such as "
                    "the AD Lite S, \nplease contact a member of our \nteam "
                    "to discuss this further \non 08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        3: {
            "label": "Truck",
            "result": {
                1: ("Direct to Question regarding S5+ \nor S7 and display the "
                    "relevant result"),
                2: ("We would recommend our X1 5CH 4G \nDVR device, please "
                    "contact a \nmember of our team to discuss \nthis further "
                    "on 08000 82 82000"),
                3: ("We would recommend our Barra Egde \ndevice, please "
                    "contact a member \nof our team to discuss this \nfurther "
                    "on 08000 82 82 00"),
                4: ("We would recommend a Video-bvased \nsolution such as "
                    "the X1 5CH 4G \nDVR, please contact a member \nof our "
                    "team to discuss this \nfurther on 08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        4: {
            "label": "Motorcycle",
            "result": {
                1: ("Direct to Question regarding S5+ \nor S7 and display the "
                    "relevant result"),
                2: ("We would recommend our Barra Egde \ndevice, please "
                    "contact a member \nof our team to discuss this \nfurther "
                    "on 08000 82 82 00"),
                3: ("We would recommend our Dart3 Egde \ndevice, please "
                    "contact a member \nof our team to discuss this \nfurther "
                    "on 08000 82 82 00"),
                4: ("We would recommend our Dart 3 \ndevice, please contact "
                    "a member \nof our team to discuss this \nfurther on "
                    "08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        5: {
            "label": "Specialist Vehicle",
            "result": {
                1: ("Direct to Question regarding S5+ \nor S7 and display the "
                    "relevant result"),
                2: ("We would recommend our X1 5CH 4G \nDVR device, please "
                    "contact a \nmember of our team to discuss \nthis further "
                    "on 08000 82 82000"),
                3: ("We would recommend our Hawk \ndevice, please contact a "
                    "member \nof our team to discuss this \nfurther on "
                    "08000 82 82 00"),
                4: ("We would recommend our X1 5CH 4G \nDVR device, please "
                    "contact a \nmember of our team to discuss \nthis further "
                    "on 08000 82 82000"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        6: {
            "label": "Plant & Machinery",
            "result": {
                1: ("Direct to Question regarding S5+ \nor S7 and display the "
                    "relevant result"),
                2: ("We would recommend our Barra Egde \ndevice, please "
                    "contact a member \nof our team to discuss this \nfurther "
                    "on 08000 82 82 00"),
                3: ("We would recommend our Dart3 Egde \ndevice, please "
                    "contact a member \nof our team to discuss this \nfurther "
                    "on 08000 82 82 00"),
                4: ("We would recommend a Video-bvased \nsolution such as "
                    "the AD Lite S, \nplease contact a member of our \nteam "
                    "to discuss this further \non 08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        7: {
            "label": "Agricultural Tracking",
            "result": {
                1: ("Direct to Question regarding S5+ \nor S7 and display the "
                    "relevant result"),
                2: ("We would recommend our Barra Egde \ndevice, please "
                    "contact a member \nof our team to discuss this \nfurther "
                    "on 08000 82 82 00"),
                3: ("We would recommend our Hawk \ndevice, please contact a "
                    "member \nof our team to discuss this \nfurther on "
                    "08000 82 82 00"),
                4: ("We would recommend a Video-bvased \nsolution such as "
                    "the AD Lite S, \nplease contact a member of our \nteam "
                    "to discuss this further \non 08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        8: {
            "label": "Bin / Container Tracking",
            "result": {
                1: ("We would recommend the Oyster3 \nBluetooth® please "
                    "contact a \nmember of our team to discuss \nthis further "
                    "on 08000 82 82 00"),
                2: ("We would recommend the Oyster3 \nBluetooth® please "
                    "contact a \nmember of our team to discuss \nthis further "
                    "on 08000 82 82 00"),
                3: ("We would recommend the Oyster3 \nBluetooth® please "
                    "contact a \nmember of our team to discuss \nthis further "
                    "on 08000 82 82 00"),
                4: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        9: {
            "label": "Pallet & Cage Tracking",
            "result": {
                1: ("Direct to Question regarding S5+ \nor S7 and display the "
                    "relevant result"),
                2: ("We would recommend our Barra Egde \ndevice, please "
                    "contact a member \nof our team to discuss this \nfurther "
                    "on 08000 82 82 00"),
                3: ("We would recommend our Barra Egde \ndevice, please "
                    "contact a member \nof our team to discuss this \nfurther "
                    "on 08000 82 82 00"),
                4: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        10: {
            "label": "Plant & Equipment Tracking",
            "result": {
                1: ("Direct to Question regarding S5+ \nor S7 and display the "
                    "relevant result"),
                2: ("We would recommend a Video-bvased \nsolution such as "
                    "the AD Lite S + \nBarra Edge, please contact a \nmember "
                    "of our team to discuss \nthis further on 08000"),
                3: ("We would recommend a Video-bvased \nsolution such as "
                    "the AD Lite S, \nplease contact a member of our \nteam "
                    "to discuss this further \non 08000 82 82 00"),
                4: ("We would recommend a Video-bvased \nsolution such as "
                    "the AD Lite S, \nplease contact a member of our \nteam "
                    "to discuss this further \non 08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        11: {
            "label": "Trailer Tracking / Transport",
            "result": {
                1: ("Direct to Question regarding S5+ \nor S7 and display the "
                    "relevant result"),
                2: ("We would recommend our X1 5CH 4G \nDVR + Barra Edge "
                    "device, please \ncontact a member of our team to "
                    "\ndiscuss this further on 08000 \n82 82000"),
                3: ("We would recommend our X1 5CH 4G \nDVR device, please "
                    "contact a \nmember of our team to discuss \nthis further "
                    "on 08000 82 82000"),
                4: ("We would recommend our X1 5CH 4G \nDVR device, please "
                    "contact a \nmember of our team to discuss \nthis further "
                    "on 08000 82 82000"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        12: {
            "label": "Trains / Rail",
            "result": {
                1: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                2: ("We would recommend a Video-bvased \nsolution such as "
                    "the X7 Pro, \nplease contact a member of our \nteam to "
                    "discuss this further \non 08000 82 82 00"),
                3: ("We would recommend our Hawk device, \nplease contact a "
                    "member of our \nteam to discuss this further \non 08000 "
                    "82 82 00"),
                4: ("We would recommend a Video-bvased \nsolution such as "
                    "the X7 Pro, \nplease contact a member of our \nteam to "
                    "discuss this further \non 08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        13: {
            "label": "Utilities, gas, power, water",
            "result": {
                1: ("Direct to Question regarding S5+ \nor S7 and display the "
                    "relevant result"),
                2: ("We would recommend our Barra Egde \ndevice, please "
                    "contact a member \nof our team to discuss this \nfurther "
                    "on 08000 82 82 00"),
                3: ("We would recommend our Barra Egde \ndevice, please "
                    "contact a member \nof our team to discuss this \nfurther "
                    "on 08000 82 82 00"),
                4: ("We would recommend a Video-bvased \nsolution such as "
                    "the AD Lite S, \nplease contact a member of our \nteam "
                    "to discuss this further \non 08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        },
        14: {
            "label": "Other",
            "result": {
                1: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                2: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                3: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                4: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                5: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00"),
                6: ("Please call us to discuss your \nrequirements - "
                    "08000 82 82 00")
            }
        }
    }

    reason_dict = {
        1: "Insurance requirement",
        2: "Protect from theft",
        3: "Monitor utilisation",
        4: "Improve Driver behaviour",
        5: "Regulatory requirement",
        6: "Other"
    }
    print("\n")
    for k, v in vehicle_asset_types.items():
        print(f"{k}. {v['label']}")
    asset_type = int(input("\nSelect your vehicle or asset type: "))
    for k, v in reason_dict.items():
        print(f"{k}. {v}")
    reason_input = int(
        input("\nWhat is the reason you are looking for a tracking solution?\n"
              "Select a number: ")
    )

    print("\n================================================")
    print(f"{vehicle_asset_types[asset_type]['result'][reason_input]}")
    print("==================================================\n")
