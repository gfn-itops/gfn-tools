from setuptools import setup, find_packages

setup(
    name='gfn-tools',
    version='0.0.1',
    description='Symbolic metadata compliance CLI (GFNDC)',
    author='E. Port (Layer Compliance)',
    author_email='lc@gfndc.org',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gfn=gfn.main:init',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Intended Audience :: Other Audience",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console"
    ],
    python_requires='>=3.3',
)
