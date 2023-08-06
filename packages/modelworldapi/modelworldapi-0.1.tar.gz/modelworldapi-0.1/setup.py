from distutils.core import setup
setup(
  name = 'modelworldapi',         # How you named your package folder (MyLib)
  packages = ['modelworldapi'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='GNU GPLv3',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Used exclusively for ModelWorld',   # Give a short description about your library
  author = 'Ojas Gupta',                   # Type in your name
  author_email = 'gupta.ojas.27@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Ojas1024/modelworldapi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['ModelWorld', 'Object Detection', 'Online Object Detection', "PyTorch", "Computer Vision", "Free"],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
    "certifi",
    "charset-normalizer",
    "idna",
    "requests",
    "urllib3",
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)