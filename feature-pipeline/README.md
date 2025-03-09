Worth noting that you don't actually need Poetry just to use pyproject.toml instead of requirements.txt. setuptools supports both.

But for Poetry, specifically, the main benefits are:

1. Poetry stores the version of every single dependency, including dependencies of other dependencies, in poetry.lock files. This makes repeatable builds easy to do.

2. Poetry's dependency resolver is better than pip's, you can pretty much trust that whatever combination it finds will work. It also has helpful error messages for when you might need additional version constraints.

3. Poetry not only lets you lift the need for requirements.txt, but also almost every other configuration file (setup.py, setup.cfg, linter configs, Tox config, pytest config...), resulting in a less cluttered repository

4. Poetry manages the virtual environment for you, so you never have to touch it yourself (and it can use an existing one)
You can build and publish to PyPI effortlessly