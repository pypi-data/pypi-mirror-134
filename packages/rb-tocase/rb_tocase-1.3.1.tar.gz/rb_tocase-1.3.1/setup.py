# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rb_tocase']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rb-tocase',
    'version': '1.3.1',
    'description': 'RB toCase is a Case converter.',
    'long_description': '<h1 align="center">toCase<h1>\n<img alt="Cover" src="./assets/cover.svg">\n<h4 align="center">made by: <a href="https://github.com/RickBarretto/">RickBarreto</a></h4>\n\n## What is it?\n**RB toCase** is a Case converter made in python, for peoples who wants simplify this feature. It can convert to and from Camel, Pascal, Snake, Kebab and Strings Sentences.\n**And, You don\'t need say what is the input type, the code parse it. Just say whats is the output type.**\n\n> Older name was toCase, but when I was publishing on Pipy tocase package already exists. So I changed the name!\n\n## Install\n```\npip install git+https://github.com/RickBarretto/toCase.git\n```\n\n## Why I must to use it?\n+ toCase was made to make easy your life with case converting\n+ I was made in python, so, if you want, you can copy the [toCase.py](https://github.com/RickBarretto/toCase/blob/main/src/ToCase.py) and use in your project. **It\'s free to use, look the [MIT LICENSE](LICENSE).**\n\n## Glossary:\n- [What is it?](#what-is-it)\n- [Install](#install)\n- [Why I must to use it?](#why-i-must-to-use-it)\n- [Glossary:](#glossary)\n- [Examples:](#examples)\n  - [Importing:](#importing)\n  - [Convert to Camel Case:](#convert-to-camel-case)\n  - [Convert to Snake Case:](#convert-to-snake-case)\n  - [Convert to Kebab Case:](#convert-to-kebab-case)\n  - [Convert to Pascal Case:](#convert-to-pascal-case)\n  - [Convert to Sentence:](#convert-to-sentence)\n- [Read The Docs!](#read-the-docs)\n\n## Examples: \n\n### Importing:\n```py\n>>> from toCase import Case\n>>> # or\n>>> from toCase import *\n>>> # see the examples below\n```\n\n### Convert to Camel Case:\n```py\n>>> Case.toCamel("Changing to CaMel CASE")   # From String Sentence\n\'changingToCamelCase\'\n>>> Case.toCamel("Changing-to-camel-case")   # From Kebab Case\n\'changingToCamelCase\'\n>>> Case.toCamel("Changing_to_CAMEL_CASE")   # From Snake Case\n\'changingToCamelCase\'\n>>> Case.toCamel(" ChangingToCamelCase  ")   # From Pascal Case\n\'changingToCamelCase\'\n```\n+ [See more](DOC.md#casetocamelstring-str-case1-str--lower)\n\n### Convert to Snake Case:\n```py\n>>> Case.toSnake(" ChanginToSnakeCase ")     # From Pascal Case\n\'changin_to_snake_case\'\n>>> Case.toSnake(" Changin To Snake Case ")  # From String\n\'changin_to_snake_case\'\n>>> Case.toSnake(" Changin-To-Snake-Case ")  # From Kebab\n\'changin_to_snake_case\'\n>>> Case.toSnake(" changinToSnakeCase ")     # From Camel\n\'changin_to_snake_case\'\n```\n[See more](DOC.md#casetosnakestring-str-case-str--lower-case1-str--lower)\n\n### Convert to Kebab Case:\n```py\n>>> Case.toKebab("Changing to Kebab")    # From String\n\'changing-to-kebab\'\n>>> Case.toKebab("ChangingToKebab")      # From Pascal Case\n\'changing-to-kebab\'\n>>> Case.toKebab("changingToKebab")      # From Camel Case\n\'changing-to-kebab\'\n>>> Case.toKebab("changing_to_kebab")    # From Snake Case\n\'changing-to-kebab\'\n```\n\n[See more](DOC.md#casetokebabstring-str-case-str--lower-case1-str--lower)\n\n### Convert to Pascal Case:\n```py\n>>> Case.toPascal("Changing to Pascal")  # From String\n\'ChangingToPascal\'\n>>> Case.toPascal("Changing-to-Pascal")  # From Kebab\n\'ChangingToPascal\'\n>>> Case.toPascal("Changing_to_Pascal")  # From Snake\n\'ChangingToPascal\'\n>>> Case.toPascal("ChangingtoPascal")    # From Pascal\n\'ChangingtoPascal\'\n>>> Case.toPascal("changingToPascal") # From Camel\n\'ChangingToPascal\'\n```\n+ [See more](DOC.md#casetopascalstring-str-case1-str--title)\n\n### Convert to Sentence:\n```py\n>>> Case.toSentence("ItsAPascalCase")\n\'its a pascal case\'\n>>> Case.toSentence("itsACamelCase")\n\'its a camel case\'\n>>> Case.toSentence("Its-A-Kebab-Case")\n\'its a snake case\'\n>>> Case.toSentence("Its_a_snake_case")\n\'its a snake case\'\n```\n+ [See more](DOC.md#casetosentencestring-str-case-str--lower-case1-str--lower)\n\n\n## Read The Docs!\n[Documentation](DOC.md)',
    'author': 'RickBarretto',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/RickBarretto/toCase',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
