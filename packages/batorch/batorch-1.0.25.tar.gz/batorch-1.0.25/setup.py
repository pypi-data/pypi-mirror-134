from setuptools import setup, find_packages

setup(
	name = 'batorch',
	version = '1.0.25',
	keywords = ['pip', 'pymyc', 'batorch', 'torch', 'batch', 'batched data'],
	description = "'batorch' is an extension of package torch, for tensors with batch dimensions. ",
	long_description = '',
	long_description_content_type = 'text/markdown',
	license = 'MIT Licence',
	url = 'https://github.com/Bertie97/PyZMyc/batorch',
	author = 'Yuncheng Zhou',
	author_email = 'bertiezhou@163.com',
	packages = find_packages(),
	include_package_data = True,
	platforms = 'any',
	install_requires = ['torch']
)
