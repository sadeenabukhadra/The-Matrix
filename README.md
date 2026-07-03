# The-Matrix
The goal of this project  is creating ecosystem in python. 

# Content

[EX1](#EX1)

[EX2](#EX2)


# EX1
It includes a program that check if the system is inside virtual enviroment (venv) or outside it .
 by : 
 | Element                         | What it represents                           | Example (outside venv)   | Example (inside venv)              | Why we use it                              |
| ------------------------------- | -------------------------------------------- | ------------------------ | ---------------------------------- | ------------------------------------------ |
| `sys.prefix`                    | Current Python environment path              | `/usr` or `C:\Python311` | `/home/user/matrix_env`            | Shows where Python is currently running    |
| `sys.base_prefix`               | Original system Python installation path     | `/usr`                   | `/usr`                             | (constant) reference for comparison              |
| `sys.prefix != sys.base_prefix` | Checks if inside a virtual environment       | False                    | True                               | Detects whether environment is isolated    |
| `sys.executable`                | Path to the Python interpreter being used    | `/usr/bin/python3`       | `/home/user/matrix_env/bin/python` | Shows which Python is executing the script |
| `os.path.basename(sys.prefix)`  | Extracts only the environment name from path | `usr` (not useful)       | `matrix_env`                       | Gets clean venv name only                  |
| `sys.prefix (printed)`          | Full current environment path                | `/usr`                   | `/home/user/matrix_env`            | Displays full active environment location  |
| `os.path`                       | Module for path manipulation                 | —                        | —                                  | Used to handle file/system paths properly  |


so we know if the program inside the venv :

               if sys.prefix != sys.base_prefix:
                       print("Inside virtual environment")
               else:
                       print("Outside virtual environment")


# EX1
The goals of this exercise :
1) How to install dependencies ?
2) How to check if they are installed ?
3) How to tell the user what to do if the missing ?
4) How to describe  dependencies  using pip nad poetory?


Dependency Management
- pip
Default Python package manager
Installs packages from PyPI
Uses requirements.txt

Example:

           pip install -r requirements.txt

- Poetry
Modern dependency manager
Handles virtual environments automatically
Uses pyproject.toml and poetry.lock

Example:

       poetry install
   


