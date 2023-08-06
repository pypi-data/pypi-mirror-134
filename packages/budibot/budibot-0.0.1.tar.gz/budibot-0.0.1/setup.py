from setuptools import setup, find_packages
 
# classifiers = [
#   'Development Status :: 5 - Production/Stable',
#   'Intended Audience :: Education',
#   'Operating System :: Microsoft :: Windows :: Windows 10',
#   'License :: OSI Approved :: MIT License',
#   'Programming Language :: Python :: 3.9'
# ]
 
# setup(
#   name='Budibot',
#   version='0.0.1',
#   description='NLP Chatbot model for UMKM',
#   long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
#   url='',  
#   author='Malvin',
#   author_email='khoemalvin17@gmail.com',
#   license='MIT', 
#   classifiers=classifiers,
#   keywords='chatbot', 
#   packages=find_packages(),
#   install_requires=['fuzzywuzzy','numpy','pandas','requests','Sastrawi','scikit-learn']
# )

setup(
    name = "budibot",
    version = "0.0.1",
    author = "Malvin",
    author_email = "khoemalvin17@gmail.com",
    description = ("NLP Chatbot model for UMKM"),
    license = "MIT",
    keywords = "Chatbot",
    url = "",
    packages=find_packages(),
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],
    install_requires=[
      'fuzzywuzzy','numpy','pandas',
      'requests','Sastrawi','scikit-learn'
    ]
)