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

or by supplying the file later(no bash auto-completion ;))
***
#### Integer to Roman
This script accepts only unsigned integers less than a billion..

Don't recommend surpassing 1 million..If you don't want a screen full of symbols :)

Note:Windows don't like that unicode..Don't run on Windows..
***
#### Rot13
The script accepts all the characters and rotates only the letters.

I've set the fastest function as the default function but that can easily change.
***
#### Rot13 Benchmarks
The most interesting script in the repo (imo).

+Note: This will take more depending on cpu speed but no more than 30sec.

##### Example Result of the Benchmark

![alt text](https://i.imgur.com/wFqQcHt.png "Example Run")
