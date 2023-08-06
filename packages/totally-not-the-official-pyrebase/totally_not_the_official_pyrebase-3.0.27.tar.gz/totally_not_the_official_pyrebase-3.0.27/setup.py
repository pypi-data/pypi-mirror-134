from setuptools import setup, find_packages

setup(
    name='totally_not_the_official_pyrebase',
    version='3.0.27',
    url='https://github.com/thisbejim/Pyrebase',
    description='firebase api wrapper fork from thisbejim but remove module limitation',
    author='James Childs-Maidment',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='Firebase',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests',
        'gcloud',
        'oauth2client',
        'requests_toolbelt',
        'python_jwt',
        'pycryptodome'
    ]
)
