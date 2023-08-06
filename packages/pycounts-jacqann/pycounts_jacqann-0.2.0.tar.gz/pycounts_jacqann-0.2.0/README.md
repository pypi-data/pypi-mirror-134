# pycounts_jacqann

Calculate word counts in a text file!

## Installation

```bash
$ pip install pycounts_jacqann
```

## Usage

`pycounts_jacqann` can be used to count words in a text file and plot the results as follows:

```bash
from pycounts_jacqann.pycounts import count_words
from pycounts_jacqann.plotting import plot_words
import mathplotlib.pyplot as plt

file_path = "test.txt"
counts = count_words(file_path)
fig = plot_words(counts, n=10_
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pycounts_jacqann` was created by Jacqueline Chong. It is licensed under the terms of the MIT license.

## Credits

`pycounts_jacqann` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
