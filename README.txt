The Lost Altyn Ordo – Technical Documentation

1. Code Hosting
The code is hosted on GitHub:
https://github.com/Babaiaro/The-Lost-Altyn-Ordo

2. External Services
- No external services or APIs are used.
- The game runs fully offline in Python.

3. Languages and Technologies
- Python 3.x (tested on Python 3.13)
- Text-based, console/terminal interface

4. System Requirements
- Operating Systems: Windows, macOS, Linux
- Python 3.x installed
- Terminal or command prompt to run Python scripts

5. Coding and Naming Conventions
- Classes: PascalCase (e.g., Player)
- Functions/variables: snake_case (e.g., get_choice)
- Chapter files: modular, each chapter in a separate .py file
- Comments added to explain important parts of the code

6. How to Run / Deploy
1. Download or clone the GitHub repository.
2. Open terminal/command prompt in the project folder.
3. Run the main file to start the game:
   python main.py
4. Follow on-screen prompts to play.

7. Overview of Architecture
- main.py: Main controller that runs the game and imports chapters
- chapter1.py, chapter2.py, chapter3.py: Each chapter contains story, player choices, and logic
- player.py: Contains the Player class for storing player data
- Chapters can be tested independently using:
  if __name__ == "__main__":
      # Test this chapter independently

8. Starting the Game
- Run main.py as described above.
- Enter your name when prompted.
- Make choices in each chapter to progress through the story.
- The game ends after the final chapter, showing the outcomes of your choices.

9. Additional Notes
- No external libraries required.
- Each chapter is modular and can be modified or expanded independently.
- Input validation and loops are included to ensure smooth gameplay.
- Comments and variable names are clear for other developers or maintainers.
