Worth noting that you don't actually need Poetry just to use pyproject.toml instead of requirements.txt. setuptools supports both.

But for Poetry, specifically, the main benefits are:

 1. Poetry stores the version of every single dependency, including dependencies of other dependencies, in poetry.lock files. This makes repeatable builds easy to do.

 2. Poetry's dependency resolver is better than pip's, you can pretty much trust that whatever combination it finds will work. It also has helpful error messages for when you might need additional version constraints.

 3. Poetry not only lets you lift the need for requirements.txt, but also almost every other configuration file (setup.py, setup.cfg, linter configs, Tox config, pytest config...), resulting in a less cluttered repository

 4. Poetry manages the virtual environment for you, so you never have to touch it yourself (and it can use an existing one)
 You can build and publish to PyPI effortlessly


But for Poetry, specifically, the main downsides:

 1.  You now have an extra build-time and / or runtime dependency you have to install on the system prior to installing your dependencies. For example, the stock python docker image doesn't contain poetry, so before you can bring your code in and install it you first have to install poetry in it. Poetry is abit complicated.When you ``pip install poetry``, you realize that it requires atleast 50 dependencies to be installed. They're most likely important dependencies but when you compare it with ``pip install -r requirements.txt``, the layer of complexity is non existent. Its too heavy
 2. The default versioning behaviour for packaging. When configuring your ``.toml``, you immediately notice the caret versioning where dependencies are in a >= state. This causes alot of conflicts
 3. Pip has a dependency resolver now
 4. It might fail in CI. Don't forget that the explicit install step gives them an opportunity to deliberately break your CI. You can go in depth [here](https://github.com/python-poetry/poetry/pull/6297)
 5. You are using libraries with really complex installs like pytorch (like a lot of ML libraries) you can run into issues.


Better alternative to consider is pdm which acts as a packaging development workflow.
PDM does:

1. venv creation (venv builtin module)
2. dependency installation
3. Dependency management  (i.e. mark this dependency as optional, that dependency as dev, etc)
4. build wheels (replaces build module)
5. upload to pypi (replaces twine)
6. PDM has the option to run custom shell scripts (à la npm, or a small makefile) and I use that A LOT. Scripting also has advanced features for sophisticated use cases, which may come in handy (it's the hooks page in the documentation).

It might still be a bit too new so support for its issues is not too great

