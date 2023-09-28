from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='fun code',
      url='https://github.com/ralfmein/PythonGoIT',
      author='Guido van Rossum',
      author_email='Guido_van_Rossum@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['shutil'],
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
      )
