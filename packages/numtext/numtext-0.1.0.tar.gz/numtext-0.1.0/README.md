## Num Text
#### A Python Package to convert Numbers to Text.

### Installation :

    pip install numtext

### Details :
Convert any whole number to text.

### Dependency :
This package is developed without any third party dependency. It uses `re` library which is built into python. Other features are implemented in pure python.

### Examples :
```python
import numtext as nt

a_big_number = 123456789
a_big_number_in_text = nt.convert(a_big_number)
print(a_big_number_in_text)
# nine hundred and eighty seven million six hundred and
# fifty four thousand three hundred and twenty one
```
```python
import numtext as nt

tiny_number = "12"  # Number can also be in string
tiny_number_text = nt.convert(tiny_number)
print(tiny_number_text) # twelve
```

### Roadmap :
This package is still in active development. More features will be added frequently.

### Features Yet to be added :
1. Support for numbers above `Nine hundreden and Ninty Nine Duotrigintillion (999 x 10^99)`.
2. Support for Negative Number.
3. Conversion in Indian System.
4. Support for Fractional numbers.
5. Better Exceptional Handling.
6. Text Formatting Options like lowercase, capitalize etc., for converted text.
7. < I would like to hear your advice on what feature to add  >
