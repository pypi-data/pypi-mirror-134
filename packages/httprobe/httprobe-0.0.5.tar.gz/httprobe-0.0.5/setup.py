from setuptools import find_packages, setup



setup(name='httprobe',
      version='0.0.5',
      description='Probes a list of targets and returns details about responses',
      author='midnight_repo',
      author_email='midnight_repo@protonmail.com',
      license='GPL-3.0',
      url='https://github.com/midnight-repo/httprobe',
      packages=find_packages(),
      entry_points = {'console_scripts': ['httprobe=httprobe.main:run'],},
      install_requires = ['requests', 'pandas', 'tabulate']
      )
