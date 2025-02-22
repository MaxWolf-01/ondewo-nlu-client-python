import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setuptools.setup(
    name='ondewo-nlu-client',
    version='2.8.5',
    author='Ondewo GmbH',
    author_email='office@ondewo.com',
    description='This library facilitates the interaction between a user and his/her CAI server.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ondewo/ondewo-nlu-client-python',
    packages=[
        np
        for np in filter(
            lambda n: n.startswith('ondewo.') or n == 'ondewo',
            setuptools.find_packages()
        )
    ],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3',
    install_requires=requires,
)
