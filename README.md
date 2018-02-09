# unipi-python
Various quick python scripts

# Installation
To properly run the rot13 benchmarks you will need:
### NumPy
```apt install python-numpy```
### Matplotlib
```python -mpip install -U matplotlib ``` or ```apt install python3-matplotlib```

***
# Usage

#### Random Text Generator (kinda)
This script accepts only text(.txt) files.

Either as an argument like this ``` python randText.py testTexts/medtext.txt ```

or by suppling the file later(no bash autocompletion ;))
#### Integer to Roman
This script accepts only unsinged integers less than a billion..

Dont recommend surpassing 1 million..If you dont want a screen full of symbols :)

#### Rot13
The script accepts all the characters and rotates only the letters.

Ive set the fastest function as the default function but that can easily change.

#### Rot13 Benchamrks
The most interesting script in the repo (imo).

+Note: This will take more depending on cpu power but not more than 30sec.

##### Example Result of the Benchmark

![alt text](https://i.imgur.com/wFqQcHt.png "Example Run")
