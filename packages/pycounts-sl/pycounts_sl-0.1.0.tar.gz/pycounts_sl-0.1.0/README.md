# pycounts_sl

This is a test Python package to learn python package creation process. This package includes simple functions operates on text file in Python.

## Installation

```bash
$ pip install pycounts_sl
```

## Usage

`pycounts_sl` can be used to count words in a text file and plot the top 10 most frequent words
as follows:

```python
from pycounts_sl.pycounts_sl import count_words
from pycounts_sl.plotting import plot_words
import matplotlib.pyplot as plt

file_path = "test.txt"  # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. 
Please note that this project is released with a Code of Conduct. 
By contributing to this project, you agree to abide by its terms.

## License

`pycounts_sl` was created by Steven Lio. It is licensed under the terms
of the MIT license.

## Credits

`pycounts_sl` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
