# 🎮 Tetris Game – Python + Pygame Edition

Welcome to the **Tetris Game**, a retro arcade classic reimagined using **Python** and **Pygame**! This project is not just a game, but a full-fledged learning experience that blends **game logic**, **animation**, **audio integration**, and **UI design** — all wrapped in a polished, interactive interface.

---

## 🧠 Game Concept & Theory

Tetris is a **tile-matching puzzle game** where falling tetrominoes must be arranged to form complete horizontal lines. The core logic lies in:

- **Grid-based collision detection**: Ensuring that blocks stop when they hit something.
- **Shape rotation**: Achieved using matrix transformations.
- **Row clearing**: When a full row is formed, it vanishes, and all rows above it move down.
- **Increasing difficulty**: The falling speed increases as the player levels up.
- **Game over condition**: Triggered when new blocks can’t be placed at the top.

This project implements these foundational mechanisms using structured **OOP (Object-Oriented Programming)**, resulting in clean and scalable code.

---

## 🚀 Features

- 🎨 **Colorful, grid-based gameplay** with smooth animations  
- 🧱 **Tetromino shape logic** implemented via 2D arrays  
- 🔁 **Rotation and movement** with keyboard controls  
- 💥 **Particle effects** when rows are cleared  
- 🔊 **Background music and event-triggered sound effects**  
- 📈 **Score and Level tracking**, with increasing difficulty  
- 🖼️ **Custom start screen** with interactive "Start Game" button  
- ❌ **Game Over screen** with options to restart or exit  

---

## 🧩 Technologies Used

- **Python 3.x**
- **Pygame** – game loop, rendering, event handling, and audio
- **Matrix transformations** – for tetromino rotation
- **OOP principles** – for managing game state, rendering, and user interaction
- **Sound & graphics assets** – for immersive player experience

---

## 🎮 Controls

| Key         | Action                      |
|-------------|-----------------------------|
| `←`         | Move block left             |
| `→`         | Move block right            |
| `↓`         | Drop block faster           |
| `SPACE`     | Rotate current block        |
| `ENTER`     | Restart after game over     |
| `SPACEBAR`  | Exit game after game over   |

---

## 📸 Screenshots

<p align="center">
  <img src="screenshots/start_screen.png" width="300" alt="Start Screen" />
  <img src="screenshots/gameplay.png" width="300" alt="Gameplay" />
  <img src="screenshots/game_over.png" width="300" alt="Game Over Screen" />
</p>

---

## 🧪 Learning Outcomes

This project demonstrates:

- 🎯 How to build real-time, event-driven games using Python  
- 🧩 How to manage dynamic game objects and states  
- 💻 How to use Pygame for rendering, audio, and animation  
- 🔁 Game loop architecture and frame-based rendering  
- 📦 Asset loading and error handling for media files  

---

## 💡 How to Play

- The goal is to complete as many horizontal lines as possible.
- Every time a full row is created, it disappears and scores increase.
- As the score increases, the **level rises**, and the **falling speed increases**.
- The game ends when there's no room to spawn a new block.

---

## 🤝 Contribution

Feel free to fork the repo, suggest improvements, or add your own creative twist — like new sound effects, additional shapes, or different themes.

---

⭐ **Star this repository** if you enjoyed the game or learned something new from it.  
📬 Connect on GitHub to see more projects like this!
