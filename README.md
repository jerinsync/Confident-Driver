# Course: CSE423 Computer Graphics
## Semester: Fall 2024
# Confident-Driver
A car driving game using OPEN GL library, implementing only Midpoint Line Algorithm and Mid Circle Algorithm.

---

### Moving Car Lane
- **Description**: The car lane dynamically scrolls or moves, creating the illusion of a road in motion. This effect keeps the gameplay immersive and realistic, simulating the experience of driving on a busy street or highway.
- **Implementation**: This involves a continuous movement of the background texture or lane graphics vertically (or horizontally, if the lane shifts). Speed may gradually increase to enhance the challenge as the game progresses.


---

### Moving Cars + Level Increase
- **Description**: Enemy or NPC cars continuously spawn and move down the lane, simulating traffic. As the player progresses, the difficulty increases, either by introducing more cars, varying speeds, or adding challenging patterns.
- **Level Increase Dynamics**: 
  - Higher levels could introduce faster-moving cars or obstacles.
  - Spawn rates for enemy cars increase.
  - Lanes may shift unpredictably, requiring quick reflexes.

---

### Shifting Lane with Mouse Click
- **Description**: The player's car can change lanes using a mouse click. Clicking on a specific part of the screen or UI button shifts the car to the adjacent lane.
- **Interaction**:
  - **Left Click**: Move left or right depending on the cursor's position relative to the car.
  - This mechanic allows for precise control to avoid obstacles or engage with power-ups.

---

### Shooting Car After Refill (with Spacebar)
- **Description**: The player's car is equipped with a cannon or weapon that can shoot bullets or projectiles. Shooting is enabled only after collecting a "refill" power-up.
- **Mechanics**:
  - Bullets can destroy enemy cars or obstacles in the player's path.
- **Refill Collection**: Refills appear as special items on the lane, and the player must maneuver their car to collect them.
- **Interaction**: Pressing the **spacebar** activates the shooting mechanic.
---

### Pause Menu During Game
- **Description**: A menu that pauses the game, allowing players to take a break or access options without losing progress.
- **Features**:
  - **Resume**: Continues the game.
  - **Restart**: Restarts the current level.
  - **Quit**: Exits to the main menu.


---

### Car Collision (Game Over)
- **Description**: If the player's car collides with an enemy car or obstacle, the game ends.
- **Mechanics**:
  - Collision detection is implemented using bounding boxes for all objects.
  - A collision triggers a "Game Over" screen and may include animations like car crashes or explosions.


---

### Car Pass and Destroy Score (Increase)
- **Description**: Players earn points for:
  - **Passing Cars**: Successfully dodging enemy vehicles without colliding.
  - **Destroying Cars**: Using the shooting mechanic to eliminate enemy cars.
- **Scoring System**:
  - Passing a car might add +10 points.
  - Destroying a car could add +20 points.


---

### Car Cannon Refill Option (Will Arrive on Lane)
- **Description**: Refills appear as collectible items on the lane.


