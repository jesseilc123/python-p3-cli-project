# Minecraft Database CLI Program

### DISCLAIMER

This project was created for the end-of-phase Phase-3 Project requirement at Flatiron School.The data within the project is fictional and does not correlate to any real player, world, or server relating to minecraft. The purpose of the project is to demonstrate my skills learned within Python and sqlalchemy.

## Description 

The purpose of this CLI (Command Line Interface) program is to provide a convenient and efficient way to interact with a Minecraft database. It allows users to view various data pieces such as players, worlds, and servers as well as view their relations between each other. It also allows users to add new players, worlds, and servers in an easy and safe way (through data validation).

## Installation

To install any necessary packages and enter the virtual environment, type the follow command:

```pipenv install && pipenv shell```

After all packages have installed and you've entered the virtual environment, navigate to the `lib` folder using the following command:

```cd lib/```

Finally, enter the CLI using the following command:

```python cli.py```

To seed data in the database make sure you are not in the CLI. You can exit using `CTRL + D` or follow the prompts given. Then navigate to the db file by using the following command:

from `python-p3-cli-project`
```cd lib/db/```
from `lib`:
```cd db/```

Finally seed the data using the following command:
```python seed.py```

## Usage

Usage of the CLI program was intended to be simple and straightforward. Instructions are provided in each menu to help guide you. With the use of data validation, incorrect keystrokes will not break the program or database. The 'Main Menu' holds 4 options; access sub menus such as 'Player menu', 'World menu', 'Server menu', or quit the program. In each sub menu there are 4 options (data is dependant on menu; player, world, server); display all the data, lookup data by name, add data to the database, or go back to the main menu. When you lookup data by name, you have the option to see related data applied to it. 

## lib

**--cli.py--**

`cli.py` is the main file which actually runs the script. In this file you will find 2 supporting files which are imported from `helpers.py` and `sub_menu_helpers.py`. `helpers.py` was intended to keep code DRY so we will discuss it later. The main function of `cli.py` is `main_menu()`. This function sets a while loop to run the program until the user selects 4. Once 4 is selected the while loop ends and the program is terminated. Depending on the other numbers selected by the user (1, 2, or 3) they will be directed to a new menu known as a sub menu through the `sub_menu()` function. If the user enters a keystroke that is not 1, 2, 3, or 4 they will be presented with an error however, the while loop will not break and will remain in `main_menu()`. 

The `sub_menu()` function takes 2 arguments as its parameters; a `category` and `data_list`. The category will match the data being passed down. `sub_menu()` holds another while loop where if the user selects 4 the loop will break and they will be directed to the `main_menu()`. Depending on the number the user selects, a different function will be called. If the user enters a key that is not 1, 2, 3, or 4 they will be presented with an error however, the while loop will not break and will remain in the `sub_menu()`.

**--sub_menu_helpers.py--**

Option 1 calls the function `display_all()` which takes 2 parameters; a `category` and `data_list`. This function will query the data and display all the data depending on the `sub_menu()` selected; player, world, or server. The user will then be prompted to continue or go back to the `main_menu()`. Selecting to return to the `main_menu()` will result in the  loop breaking. Otherwise the `sub_menu()` while loop will continue.

Option 2 calls one of the following functions depending on the `category`; `search_for_players()`, `search_for_worlds()`, `search_for_servers()`. All 3 take 2 parameters; a `data_list` and a `search_name`. 

The `search_for_players()` function will query the players table for any matching results to `search_name`. Since player usernames should be unique, the query will return the first result. If no matches are found in the database the interface will prompt the user no matches found breaking the loop and returning to the `sub_menu()`. If a match is found, the user will enter another while loop. This loop gives the user 3 options; exit to `sub_menu()`, see related worlds, or see related servers. If any unexpected key strokes occur the user will be presented with an error however, the loop will not break. `0` will break the loop(exit). `1` will query player.worlds and display any related worlds. If no results are found the user will be prompted. Both result in the loop breaking. `2` will query player.servers and display any related servers. If no results are found the user will be prompted. Both result in the while loop breaking. 

The `search_for_worlds()` function will query the worlds table for any matching results to `search_name`. Since world names should be unique, the query will return the first result. If no matches are found in the database the interface will prompt the user no matches found, breaking the loop and returning to the `sub_menu()`. If a match is found, the user will enter another while loop. This loop gives the user 3 options; exit to `sub_menu()`, see related players, or see related servers. If any unexpected keystrokes occur the user will be presented with an error however, the loop will not break. `0` will break the loop(exit). `1` will query world.players and display any related players. If no results are found the user will be prompted. Both result in the while loop breaking. `2` will query world.servers and display any related servers. If no results are found the user will be prompted. Both result in the while loop breaking.

The `search_for_servers()` function function will query the servers table for any matching results to `search_name`. The first server is returned. If no matches are found in the database the interface will prompt the user no matches found, breaking the loop and returning to the `sub_menu()`. If a match is found, the user will enter another while loop. This loop gives the user 3 options; exit to `sub_menu()`, see related players, or see related worlds. If any unexpected key strokes occur the user will be presented with an error however, the loop will not break. `0` will break the loop(exit). `1` will query the server database and grab all `server.player_id`'s then query the players table for all matching id's. If no results are found the user will be prompted.`2` will query the server database and grab all `server.world_id`'s then query the players table for all matching id's. If no results are found the user will be prompted.

Option 3 from the `sub_menu()` calls one of the following functions depending on the category: `add_to_player()`, `add_to_world()`, `add_to_server()`. These functions do not take any parameters. All 3 functions add a new item to their respective tables. Each question enters the user into a while loop. If the user enters information that satisfies the requirements of the question the while loop breaks and the next question is prompted. This happens until all questions have been answered and then the user is prompted with the item they added and return to the `sub_menu()`. If at any point the user enters inputs anything that do not satisfy the question's requirements, the user will be prompted invalid input and the while loop will not break until the inputs satisfy the requirements. 

**--helper.py--**

`helper.py` has many functions that aim to reduce repetition and keep code DRY. 

`logo()` and `closing_logo()` simply prints ascii art. 

`closing_tag()` return's the a nice UI when the user quits the program.

`main_menu_options()` print's the main menu options. This helps reduce clutter in `cli.py`.

`sub_menu_options` takes `category` as a parameter and print's the sub menu options. Sub menu depends on `category`.

`loading()` creates the illusion the program is loading. 

`no_matches_found()` is called every time no matches are found in queries.

`invalid_input()` is called every time the user inputs an invalid input.

`print_players()`, `print_worlds()`, and `print_servers()` all take `data` as a parameter. When called they print out the `data` in a uniform and consistent way. 

`disclaimer_for_add_to_server()` simply print's instructions when the user adds a server. Reduces clutter in `sub_menu_helpers.py`.


## lib/db

**--debug.py--**

The purpose of this file is to allow you to debug your database when changes are made. Imports are necessary to query the database using sqlalchemy. You can run commands such as `session.query().all` to view items in your database.

**--models.py--**

The purpose of this file is to set up tables for your database. It also sets up a relationship between all tables using `relationship` and `association_proxy`. Server serves as a join table for Player and World. Through Servers many players can be in many worlds and many worlds can have many players. A Server can also hold many worlds and many players. 

**--seed.py--**

The purpose of this file is to seed your database in order to reset it or fill it with data if none is present. By using `faker` and `random` much of the data is random. Players are limited to 30, worlds are limited to 15, servers are limited to 2. However through `cli.py` and `debug.py` you can add more if you choose to.

## Conclusion
If you want to use this project feel free too just fork and clone it. If you have any recommendations please feel free to send them my way. Thanks!

| [linkedin](https://www.linkedin.com/in/jesse-ilc-se2023/) | [blog](https://dev.to/jesseilc123) |
