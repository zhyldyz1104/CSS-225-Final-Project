# CSS-225 Milestone 3 – Text Adventure Game

This project is a text-based adventure game inspired by *The Alchemist* by Paulo Coelho.  
The player follows Santiago’s journey through interactive story chapters, making choices that shape the outcome.  
Each chapter is implemented as a separate Python module to keep the code modular and easy to expand.

---

## 🧩 Project Structure

- `main.py` – Entry point of the game. Handles username input, chapter flow, and restart logic.
- `globalvariables.py` – Stores shared variables (like `username`, `success`) and helper functions (e.g. yes/no input validator).
- `chapter1.py` – Start in Andalusia, talk to villagers, visit the gypsy, sell sheep, and begin the journey.
- `chapter2.py` – Explore the oasis, help the Englishman, and follow the hawk’s flight.
- `chapter3.py` – Meet the chieftain and the alchemist, decide whether to accept guidance, and continue the desert journey.
- `chapter4.py` – Learn spiritual lessons, solve the alchemist’s riddles, and reach the Pyramids — or restart the game if you fail.

---

## 🕹️ How to Play

1. Make sure all `.py` files are in the same directory.
2. Run the game from the terminal:

   ```bash
   python main.py
