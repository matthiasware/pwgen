# pwgen

A small CLI tool for password generation.

### Usage
```sh
usage: pwgen [-h] [-l <int>] [-u <int>] [-d <int>] [-s <int>] [-i <str>] [-e <str>] <length>

positional arguments:
  <length>              password length

options:
  -h, --help                show this help message and exit
  -l <int>, --lower <int>   min amount of lower case characters
  -u <int>, --upper <int>   min amount of upper case characters
  -d <int>, --digit <int>   min amount of digits
  -s <int>, --symbol <int>  min amount of symbols
  -i <str>, --include <str> include specified characters at least once
  -e <str>, --exclude <str> exclude specified characters. Overwrites other specifications
```

### Examples

Generates password of length 10 consisting letters, symbols and digits:
```sh
pwgen 10
```

Generate password of length 10 consisting of letters and digits but no symbols: 
```sh
pwgen 10 --symbol 0
```

Generate password of length 8 consisting of letters, symbols and at least 4 digits:
```sh
pwgen 8 --digit 4
```

Generate password of length 10 consisting of letters, digits, symbols but excludes '#' and '!' symbols.
```sh
pwgen 10 --exclude '#!
```

Generate password of length 10 and explicitly includes the characters 'H', '4', 'X', 'X', 'O', 'R':
```sh
pwgen 8 --include H4XOR


### Install

After cloning, simply run
```sh
pip install .
```

