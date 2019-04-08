import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='unicorn-binance-websocket-api',
     version='1.0.0',
     author="UNICORN Data Analysis, www.unicorn-data.com",
     author_email="",
     scripts=['unicorn_binance_websocket_api.py'],
     description="A python API to use the Binance Websocket API in a easy, fast, robust and fully-featured way.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT License',
     project_urls={
        'Source': 'https://github.com/unicorn-data-analysis/unicorn-binance-websocket-api',
        'Documentation': 'https://www.unicorn-data.com/unicorn-binance-websocket-api.html',
        'Howto': 'https://www.unicorn-data.com/blog/article-details/howto-unicorn-binance-websocket-api.html',
     },
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3.5",
         'Intended Audience :: Developers',
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         'Topic :: Software Development :: Libraries :: Python Modules',
     ],
)