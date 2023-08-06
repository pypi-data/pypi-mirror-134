# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nekton', 'nekton.utils']

package_data = \
{'': ['*'], 'nekton': ['bins/*']}

install_requires = \
['jsonschema>=3.2.0,<4.0.0',
 'nibabel>=3.2.1,<4.0.0',
 'numpy>=1.22.0,<2.0.0',
 'pydicom-seg>=0.4.0,<0.5.0',
 'pydicom>=2.2.2,<3.0.0']

setup_kwargs = {
    'name': 'nekton',
    'version': '0.2.0',
    'description': 'A python package for DICOM to NifTi and NifTi to DICOM-SEG and GSPS conversion',
    'long_description': '# Nekton\n[![Python Application Testing](https://github.com/deepc-health/nekton/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/deepc-health/nekton/actions/workflows/tests.yml)[![Test and Release](https://github.com/deepc-health/nekton/actions/workflows/release.yml/badge.svg?branch=master)](https://github.com/deepc-health/nekton/actions/workflows/release.yml)\n\n> A python package for DICOM to NifTi and NifTi to DICOM-SEG and GSPS conversion\n\n## SETUP\nTBD\n## DICOM to NifTi\n\nThe DICOM to NifTi conversion in the package is based on a wrapper around the [dcm2niix](https://github.com/rordenlab/dcm2niix) software.\n\n### Usage\n\nTBD\n\n### Notes\n\n- The renaming functionality retains the [suffixes](https://github.com/rordenlab/dcm2niix/blob/master/FILENAMING.md) from the original program.\n- The BIDS sidecar json is retained as well.\n\n## NifTi to DICOM-SEG\n\n### Usage\n\nTBD\n\n## NifTi to GSPS\n\n\n======\n',
    'author': 'a-parida12',
    'author_email': 'abhijeet@deepc.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/deepc-health/nekton',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
