HOW TO USE:
1.register for pypi:https://pypi.python.org/pypi?%3Aaction=register_form
2.install setuptools£ºhttps://pypi.python.org/pypi/setuptools 

	* download ez_setup.py:https://bootstrap.pypa.io/ez_setup.py
	* run:python ez_setup.py
	* configure ~/.pypirc£º£¨in windows, you have to use rename command in cmd£©
	* example:
	[distutils]
	index-servers =
    		pypi

	[pypi]
	username:******
	password:******
3. copy setup.py to ../../£º

4. register project£º
python setup.py register
5. pack and upload
:python setup.py sdist upload
Enjoy it with pip install bos-python-sdk!