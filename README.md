# Airbnb Clone - Console

## Description

> This project is the first phase of the Airbnb Clone, focusing on the backend console. The repository contains a command-line interpreter that serves as a management tool for different class instances, simulating the basic functionalities of a database.The core class, `BaseModel`, provides shared
functionality for a variety of subclass models (`Amenity`, `City`, `State`, `Place`, `Review`), allowing for instance creation, updating, and deletion through simple commands.

## Features

- **Object Persistence**: Save, load, and manage object instances.
- **Command Interpreter**: An interactive and non-interactive interpreter that mimics a Unix shell for object manipulation.
- **Class Models**: Built-in support for essential classes with unique attributes and relationships.

## Command Interpreter Usage

| Command     | Example Usage                                   | Description                                 |
|-------------|-------------------------------------------------|---------------------------------------------|
| `help`      | `help`                                          | Lists all available commands                |
| `create`    | `create <class>`                                | Creates a new instance of a class (e.g., `User`, `Place`)  |
| `update`    | `<class>.update('<id>', {'attribute': 'value'})`| Updates an attribute of an object           |
| `destroy`   | `<class>.destroy('<id>')`                       | Deletes a specific object                   |
| `show`      | `<class>.show('<id>')`                          | Shows an object's details                   |
| `all`       | `<class>.all()`                                 | Lists all instances of a specified class    |
| `count`     | `<class>.count()`                               | Displays the count of class instances       |
| `quit`      | `quit`                                          | Exits the command interpreter               |

#### Installation
```
git clone git@github.com:hassanah391/AirBnB_clone.git
cd AirBnB_clone
```
#### Usage
Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Environment
* Language: Python3 (version 3.8.5)
* OS: Ubuntu 20.04 LTS
* Style guidelines: [Pycodestyle 2.8.0](https://pycodestyle.pycqa.org/en/2.8.0/)

### Authors
Hassan Ahmed (https://x.com/hassan357753)
