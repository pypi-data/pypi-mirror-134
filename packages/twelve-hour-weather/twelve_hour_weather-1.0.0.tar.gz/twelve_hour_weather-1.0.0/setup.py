from setuptools import setup

setup(
    name='twelve_hour_weather',                         # Your package will have this name
    packages=["sunnyday"],                              # Name the package again
    version='1.0.0',                                    # To be increased everytime you change your library
    license="MIT",                                      # Type of license. More here: http://help.github.com/articles/licensing-a-repository
    description='Weather forecast data',                # Short description of your library
    author='Matt Lade',                                 # Your name
    author_email='ladelz86@hotmail.com',                # Your email
    url='https://example.com',                          # Homepage of your library (r.g. github or your website)
    keywords=["weather", "forecast", "openweather"],    # Keywords users can search on pypi.org
    install_requires=[                                  # Other 3rd-party libs that pip needs to install
        'requests',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",              # Choose either "3 - Alpha", "4 - Beta" or "5 Production/Stable" as the current status
        "Intended Audience :: Developers",              # Who is the audience for your library?
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",       # Type a license again
        "Programming Language :: Python :: 3.7",        # Python versions that your library supports
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
