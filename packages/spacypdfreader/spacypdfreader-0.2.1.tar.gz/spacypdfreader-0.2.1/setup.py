# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spacypdfreader', 'spacypdfreader.parsers']

package_data = \
{'': ['*']}

install_requires = \
['pdfminer.six>=20211012,<20211013',
 'rich>=10.15.2,<11.0.0',
 'spacy>=3.0.0,<4.0.0']

extras_require = \
{'pytesseract': ['pytesseract>=0.3.8,<0.4.0',
                 'Pillow>=8.4.0,<9.0.0',
                 'pdf2image>=1.16.0,<2.0.0']}

setup_kwargs = {
    'name': 'spacypdfreader',
    'version': '0.2.1',
    'description': 'A PDF to text extraction pipeline component for spaCy.',
    'long_description': '# spacypdfreader\n\nEasy PDF to text to *spaCy* text extraction in Python.\n\n<p>\n    <a href="https://pypi.org/project/spacypdfreader" target="_blank">\n        <img src="https://img.shields.io/pypi/v/spacypdfreader?color=%2334D058&label=pypi%20package" alt="Package version">\n    </a>\n    <a href="https://github.com/SamEdwardes/spacypdfreader/actions/workflows/pytest.yml" target="_blank">\n        <img src="https://github.com/SamEdwardes/spacypdfreader/actions/workflows/pytest.yml/badge.svg" alt="pytest">\n    </a>\n</p>\n\n<hr></hr>\n\n**Documentation:** [https://samedwardes.github.io/spacypdfreader/](https://samedwardes.github.io/spacypdfreader/)\n\n**Source code:** [https://github.com/SamEdwardes/spacypdfreader](https://github.com/SamEdwardes/spacypdfreader)\n\n**PyPi:** [https://pypi.org/project/spacypdfreader/](https://pypi.org/project/spacypdfreader/)\n\n**spaCy universe:** [https://spacy.io/universe/project/spacypdfreader](https://spacy.io/universe/project/spacypdfreader)\n\n<hr></hr>\n\n*spacypdfreader* is a python library for extracting text from PDF documents into *spaCy* `Doc` objects. When you use *spacypdfreader* the token and doc objects from spacy are annotated with additional information about the pdf.\n\nThe key features are:\n\n- **PDF to spaCy Doc object:** Convert a PDF document directly into a *spaCy* `Doc` object.\n- **Custom spaCy attributes and methods:**\n    - `token._.page_number`\n    - `doc._.page_range`\n    - `doc._.first_page`\n    - `doc._.last_page`\n    - `doc._.pdf_file_name`\n    - `doc._.page(int)`\n- **Multiple parsers:** Select between multiple built in PDF to text parsers or bring your own PDF to text parser.\n\n## Installation\n\nInstall *spacypdfreader* using pip:\n\n```bash\npip install spacypdfreader\n```\n\nTo install with the required pytesseract dependencies:\n\n```bash\npip install \'spacypdfreader[pytesseract]\'\n```\n\n## Usage\n\n```python\nimport spacy\nfrom spacypdfreader import pdf_reader\n\nnlp = spacy.load("en_core_web_sm")\ndoc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)\n\n# Get the page number of any token.\nprint(doc[0]._.page_number)  # 1\nprint(doc[-1]._.page_number) # 4\n\n# Get page meta data about the PDF document.\nprint(doc._.pdf_file_name)   # "tests/data/test_pdf_01.pdf"\nprint(doc._.page_range)      # (1, 4)\nprint(doc._.first_page)      # 1\nprint(doc._.last_page)       # 4\n\n# Get all of the text from a specific PDF page.\nprint(doc._.page(4))         # "able to display the destination page (unless..."\n```\n\n## What is *spaCy*?\n\n*spaCy* is a natural language processing (NLP) tool. It can be used to perform a variety of NLP tasks. For more information check out the excellent documentation at [https://spacy.io](https://spacy.io).\n\n## Implementation Notes\n\nspaCyPDFreader behaves a little bit different than your typical [spaCy custom component](https://spacy.io/usage/processing-pipelines#custom-components). Typically a spaCy component should receive and return a `spacy.tokens.Doc` object.\n\nspaCyPDFreader breaks this convention because the text must first be extracted from the PDF. Instead `pdf_reader` takes a path to a PDF file and a `spacy.Language` object as parameters and returns a `spacy.tokens.Doc` object. This allows users an easy way to extract text from PDF files while still allowing them use and customize all of the features spacy has to offer by allowing you to pass in the `spacy.Language` object.\n\nExample of a "traditional" spaCy pipeline component [negspaCy](https://spacy.io/universe/project/negspacy):\n\n```python\nimport spacy\nfrom negspacy.negation import Negex\n\nnlp = spacy.load("en_core_web_sm")\nnlp.add_pipe("negex", config={"ent_types":["PERSON","ORG"]})\ndoc = nlp("She does not like Steve Jobs but likes Apple products.")\n```\n\nExample of `spaCyPDFreader` usage:\n\n```python\nimport spacy\nfrom spacypdfreader import pdf_reader\nnlp = spacy.load("en_core_web_sm")\n\ndoc = pdf_reader("tests/data/test_pdf_01.pdf", nlp)\n```\n\nNote that the `nlp.add_pipe` is not used by spaCyPDFreader.',
    'author': 'SamEdwardes',
    'author_email': 'edwardes.s@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/SamEdwardes/spaCyPDFreader',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
