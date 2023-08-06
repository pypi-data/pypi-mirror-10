from setuptools import setup, find_packages

VERSION = '1.0'


setup(
    name="mkdocs-basic-theme",
    version=VERSION,
    url='http://www.mkdocs.org',
    license='BSD',
    description='Minimal theme for MkDocs',
    author='Dougal Matthews',
    author_email='dougal@dougalmatthews.com.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'basictheme = basic_theme',
        ]
    },
    zip_safe=False
)
