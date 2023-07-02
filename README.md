# KeeneticRCI

Python library for remote code execution on Keenetic devices using RCI.

## **Warning!**

- **All commands may not be available.**
- **Any kind of special character (Ex: #@~!$%^:&) will probably break the script/result in failing to run the command.**

## Installation

This package is not available at PyPi for now.

```sh
git clone https://github.com/AlperShal/KeeneticRCI
cd KeeneticRCI
pip install .
```

## How to use

```py
#Import the library
import KeeneticRCI

#Initialize connection to router and authenticate
router = KeeneticRCI.router(user="YOUR_USER", password="YOUR_PASS", ip="IP/DOMAIN_TO_YOUR_ROUTER")

#Run your command
router.run("show version")
```

```py
#One line command
KeeneticRCI.router(user="YOUR_USER", password="YOUR_PASS", ip="IP/DOMAIN_TO_YOUR_ROUTER").run("show version")
```

Built on/forked from [keyiflerolsun/KeeneticPy](https://github.com/keyiflerolsun/KeeneticPy). Huge thanks for the awesome work.
