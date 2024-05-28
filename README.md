# Vision Telematics
The purpose of this Python console application, is to allow potential customers who have an interest in telematics, to answer a few simple questions in order to determine the best telematics product/solution to meet their needs. This directly relates to the Project 1 & 2 website (RS Vision Consulting) and will plan to build upon further in project 4 and 5 where we intend to build a complete "Telematics solution wizard" with a front and backend service. This will effectively allow potential customer to register their interest, navigate through some interactive questions / options and present product information/comparisons". This will be designed to take customers through a typical fact finding process which would normally be undertaken by a sales person in an automated way. We will also look to build a quote and potentially allow the customer to order online where currently this is not possible.

[Live version of the program](https://project03-66119f33b52f.herokuapp.com/)

<div align="center">
    <img src="assets/mockup.jpg" />
</div>

#### How to run
- Just simple question and Answer
- User will just input the numbers from the options

#### Script Functions
#### 1. `select_asset()`
- **Purpose:** Guides the user through selecting a vehicle or asset type and the reason for needing a tracking solution.
- **Input:** User selects vehicle/asset type and reason for tracking.
- **Output:** Provides a recommendation based on the user's inputs.


#### 2. `asset_tracking()`
- **Purpose:** Assists the user in selecting a tracking solution for various assets such as agricultural equipment, bins, pallets, etc.
- **Input:** User selects asset type and whether the asset is powered or unpowered.
- **Output:** Provides specific tracking recommendations based on the asset type and usage conditions.

#### 3. `vehicle_tracking()`
- **Purpose:** Helps users select tracking solutions for different vehicle types.
- **Input:** User selects vehicle type and required features.
- **Output:** Offers recommendations for tracking devices based on the selected features.

#### 4. `stolen_vehicle_or_asset_tracking()`
- **Purpose:** Provides solutions for tracking stolen vehicles or assets.
- **Input:** User selects the type of asset and any required features.
- **Output:** Recommends appropriate tracking solutions for stolen assets.

#### 5. `video_telematics()`
- **Purpose:** Guides users in selecting video telematics solutions, such as dashcams and DVR systems.
- **Input:** User selects the type of video telematics and whether an in-vehicle monitor is required.
- **Output:** Provides specific product recommendations based on user inputs.

#### 6. `select_type()`
- **Purpose:** Allows users to choose the type of telematics service they require.
- **Input:** User selects the service type (Asset Tracking, Vehicle Tracking, Stolen Vehicle & Asset Tracking, Video Telematics).
- **Output:** Calls the appropriate function based on user selection.
