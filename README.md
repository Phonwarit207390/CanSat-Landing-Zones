# SALT - Landing Zones

A [Python](https://www.python.org/) script to analyze aerial pictures using computer vision and match the outputs to GPS coordinates.

## Author

**Byron Trikkalidis**

Contact: <vtrikkalidis@gmail.com>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable) to install the **Roboflow** package ([Documentation](https://docs.roboflow.com/)). 

```bash
pip install roboflow
```

## Usage

### Input

The *`images`* folder should contain:

- the *`info.json`* file containing the required information for every picture captured (*name*, center & bottom-right corner *coordinates*, image *dimensions* in px). This file is of the following format:

```json
[
    {
        "name": "image1",
        "location": [[38.055133, 23.320294], [38.052865, 23.325891]],
        "height": 682,
        "width": 1344
    }
]
```

- the pictures captured with a *`.jpg`* extension.

> Tip: Use pictures with low resolution. For example, 500 KB.

### Output

The *`data`* folder will contain:

- the *`data.csv`* file with the GPS coordinates. This file is of the following format:

```csv
latitude,longitude
38.054009,23.317695
38.053956,23.323509
```

- the new pictures with the predictions, with a *`.jpg`* extension.

> Tip: For faster results comment line 23:
> ```python
> # result.save(f'data\{image["name"]}.jpg')
> ```
> This line saves the new picture with the predictions.

## License

[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2023 Byron Trikkalidis

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.