# whodunnit

`whodunnit` is a simple to use progress tracker for teams.


## Requirements

`whodunnit` requires Python 3.5+ and Node JS 6+. Dependencies are managed by
their respective package managers.


## Installing

To install `whodunnit` you will first require to install the Node dependencies.
Node dependencies are managed through `npm` and can be installed with
`npm install`.

After that is finished, running one of the following will create an installable
package:

```sh
python setup.py bdist_wheel  # This is the preferred method. (Requires wheel.)
python setup.py bdist_egg
```

## Developing

You can set up a development environment by running:

```sh
npm install
python setup.py development
```

After this, you can run the devserver in `./contrib/devserver`. This will launch
BrowserSync proxying the Python development server. This is a live reloading
server, which means the following:

- changes to CSS will cause the CSS to be dynamically reloaded;
- changes to JS(X) will cause a refresh; and
- changes to Python files will cause the server to restart.
