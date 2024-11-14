### Airbnb Clone
#### Description
> This is the first phase of the Airbnb Clone: the console.
> This repository holds a command interpreter and classes (i.e. BaseModel class
> and several other classes that inherit from it: Amenity, City, State, Place,
> Review), and a command interpreter. The command interpreter, like a shell,
> can be activated, take in user input, and perform certain tasks
> to manipulate the object instances.
#### How to Use Command Interpreter
---
| Commands  | Sample Usage                                  | Functionality                              |
| --------- | --------------------------------------------- | ------------------------------------------ |
| `help`    | `help`                                        | displays all commands available            |
| `create`  | `create <class>`                              | creates new object (ex. a new User, Place) |
| `update`  | `User.update('123', {'name' : 'Greg_n_Mel'})` | updates attribute of an object             |
| `destroy` | `User.destroy('123')`                         | destroys specified object                  |
| `show`    | `User.show('123')`                            | retrieve an object from a file, a database |
| `all`     | `User.all()`                                  | display all objects in class               |
| `count`   | `User.count()`                                | returns count of objects in specified class|
| `quit`    | `quit`                                        | exits                                      |
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
(hbnb) quit
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)
$ cat test_help | ./console.py
(hbnb)
```
### Environment
* Language: Python3 (version 3.8.5)
* OS: Ubuntu 20.04 LTS
* Style guidelines: [Pycodestyle 2.8.0], [Google Style Python Docstrings]
### Authors
Hassan Ahmed [@](https://www.linkedin.com/in/hassan-ahmed-77578b206/)