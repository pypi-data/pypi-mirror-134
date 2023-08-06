from setuptools import find_packages, setup
setup(
    name='vboUtil',
    packages=find_packages(include=['vboUtil']),
    version='0.1.2',
    description='Functions given in the VBO Bootcamp',
    author='Mehmet OZER',
    license='MIT',
    install_requires=['pandas', 'numpy', 'matplotlib', 'sklearn', 'datetime', 'lifetimes',
                      'seaborn'],  # Libraries required that are not available by default
    setup_require=['pytest-runner'],
    test_require=['pytest'],
    test_suite='tests'
)