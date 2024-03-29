# Dr.Forage

Explore the forest in order to forage ingredients for natural remedies to treat your patients in a post apopcalyptic world.

## Local Setup 

### Choose an IDE for development
My recommendations for code editors for development in Python are PyCharm or VSCode. I use PyCharm. If you don't have one of these IDEs, I highly recommend downloading them.

Pycharm has a free community version available for download here for Windows, Mac, and Linux: https://www.jetbrains.com/pycharm/download

VSCode is completely free and available for download here for Windosws, Mac, and Linux: https://code.visualstudio.com/Download

### Ensure you have Python 3 installed
I am using version `3.9.4` of Python. As long as you have that version or higher, you don't need to do any setup.

Here's instructions for setting up Python on Windows or Mac: https://www.datacamp.com/blog/how-to-install-python

### Clone the Repository
See the Github docs for further instruction: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

### Install the Requirements
As with any Python project, you want to insure you install the dependencies through the requirements.txt file.
In your terminal ensure you have navigated to the project folder run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`.

If you want to know more about the requirements file check out this resource: https://learnpython.com/blog/python-requirements-file/

### Setup Complete!
You Should be able to run this game from the `main.py` file on your system now.

## Controls
| Key | Description           |
|-----|-----------------------|
| W   | move character up     |
| A   | move character left   |
| S   | move character down   |
| D   | move character right  |
| E   | interact              |
| I   | toggle inventory menu |
| H   | switch between scenes |

## Game Ideas

### Basic Game Flow
1. The player gets a customer who has an ailment in your clinic. They list their symptoms and you diagnose them.
2. The player goes into to the village and ask the elders about the ailment to acquire a recipe.
3. The player goes to the forest to forage the ingredients for the remedy outlined in the recipe.
4. The player returns to the clinic and prepares the remedy with a minigame.
5. The player treats the customer and they reward the player with items and supplies.

### Other ideas
- Ghost grandma that gives you the recipe for a major illness
- Community based mechanics (different characters have different specialties and can reward you with different items when they're treated)
- Bartering system in town (so you can get supplies)


### What needs to be figured out
- Should there be stamina while foraging?
- Should there be elements of magic?
- Should there be a story line?
- Should there be educational tidbits?
- Should there be achievements?
- Should there be a setting to convert the units in recipe (metric support)?
- Should there be a guide for the plants?
- Should there be elements of farming, or other elements to the game?
- Should there be skills that can be leveled up?
- Should it be laid out in levels?

## Tasks

### In progress
- Workstation Scene (mini game to create the remedy): Lauryn

### To be picked up
- Clinic scene (customer comes in and presents with an illness or injury)
- Village scene (a village with explorable houses and npcs to get recipes from)
- Treatment scene (customer is given remedy, customer gives reward)
- Inventory persistence (how will the items from the inventory transfer between scenes?)

### Done
- Forrest scene (items in the screen that are able to be harvested and added to an inventory)


## Resources

### Coding
- Installing Python: https://www.datacamp.com/blog/how-to-install-python
- Cloning a repository from Github: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
- Python requirements file: https://learnpython.com/blog/python-requirements-file/
- Pygame documentation: https://www.pygame.org/docs/index.html
- Pygame basics: https://realpython.com/pygame-a-primer/#sprite-groups
- Pygame scene management: https://nerdparadise.com/programming/pygame/part7
- Python conventions: https://peps.python.org/pep-0008/
- Endesga 64 Palette values: https://lospec.com/palette-list/endesga-64
- 
 
### Recipes
- Ginger tea: https://cookieandkate.com/fresh-ginger-tea-recipe/