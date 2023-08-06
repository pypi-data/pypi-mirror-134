from setuptools import setup, find_packages
import re


requirements = []
version = ""
readme = ""

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

with open('webx/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("version is not set")

with open("README.md") as f:
    readme = f.read()

packages = [
    "webx.asgi",
    "webx.config",
    "webx.core",
    "webx.http",
    "webx.templating",
    "webx.tooling",
    "webx.types",
    "webx.views",
    "webx.core.management.boilerplate",
    "webx.core.management.commands"
]

setup(
    name='webx',
    author='justanotherbyte',
    url='https://github.com/justanotherbyte/webx',
    project_urls={
        "Documentation": "https://webx.kozumikku.tech/",
        "Issue tracker": "https://github.com/justanotherbyte/webx/issues",
    },
    version=version,
    packages=packages,
    license='MIT',
    description='A next-generation ASGI Python web-framework, focused on Speed and Stability',
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.8.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
    entry_points={
        "console_scripts": ["webx-admin=webx.__main__:admin"]
    }
)