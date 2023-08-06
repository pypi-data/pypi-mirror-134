# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sfu_tf_lib',
 'sfu_tf_lib.base',
 'sfu_tf_lib.common',
 'sfu_tf_lib.dataset',
 'sfu_tf_lib.metrics',
 'sfu_tf_lib.metrics.aggregation',
 'sfu_tf_lib.models',
 'sfu_tf_lib.modules',
 'sfu_tf_lib.trackers']

package_data = \
{'': ['*']}

install_requires = \
['mlflow-skinny>=1.8,<2.0',
 'numba>=0.51,<1',
 'numpy',
 'scikit-learn>=0.24,<1',
 'scipy>=1.4,<2.0',
 'sfu-data-io>=0.1,<1',
 'tensorflow>=2.2,<3.0']

setup_kwargs = {
    'name': 'sfu-tf-lib',
    'version': '1.0.0',
    'description': 'Libraries that support the development of machine learning models in TensorFlow.',
    'long_description': None,
    'author': 'Anderson de Andrade',
    'author_email': 'anderson_de_andrade@sfu.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
