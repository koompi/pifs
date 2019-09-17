from distutils.core import setup
setup(
  name = 'pifs',         
  packages = ['pifs'],   
  version = '1.0.2',      
  license='MIT',       
  description = 'project use to encrypt and decrypt and upload to ipfs',
  author = 'Pionium',                
  author_email = 'pi@koompi.com',      
  url = 'https://github.com/koompi/pifs.git',
  download_url = 'https://github.com/koompi/pifs/archive/master.zip',
  entry_points = {
        "console_scripts": ['pifs-upload = pifs.upload:run',
                            'pifs-download = pifs.download:run',
                            'pifs = pifs.fexcept:ferror',
                            ],
        },
  install_requires=[      
          'ipfsapi',
          'cryptography',
      ],
  classifiers=[      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
