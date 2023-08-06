from setuptools import setup


with open('README.md', 'r') as file_ref:
    long_description = file_ref.read()

setup(
    name='universal-answer-package-tutorial',
    version='0.0.1',
    description='Universal tool to determine the answer.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['answer'],
    package_dir={'': 'src'},
    install_requires=[
        "tqdm ~= 4.62"
    ],
    extras_require={
        'dev': [
            "pytest>=6.2",
            "check-manifest"
        ]
    },
    license='MIT License',
    author='Manuel Dornacher',
    author_email='manuel.dornacher@gmail.com',
    url='https://github.com/MDornacher/universal-answer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Education :: Testing',
    ]
)
