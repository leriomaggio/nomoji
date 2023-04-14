# NoMoJi

`NoMoJi` (Number-Emoji) is a simple and silly Python package to print integer numbers using Emoji digits.

Plus there is also a fancy `GAME_DIE` to use for apps like [`dnd-roller`](https://github.com/leriomaggio/dnd-roller).

This project is used as part of the PyConUS tutorial **Publishing your Python project, the conda way** 
presented at [PyConUS](https://us.pycon.org/2023/schedule/presentation/94/) by:

* [Dave Clements](https://us.pycon.org/2023/speaker/profile/108/)
* [Bianca Henderson](https://us.pycon.org/2023/speaker/profile/75/)
* [Mahe Iram Khan](https://us.pycon.org/2023/speaker/profile/166/)
* [Valerio Maggio](https://us.pycon.org/2023/speaker/profile/109/)

This package will be published on PyPi and it will be used solely
to demonstrate how to add `pip` dependecies to a `conda` package.

### Usage

```python
from nomoji import emojize

emojize(2)
```
This would produce 2️⃣ (the number as keypad emoji).

Similarly:
```Python
emojize(10)
```
would generate the 🔟 emoji unicode character, while:
```Python
emojize(24)
```
would result in 2️⃣4️⃣.
