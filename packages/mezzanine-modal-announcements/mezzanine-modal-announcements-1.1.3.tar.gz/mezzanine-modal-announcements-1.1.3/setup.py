from distutils.core import setup
from setuptools import find_packages
setup(
    name = 'mezzanine-modal-announcements',
    packages = find_packages(),
    include_package_data=True,
    version = '1.1.3',
    description = 'Popup announcements for Mezzanine websites utilizing Bootstrap modals.',
    author = 'Joshua Cartmell',
    author_email = 'chat@joshc.io',
    url = 'https://github.com/joshcartme/mezzanine-modal-announcements',
    download_url = 'https://github.com/joshcartme/mezzanine-modal-announcements/tarball/1.1.3',
    keywords = ['mezzanine', 'django', 'announcements'],
    classifiers = [],
)
