# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pearson_pdf']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.3.2,<10.0.0', 'requests>=2.26.0,<3.0.0']

entry_points = \
{'console_scripts': ['pearson-pdf = pearson_pdf.__main__:main']}

setup_kwargs = {
    'name': 'pearson-pdf',
    'version': '1.4.0',
    'description': 'Tool to download Pearson books as PDFs.',
    'long_description': "# pearson-pdf\n\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pearson-pdf)](https://pypi.org/project/pearson-pdf/)\n[![PyPI](https://img.shields.io/pypi/v/pearson-pdf)](https://pypi.org/project/pearson-pdf/)\n[![Downloads](https://pepy.tech/badge/pearson-pdf)](https://pepy.tech/project/pearson-pdf)\n[![ci](https://github.com/jyooru/pearson-pdf/actions/workflows/ci.yml/badge.svg)](https://github.com/jyooru/pearson-pdf/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/gh/jyooru/pearson-pdf/branch/main/graph/badge.svg?token=SRK5RPLHN0)](https://codecov.io/gh/jyooru/pearson-pdf)\n[![License](https://img.shields.io/github/license/jyooru/pearson-pdf)](LICENSE)\n\nTool to download Pearson books as PDFs.\n\n## Installation\n\nInstall `pearson-pdf` using pip.\n\n```bash\npip install pearson-pdf\n```\n\n## Usage\n\nTo download a PDF, you'll need to get the book's ID:\n\n1. Open up DevTools in your browser.\n2. Navigate to Console.\n3. Type in:\n   ```js\n   window.foxitAssetURL;\n   ```\n4. Copy that URL.\n5. Download your URL as a PDF to `output.pdf` using pearson-pdf:\n   ```bash\n   pearson-pdf https://example.com/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/foxit-assets output.pdf\n   ```\n\nMore information on usage is in the help page:\n\n```bash\npearson-pdf -h\n```\n\n## License\n\nSee [LICENSE](LICENSE) for details.\n",
    'author': 'Joel',
    'author_email': 'joel@joel.tokyo',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jyooru/pearson-pdf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
