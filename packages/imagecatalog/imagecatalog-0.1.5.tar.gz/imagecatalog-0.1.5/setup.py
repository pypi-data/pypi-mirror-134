# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['imagecatalog']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.0.0,<10.0.0', 'fpdf2>=2.4.6,<3.0.0']

entry_points = \
{'console_scripts': ['imagecatalog = imagecatalog.__main__:main']}

setup_kwargs = {
    'name': 'imagecatalog',
    'version': '0.1.5',
    'description': 'Create a PDF contact sheet from a set of images',
    'long_description': '# imagecatalog\n\n[![Docs](https://img.shields.io/readthedocs/imagecatalog.svg?color=green)](https://imagecatalog.readthedocs.io/en/latest/)\n[![PyPI](https://img.shields.io/pypi/v/imagecatalog.svg?color=green)](https://pypi.org/project/imagecatalog)\n[![Python Version](https://img.shields.io/pypi/pyversions/imagecatalog.svg?color=green)](https://python.org)\n[![License](https://img.shields.io/pypi/l/imagecatalog.svg?color=green)](https://github.com/tdmorello/imagecatalog/raw/main/LICENSE)\n[![codecov](https://codecov.io/gh/tdmorello/imagecatalog/branch/main/graph/badge.svg)](https://codecov.io/gh/tdmorello/imagecatalog)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)\n<!-- [![tests](https://github.com/tdmorello/imagecoverage/workflows/tests/badge.svg)](https://github.com/tdmorello/imagecoverage/actions) -->\n\nCreate a PDF contact sheet from a list of files.\n\n## Installation\n\nInstall from PyPI\n\n```bash\npip install imagecatalog\n```\n\nor get latest dev version from GitHub.\n\n```bash\npip install git+https://github.com/tdmorello/imagecatalog.git\n```\n\n---\n\n## Usage\n\n### Command line\n\n```bash\nimagecatalog -h\n```\n\n```bash\nimagecatalog -i images/ -f \'*.png\' --title \'Image Catalog\' example.pdf\n```\n\n[PDF output](https://github.com/tdmorello/imagecatalog/blob/main/resources/example.pdf)\n\n```bash\nimagecatalog   \\\n    -i images/ \\\n    -f \'*.png\' \\\n    --rows 2   \\\n    --cols 4   \\\n    --orientation landscape \\\n    --title \'Image Catalog\' \\\n    example_landscape.pdf\n```\n\n[PDF output](https://github.com/tdmorello/imagecatalog/blob/main/resources/example_landscape.pdf)\n\nFile paths and metadata can also be supplied from a csv file with headers "image", "label", "note"\n\n```bash\n$ head -n5 sample.csv\nimage,label,note\nimages/image_00.png,Image 0,image 0 note\nimages/image_01.png,Image 1,image 1 note\nimages/image_02.png,Image 2,image 2 note\nimages/image_03.png,Image 3,image 3 note\n```\n\n```bash\nimagecatalog --csv sample.csv --title \'Image Catalog from CSV\' example_csv.pdf\n```\n\n[PDF output](https://github.com/tdmorello/imagecatalog/blob/main/resources/example.pdf)\n\n---\n\n### Scripting\n\n```python\nfrom imagecatalog import Catalog\n\n# Catalog inherits from FPDF\n# see https://github.com/PyFPDF/fpdf2 for more methods\ncatalog = Catalog()\n\n# optionally add a title\ncatalog.set_title("Image Catalog")\n\n# grab a set of existing images from a local directory\nimages = [f"images/image_{i:02}.png" for i in range(12)]\n\n# optionally add labels (defaults to filenames)\nlabels = [f"Image {i}" for i in range(len(images))]\n\n# optionally add notes\nnotes = [f"note for image {i}" for i in range(len(images))]\n\n# generate the pdf\ncatalog.add_page()\ncatalog.build_table(images, labels, notes, rows=4, cols=3)\n\n# save\ncatalog.output("example.pdf")\n```\n\n---\n\n## Contributions\n\n`imagecatalog` uses `poetry` for building and package management. Pull requests are welcome.\n',
    'author': 'Tim Morello',
    'author_email': 'tdmorello@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
