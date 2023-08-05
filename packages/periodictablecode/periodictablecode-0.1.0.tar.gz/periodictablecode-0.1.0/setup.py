from setuptools import setup

setup(
    name='periodictablecode',
    version='0.1.0',    
    description='Encrypting strings using the periodic table',
    long_description="",
    url='https://github.com/Sam-Nielsen-Dot/periodictablecode',
    author='Sam Nielsen',
    author_email='lenssimane@gmail.com',
    license='MIT',
    packages=['periodictablecode'],
    install_requires=[                  
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Healthcare Industry',
        'Environment :: Win32 (MS Windows)',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    include_package_data=True,
    package_data={'': ['periodictablecode/data/*.csv']},
)
