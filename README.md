# Confident-Driver
A car driving game using OPEN GL library, implementing only Midpoint Line Algorithm and Mid Circle Algorithm

---

### **1. Moving Car Lane**
- **Description**: The car lane dynamically scrolls or moves, creating the illusion of a road in motion. This effect keeps the gameplay immersive and realistic, simulating the experience of driving on a busy street or highway.
- **Implementation**: This involves a continuous movement of the background texture or lane graphics vertically (or horizontally, if the lane shifts). Speed may gradually increase to enhance the challenge as the game progresses.
- **Challenges**: Maintaining smooth movement while synchronizing with obstacles and other elements in the lane.

---

### **2. Moving Cars + Level Increase**
- **Description**: Enemy or NPC cars continuously spawn and move down the lane, simulating traffic. As the player progresses, the difficulty increases, either by introducing more cars, varying speeds, or adding challenging patterns.
- **Level Increase Dynamics**: 
  - Higher levels could introduce faster-moving cars or obstacles.
  - Spawn rates for enemy cars increase.
  - Lanes may shift unpredictably, requiring quick reflexes.

---

### **3. Shifting Lane with Mouse Click**
- **Description**: The player's car can change lanes using a mouse click. Clicking on a specific part of the screen or UI button shifts the car to the adjacent lane.
- **Interaction**:
  - **Left Click**: Move left or right depending on the cursor's position relative to the car.
  - This mechanic allows for precise control to avoid obstacles or engage with power-ups.
- **Challenges**: Ensuring the lane shift feels responsive and intuitive without causing unintended jumps between lanes.

---

### **4. Shooting Car After Refill (with Spacebar)**
- **Description**: The player's car is equipped with a cannon or weapon that can shoot bullets or projectiles. Shooting is enabled only after collecting a "refill" power-up.
- **Mechanics**:
  - Bullets can destroy enemy cars or obstacles in the player's path.
  - The cannon may have limited ammo, adding a layer of strategy to when and how to use it.
- **Refill Collection**: Refills appear as special items on the lane, and the player must maneuver their car to collect them.
- **Interaction**: Pressing the **spacebar** activates the shooting mechanic.
- **Purpose**: Adds an offensive element to gameplay, encouraging strategic play.

---

### **5. Pause Menu During Game**
- **Description**: A menu that pauses the game, allowing players to take a break or access options without losing progress.
- **Features**:
  - **Resume**: Continues the game.
  - **Restart**: Restarts the current level.
  - **Quit**: Exits to the main menu.
  - Optional settings like adjusting sound or controls.
- **Activation**: Usually bound to a key like `P` or a button on the screen.
- **Implementation**: The game stops rendering active elements, while the pause menu overlays the screen.

---

### **6. Car Collision (Game Over)**
- **Description**: If the player's car collides with an enemy car or obstacle, the game ends.
- **Mechanics**:
  - Collision detection is implemented using hitboxes or bounding boxes for all objects.
  - A collision triggers a "Game Over" screen and may include animations like car crashes or explosions.
- **Purpose**: Provides a definitive endpoint to each gameplay session, rewarding careful maneuvering.

---

### **7. Car Pass and Destroy Score (Increase)**
- **Description**: Players earn points for:
  - **Passing Cars**: Successfully dodging enemy vehicles without colliding.
  - **Destroying Cars**: Using the shooting mechanic to eliminate enemy cars.
- **Scoring System**:
  - Passing a car might add +10 points.
  - Destroying a car could add +20 points.
- **Purpose**: Encourages both evasive and offensive strategies, enhancing replayability.

---

### **8. Car Cannon Refill Option (Will Arrive on Lane)**
- **Description**: Refills appear as collectible items on the lane. These items replenish the player's ammo, enabling them to use the shooting mechanic again.
- **Appearance**:
  - Refills could be represented as glowing or distinct items to stand out on the lane.
  - They might spawn at intervals or based on player performance.
- **Challenge**: Players must maneuver carefully to collect the refill while avoiding obstacles.

---

### **9. Game Over, Scoreboard, and Restart Option**
- **Game Over Screen**:
  - Displays a message like "Game Over!" alongside the player's final score.
  - Could include animations (e.g., a crashing car or fading screen effect).
- **Scoreboard**:
  - Shows the player's performance, such as:
    - **Current Game Score**: Points earned in the session.
    - **High Score**: Best score achieved in previous games.
  - Encourages replayability by motivating players to beat their previous records.
- **Restart Option**:
  - Allows players to start a new session without returning to the main menu.
  - Ensures a smooth and frustration-free gameplay loop.

---

### Combined Gameplay Flow:
- The game starts with a moving lane and gradually introduces enemy cars.
- Players shift lanes using mouse clicks to avoid collisions and collect refills.
- Shooting becomes available after collecting refills, enabling destruction of obstacles.
- The pause menu provides breaks or options mid-game.
- Collisions trigger a "Game Over," and players can restart or check their scores.

These features collectively make for an engaging and challenging game, blending reflex-based mechanics with strategic elements. Let me know if you'd like help implementing any specific feature!
