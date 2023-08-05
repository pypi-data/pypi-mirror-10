All commands are used under the root dir of the project (where this README.txt is), 

1. For nose test:
use the command 'nosetests'
use the command 'nosetests --'

2. For releasing a new version:
python setup.py sdist upload -r pypi


3. Implementation of max pooling uses Cython.
For developers, use 'python setup.py build_ext --inplace' to generate '.so' (linux) or '.pyd' (windows) 

4. To run simple_cnn.py:
python simplecnn/simple_cnn.py

