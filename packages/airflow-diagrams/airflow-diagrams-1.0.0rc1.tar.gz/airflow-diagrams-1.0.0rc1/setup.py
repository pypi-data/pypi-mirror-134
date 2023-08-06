# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['airflow_diagrams']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'apache-airflow-client>=2.2.0,<3.0.0',
 'diagrams>=0.20.0,<0.21.0',
 'thefuzz[speedup]>=0.19.0,<0.20.0',
 'typer>=0.4.0,<0.5.0']

setup_kwargs = {
    'name': 'airflow-diagrams',
    'version': '1.0.0rc1',
    'description': 'Auto-generated Diagrams from Airflow DAGs.',
    'long_description': "# airflow-diagrams\n\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/feluelle/airflow-diagrams/master.svg)](https://results.pre-commit.ci/latest/github/feluelle/airflow-diagrams/master)\n[![PyPI version](https://img.shields.io/pypi/v/airflow-diagrams)](https://pypi.org/project/airflow-diagrams/)\n[![License](https://img.shields.io/pypi/l/airflow-diagrams)](https://github.com/feluelle/airflow-diagrams/blob/master/LICENSE)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/airflow-diagrams)](https://pypi.org/project/airflow-diagrams/)\n\n> Auto-generated Diagrams from Airflow DAGs.\n\nThis project aims to easily visualise your [Airflow](https://github.com/apache/airflow) DAGs on service level\nfrom providers like AWS, GCP, Azure, etc. via [diagrams](https://github.com/mingrammer/diagrams).\n\n## 🚀 Get started\n\n### Installation\n\nTo install it from [PyPI](https://pypi.org/) run:\n```\npip install airflow-diagrams\n```\n\n### Usage\n\nTo use this auto-generator just run the following command:\n```\nairflow_diagrams generate\n```\n**Note:** *The default command is trying to authenticate to `http://localhost:8080/api/v1` via username `admin` and password `admin`. You can change those values via flags i.e. `-h`, `-u` or `-p`. Check out the help i.e. `--help` for more information.*\n\nThis will create a file like `<dag-id>_diagrams.py` which contains the definition to create a diagram. Run this file and you will get a rendered diagram.\n\nExamples of generated diagrams can be found in the [examples](examples) directory.\n\n## 🤔 How it Works\n\nℹ️ At first it connects, by using the official [Apache Airflow Python Client](https://github.com/apache/airflow-client-python), to your Airflow installation to retrieve all DAGs (in case you don't specify any `dag_id`) and all Tasks for the DAG(s).\n\n🔮 Then it tries to find a diagram node for every DAGs task, by using [Fuzzy String Matching](https://github.com/seatgeek/thefuzz), that matches the most. If you are unhappy about the match you can also provide a `mapping.yml` file to statically map from Airflow task to diagram node.\n\n🪄 Lastly it renders the results into a python file which can then be executed to retrieve the rendered diagram. 🎉\n\n## ❤️ Contributing\n\nContributions are very welcome. Please go ahead and raise an issue if you have one or open a PR. Thank you.\n",
    'author': 'Felix Uellendall',
    'author_email': 'feluelle@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
