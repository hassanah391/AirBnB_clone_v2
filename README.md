### Airbnb Clone

#### Description
This repository holds a command interpreter and classes for an Airbnb clone project. The command interpreter, similar to a shell, can be activated to take user input and perform tasks to manipulate object instances.

#### Command Interpreter Usage

| Command | Sample Usage | Functionality |
| --- | --- | --- |
| `help` | `help` | Displays all available commands |
| `create` | `create <class>` | Creates a new object (e.g., User, Place) |
| `update` | `User.update('123', {'name': 'Greg_n_Mel'})` | Updates an object's attribute |
| `destroy` | `User.destroy('123')` | Deletes a specified object |
| `show` | `User.show('123')` | Retrieves an object from a file or database |
| `all` | `User.all()` | Displays all objects in a class |
| `count` | `User.count()` | Returns the count of objects in a specified class |
| `quit` | `quit` | Exits the command interpreter |

#### Installation
```
git clone git@github.com:hassanah391/AirBnB_clone.git
cd AirBnB_clone
```

#### Usage
Interactive Mode:
```
$ ./console.py
(hbnb) help
(hbnb) quit
```

Non-Interactive Mode:
```
$ echo "help" | ./console.py
(hbnb)
$ cat test_help | ./console.py
(hbnb)
```

### Environment
- Language: Python3 (version 3.8.5)
- OS: Ubuntu 20.04 LTS
- Style guidelines: [Pycodestyle 2.8.0], [Google Style Python Docstrings]

### Author
Hassan Ahmed [@](https://www.linkedin.com/in/hassan-ahmed-77578b206/)
