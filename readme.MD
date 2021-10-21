## Studee populator script

This script is designed to take in a textfile written in a certain format, clean it by separating it out into different course units, and then add it to a Firebase database.

## Setup your environment

- "python3 -m venv myenv"

Activate virtualenv by using:
* Mac/Linux/OSX
- "source/myenv/bin/activate" (terminal)

* Windows
"cd \myenv\Scripts\activate.bat (cmd)

"pip install -r requirements.txt"

OR

[2]
- "pip install pipenv"
- "pipenv install


To run populator script.
Example:
"python3 populator.py filename.txt"