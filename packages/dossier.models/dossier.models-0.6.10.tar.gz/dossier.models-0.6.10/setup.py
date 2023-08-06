import os

from setuptools import setup, find_packages
from setuptools.command.install import install

from version import get_git_version
VERSION, SOURCE_LABEL = get_git_version()
PROJECT = 'dossier.models'
AUTHOR = 'Diffeo, Inc.'
AUTHOR_EMAIL = 'support@diffeo.com'
URL = 'http://github.com/dossier/dossier.models'
DESC = 'Active learning models'


def read_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    return open(file_path).read()


class CustomInstall(install):
    nltk_data=[
        'maxent_treebank_pos_tagger',
        'wordnet',
    ]
    def run(self):
        install.run(self)
        try:
            import nltk
            for data_name in self.nltk_data:
                print('nltk.download(%r)' % data_name)
                nltk.download(data_name)
        except ImportError:
            print('failed to import nltk, so not installing nltk data')


setup(
    name=PROJECT,
    version=VERSION,
    description=DESC,
    license='MIT',
    long_description=read_file('README.md'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),
    #cmdclass={'install': CustomInstall,}
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'beautifulsoup4',
        'dossier.fc >= 0.1.4',
        'dossier.label >= 0.1.5',
        'dossier.web >= 0.7.8',
        'gensim',
        'happybase',
        'joblib',
        'many_stop_words',
        'nltk',
        'numpy',
        'regex',
        'requests',
        'scipy',
        'scikit-learn',
        'streamcorpus-pipeline>=0.7.7',
        'pytest',
        'pytest-diffeo >= 0.1.4',
        'urlnorm >= 1.1.3',
        'xlsxwriter',
        'Pillow'
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'dossier.models = dossier.models.web.__main__:main',
            'dossier.models.soft_selectors = dossier.models.soft_selectors:main',
            'dossier.etl = dossier.models.etl:main',
        ],
        'streamcorpus_pipeline.stages': [
            'to_dossier_store = dossier.models.etl.interface:to_dossier_store',
        ],
    },
)

