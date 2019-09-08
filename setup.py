from setuptools import setup

setup(name='boneless',
      version='0.0.1',
      description='can i get a boneless pizza',
      long_description='lets just say...if this works youll never use skype the same again',
      url='https://github.com/jakeelkins/boneless',
      author='Jake Elkins',
      license='MIT',
      install_requires=['pyaudio'],#['cffi', 'setuptools', 'JACK-Client'],
      #dependency_links=['https://github.com/jackaudio/jack2'],
      packages=['boneless'],
      package_data={'': ['']},
      zip_safe=False,
      python_requires='>=3.6')
