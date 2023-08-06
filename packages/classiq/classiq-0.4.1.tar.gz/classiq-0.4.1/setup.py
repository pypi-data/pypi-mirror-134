# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['classiq', 'classiq.authentication', 'classiq.quantum_functions']

package_data = \
{'': ['*']}

install_requires = \
['ConfigArgParse>=1.5,<2.0',
 'Pyomo>=6.0,<6.1',
 'httpx>=0.21,<0.22',
 'keyring>=23.0.1,<24.0.0',
 'nest-asyncio>=1.5.1,<2.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'semver>=2.13.0,<3.0.0',
 'websockets>=9.1,<10.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=4.8.1,<5.0.0'],
 'all': ['classiq-interface>=0.4.1,<0.5.0']}

setup_kwargs = {
    'name': 'classiq',
    'version': '0.4.1',
    'description': 'Classiq SDK Package',
    'long_description': '<p align="center">\n  <a href="https://www.classiq.io"><img src="https://uploads-ssl.webflow.com/60000db7a5f449af5e4590ac/6122b22eea7a9583a5c0d560_classiq_RGB_Green_with_margin.png\n" alt="Classiq"></a>\n</p>\n<p align="center">\n    <em>The Classiq Quantum Algorithm Design platform helps teams build sophisticated quantum circuits that could not be designed otherwise</em>\n</p>\n\n\nWe do this by synthesizing high-level functional models into optimized quantum circuits, taking into account the\nconstraints that are important to the designer. Furthermore, we are able to generate circuits for practically any\nuniversal gate-based quantum computer and are compatible with most quantum cloud providers.\n\n## Requirements\nPython 3.8+\n\n\n## Installation\n```console\npip install --upgrade pip\n$ pip install \'classiq[all]\'\n```\n\n## Example\n\n```python\nfrom classiq import generator\nfrom classiq.builtin_functions import StatePreparation, QFT\nfrom classiq_interface.generator.state_preparation import (\n    PMF,\n    Metrics,\n    NonNegativeFloatRange,\n)\n\ncircuit_generator = generator.Generator(qubit_count=20, max_depth=100)\n\nprobabilities = (0.5, 0.1, 0.2, 0.005, 0.015, 0.12, 0.035, 0.025)\npmf = PMF(pmf=probabilities)\nsp_params = StatePreparation(\n    probabilities=pmf,\n    num_qubits=4,\n    error_metric={Metrics.KL: NonNegativeFloatRange(upper_bound=0.3)},\n)\n\noutput_dict = circuit_generator.StatePreparation(params=sp_params)\n\nstate_preparation_output = output_dict["OUT"]\n\nqft_params = QFT(num_qubits=3)\ncircuit_generator.QFT(\n    params=qft_params, in_wires={"IN": state_preparation_output}\n)\n\ncircuit = circuit_generator.generate()\ncircuit.show()\n```\n\n## License\nSee [license](https://classiq.io/license).\n',
    'author': 'Classiq Technologies',
    'author_email': 'support@classiq.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://classiq.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
