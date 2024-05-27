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


def asset_tracking():
    assets = {
        1: "Agricultural Tracking",
        2: "Bin / Container Tracking",
        3: "Pallet & Cage Tracking",
        4: "Plant & Equipment Tracking",
        5: "Trailer Tracking / Transport",
        6: "Trains / Rail",
        7: "Utilities: Gas, Power, Water",
        8: "Other"
    }

    print("\n")
    for k, v in assets.items():
        print(f"{k}. {v}")

    asset_tracking_choice = int(input("Please select your choice: "))
    option_dict = {
        1: "Powered",
        2: "Unpowered",
        3: "Unsure"
    }
    print("\nIs the asset you are looking to monitor powered or unpowered?")
    for k, v in option_dict.items():
        print(f"{k}. {v}")

    power_choice = int(input("Enter your choice: "))
    print("\nDo you use the asset for:")

    powered_place_option = {
        1: {
            "label": "Indoors",
            "result": ("Please call us to\n"
                       "discuss your requirements -\n"
                       "08000 82 82 00")
        },
        2: {
            "label": "Outdoors",
            "result": ("We have a number\n"
                       "of options including Dart 3,\n"
                       "G62 (LORAWAN only), G70,\n"
                       "G120. Please call a\n"
                       "member of our team to\n"
                       "discuss your requirements -\n"
                       "08000 82 82 00")
        },
        3: {
            "label": "Both Indoor & Outdoor",
            "result": ("We have a number\n"
                       "of options including Dart 3,\n"
                       "G62 (LORAWAN only), G70,\n"
                       "G120. Please call a\n"
                       "member of our team to\n"
                       "discuss your requirements -\n"
                       "08000 82 82 00")
        },
        4: {
            "label": "Fixed Location",
            "result": ("Please call us to\n"
                       "discuss your requirements -\n"
                       "08000 82 82 00")
        },
        5: {
            "label": "Other",
            "result": ("Please call us to\n"
                       "discuss your requirements -\n"
                       "08000 82 82 00")
        }
    }

    unpowered_place_option = {
        1: {
            "label": "Indoors",
            "result": ("Barra Core and any\n"
                       "of the Edge devices\n"
                       "such as Barra Edge,\n"
                       "Yabby Edge, Oyster\n"
                       "Edge - Please call a\n"
                       "member of our team to\n"
                       "discuss your requirements further -\n"
                       "08000 82 82 00")
        },
        2: {
            "label": "Outdoors",
            "result": ("We have a number\n"
                       "of options, Barra GPS,\n"
                       "Yabby 3, Oyster 3,\n"
                       "Oyster 3 Bluetooth,\n"
                       "Remora 3, Oyster 3\n"
                       "Global & Remora 3\n"
                       "Global. Please call a\n"
                       "member of our team to\n"
                       "discuss your requirements -\n"
                       "08000 82 82 00")
        },
        3: {
            "label": "Both Indoor & Outdoor",
            "result": ("Any of the Edge\n"
                       "devices such as Barra\n"
                       "Edge, Yabby Edge,\n"
                       "Oyster Edge - Please\n"
                       "call a member of\n"
                       "our team to discuss\n"
                       "your requirements further -\n"
                       "08000 82 82 00")
        },
        4: {
            "label": "Fixed Location",
            "result": ("Please call us to\n"
                       "discuss your requirements -\n"
                       "08000 82 82 00")
        },
        5: {
            "label": "Other",
            "result": ("Please call us to\n"
                       "discuss your requirements -\n"
                       "08000 82 82 00")
        }
    }

    for k, v in powered_place_option.items():
        print(f"{k}. {v['label']}")

    use_asset_choice = int(input("Enter your choice: "))
    if power_choice == 1:
        print("\n================================================")
        print(f"{powered_place_option[use_asset_choice]['result']}")
        print("==================================================\n")
    elif power_choice == 2:
        print("\n================================================")
        print(f"{unpowered_place_option[use_asset_choice]['result']}")
        print("==================================================\n")
    else:
        print("\n================================================")
        print("Please call us to\n"
              "discuss your requirements -\n"
              "08000 82 82 00")
        print("==================================================\n")


def vehicle_tracking():
    vehicles = {
        1: "Car",
        2: "Van",
        3: "Truck",
        4: "Motorcycle",
        5: "Specialist Vehicle",
        6: "Plant & Machinery",
        7: "Other"
    }
    print("\n")
    for k, v in vehicles.items():
        print(f"{k}. {v}")
    vehicle_choice = int(input("Enter your choice: "))

    print("\nDo you require any of the following features?")
    feature = {
        1: {
            "label": "Driver ID",
            "result": (
                "We have a number of options including \nDart 3, G150 Global "
                "and G70. \nPlease call a member of our team \nto  "
                "discuss your requirements - 08000 82 82 00"
            )
        },
        2: {
            "label": "Fuel Monitoring (CANBus)",
            "result": (
                "Please call us to discuss your requirements - 08000 82 82 00"
            )
        },
        3: {
            "label": "PTO Monitoring",
            "result": (
                "We have a number of options including \nDart 3, G70, G150 "
                "Global and Hawk. \nPlease call a member of our team to "
                "\ndiscuss your requirements - 08000 82 82 00"
            )
        },
        4: {
            "label": "Video Integration",
            "result": (
                "The best solution is our AD Lite S - \nPlease call a member "
                "of the team to discuss \nyour requirements further on "
                "08000 82 82 00"
            )
        },
        5: {
            "label": "Multiple options",
            "result": (
                "Please call us to discuss your requirements - 08000 82 82 00"
            )
        },
        6: {
            "label": "None of the above",
            "result": (
                "Our most cost effective solution is the \nDart 3, please"
                " call a member of our team to \ndiscuss your requirements "
                "further 08000 82 82 00"
            )
        }
    }
    for k, v in feature.items():
        print(f"{k}. {v['label']}")
    feature_choice = int(input("Enter your choice: "))
    print("\n================================================")
    print(f"{feature[feature_choice]['result']}")
    print("==================================================\n")


def stolen_vehicle_or_asset_tracking():
    asset_dict = {
        1: "Car",
        2: "Van",
        3: "Truck",
        4: "Motorcycle",
        5: "Specialist Vehicle",
        6: "Plant & Machinery",
        7: "Other",
    }

    feature = {
        1: {
            "label": "Yes",
            "result": (
                "We would recommend our SA S7 Tracking solution, \nplease "
                "contact a member of our team to discuss \nyour requirements "
                "further on 08000 82 82 00"
            )
        },
        2: {
            "label": "No",
            "result": (
                "We would recommend our Barra Egde device, \nplease contact "
                "a member of our team to \ndiscuss this further on "
                "08000 82 82 00"
            )
        },
        3: {
            "label": "Yes - Must be a CAT 5+ system",
            "result": (
                "We would recommend our SA S5+ Tracking solution, \nplease "
                "contact a member of our team to \ndiscuss your requirements "
                "further on 08000 82 82 00"
            )
        },
        4: {
            "label": "Yes - Must be a CAT 7 system",
            "result": (
                "We would recommend our SA S7 Tracking solution, \nplease "
                "contact a member of our team to \ndiscuss your requirements "
                "further on 08000 82 82 00"
            )
        },
        5: {
            "label": "Unsure",
            "result": (
                "Please call us to discuss your \nrequirements - 08000 "
                "82 82 00"
            )
        }
    }

    print("\n")
    for k, v in asset_dict.items():
        print(f"{k}. {v}")
    asset_choice = int(input("Enter your choice: "))
    print("\nDo you require any of the following features?")

    for k, v in feature.items():
        print(f"{k}. {v['label']}")
    feature_choice = int(input("Enter your choice: "))
    print("\n================================================")
    print(f"{feature[feature_choice]['result']}")
    print("==================================================\n")
    

def video_telematics():
    video_dict = {
        1: {
            "label": "Dashcam",
            "result": {
                "yes": (
                    "We would recommend AD Lite S - 4G + 1CH \nMonitor Kit. "
                    "Please call a member \nof our team on 08000 82 82 00"
                ),
                "no": (
                    "We would recommend AD Lite S - 4G. \nPlease call a member "
                    "of our \nteam on 08000 82 82 00"
                )
            }
        },
        2: {
            "label": "AI DashCam (ADAS + DMS)",
            "result": {
                "yes": (
                    "We would recommend AD Plus 2.0 - 4G + 1CH \nMonitor Kit. "
                    "Please call a member \nof our team on 08000 82 82 00"
                ),
                "no": (
                    "We would recommend AD Plus 2.0 - 4G. \nPlease call a member "
                    "of our \nteam on 08000 82 82 00"
                )
            }
        },
        3: {
            "label": "Mobile DVR",
            "result": {
                "yes": (
                    "We would recommend X1 - 5CH 4G DVR + 1CH \nMonitor Kit. "
                    "Please call a member \nof our team on 08000 82 82 00"
                ),
                "no": (
                    "We would recommend X1 - 5CH 4G DVR. \nPlease call a member "
                    "of our \nteam on 08000 82 82 00"
                )
            }
        },
        4: {
            "label": "AI Enabled DVR",
            "result": {
                "yes": (
                    "We would recommend X1 - 5CH 4G DVR + DMS + 1CH \nMonitor "
                    "Kit. Please call a member \nof our team on 08000 82 82 00"
                ),
                "no": (
                    "We would recommend X1 - 5CH 4G DVR + DMS. \nPlease call a "
                    "member of our \nteam on 08000 82 82 00"
                )
            }
        },
        5: {
            "label": "DVS 2024",
            "result": {
                "yes": (
                    "We would recommend MOS camera+side \nradar sensor + 1CH "
                    "Monitor Kit. \nPlease call a member of our team \non 08000 "
                    "82 82 00"
                ),
                "no": (
                    "We would recommend MOS camera+side \nradar sensor. Please "
                    "call a member \nof our team on 08000 82 82 00"
                )
            }
        }
    }

    asset_type = {
        1: "Car",
        2: "Van",
        3: "Truck",
        4: "Motorcycle",
        5: "Specialist Vehicle",
        6: "Plant & Machinery",
        7: "Other"
    }

    print("\n")
    for k, v in video_dict.items():
        print(f"{k}. {v['label']}")
    video_choice = int(input("Enter your choice: "))

    print("\n")
    for k, v in asset_type.items():
        print(f"{k}. {v}")
    asset_choice = int(input("Enter your choice: "))

    print("\nDo you require an in-vehicle monitor?")
    options = {
        1: "yes",
        2: "no"
    }
    for k, v in options.items():
        print(f"{k}. {v.title()}")
    option_choice = int(input("Enter your choice: "))

    print("\n================================================")
    print(f"{video_dict[video_choice]['result'][options[option_choice]]}")
    print("==================================================\n")

    print("Thank you for using our service")
