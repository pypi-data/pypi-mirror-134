## Num Text
#### A Python Package to convert Numbers to Text.

[
![PyPI](https://img.shields.io/pypi/v/numtext)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/numtext)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/numtext)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/numtext)
![PyPI - Status](https://img.shields.io/pypi/status/numtext)
![PyPI - Downloads](https://img.shields.io/pypi/dm/numtext?color=Green&label=pipy%20downloads)
](https://pypi.org/project/numtext/)

[
![Github Username](https://img.shields.io/badge/Github%20Username-insumanth-brightgreen&logo=github)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/insumanth/numtext)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/insumanth/numtext?include_prereleases)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/insumanth/numtext)
![GitHub top language](https://img.shields.io/github/languages/top/insumanth/numtext)
![GitHub language count](https://img.shields.io/github/languages/count/insumanth/numtext)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/insumanth/numtext?label=Github%20Code%20SIze)
![GitHub repo size](https://img.shields.io/github/repo-size/insumanth/numtext?label=Github%20Repo%20Size)
](https://github.com/insumanth/numtext)



### Installation :

    pip install numtext

### Details :
Convert any whole number to text.

### Dependency :
This package is developed without any third party dependency. It uses `re` library which is built into python. Other features are implemented in pure python.

### Examples :

#### Module Examples
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

#### CLI Examples

```bash
$ numtext 123
```
One hundred and twenty three

```bash
$ numtext 987654321
```
nine hundred and eighty seven million six hundred and fifty four thousand three hundred and twenty one

```bash
$ numtext 56789 --capitalize
```
Fifty six thousand seven hundred and eighty nine

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
