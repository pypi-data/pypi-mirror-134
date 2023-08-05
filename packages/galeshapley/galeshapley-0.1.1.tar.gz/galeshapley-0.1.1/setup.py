from setuptools import find_packages, setup
import pathlib

here=pathlib.Path(__file__).parent.resolve()
long_description=(here / 'README.md').read_text(encoding='utf-8')

version = {}
with open('__version__.py', 'r') as f:
    exec(f.read(), version)

setup(
    name='galeshapley',
    version=version['__version__'],
    description='Gale Shapley Algorithm',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/stamps-group/galeshapley',
    author='Gomes, J.M.',
    author_email='gomejm@ita.br',
    license='MIT',
    keywords=["game-theory gale-shapley matching-games"],
    install_requires=[],
    packages=find_packages("galeshapley"),
    package_dir={"": "galeshapley"},
    python_requires=">=3.5",
    setup_requires=['pytest-runner'],
    tests_require=["pytest", "hypothesis", "numpy"],
    test_suite='tests',
)
