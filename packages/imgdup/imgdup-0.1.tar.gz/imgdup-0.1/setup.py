from setuptools import setup, find_packages
setup(
    name = "imgdup",
    version = "0.1",
    packages = find_packages(),
    scripts = ['imgdup.py'],
    install_requires = ['pillow>=2.8.1'],

    # metadata for upload to PyPI
    author = "Radu Ioan Fericean",
    author_email = "radu@fericean.ro",
    description = "Visual similarity image finder and cleaner",
    license = "MIT",
    keywords = "deduplication duplicate images image visual finder",
    url = "https://github.com/rif/imgdup",   # project home page, if any

)
