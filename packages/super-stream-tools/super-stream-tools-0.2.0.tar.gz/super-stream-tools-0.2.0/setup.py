from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='super-stream-tools',
    version='0.2.0',
    description='A tool to interact with streaming URLs easily',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/korigamik/media-tools',
    author='KorigamiK',
    author_email='korigamik@gmail.com',
    license='MIT',
    install_requires=['asyncio',
                      'aiohttp',
                      'aiofiles'
                      ],
    scripts=["bin/stream-tools"],
    keywords=['python', 'video', 'stream',
              'video stream', 'encode', 'ffmpeg'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.10',
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=['super_stream_tools', 'super_stream_tools/stream_library'],
    python_requires=">=3.9",
)
