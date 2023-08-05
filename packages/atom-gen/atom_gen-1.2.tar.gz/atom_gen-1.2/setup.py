from distutils.core import setup


LONG_DESCRIPTION = """
ATOM feed generator and tools

Released under MIT Licence.
"""

setup(
    name='atom_gen',
    version='1.2',
    packages=['easy_atom'],
    url='https://github.com/flrt/atom_gen',
    license='MIT',
    keywords="Atom,feed,XML",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    author='Frederic Laurent',
    author_email='frederic.laurent@gmail.com',

    description='Atom feed helpers',
    long_description=LONG_DESCRIPTION
)
