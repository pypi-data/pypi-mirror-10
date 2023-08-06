# `install_binaries` - install executable programs in bin/

`install_binaries` is a tool to help you create wrappers around
executable files.  It ensures that they're installed in a reasonable
directory, and that they have their +x bit set.  It should work fine
with old versions of pip and setuptools, and with Python 2.7 and up.
It should work with both `sdist` and `bdist_wheel` packages.

To use it, you have to do two things.  First, you need to add two lines
to your `setup.py`:

```
setup(
	name="my_cool_app",
	...
	setup_requires=['install_binaries'],
	install_binaries=['my-binary', 'build/other-one'],
)
```

This will install both `my-binary` and `other-one` to
`.../my-virtualenv/bin` when your package is installed.

Second, you need to make sure your binary is included in your
`MANIFEST.in` file.  So that might look like:

```
include requirements.txt
include VERSION
include my-binary
include build/other-one
```

If it's left out, it won't be included in the package that `python
setup.py sdist` creates.

## Known limitations

If your package gets installed as an egg, by using `easy_install` or
`setup.py install`, the `install_binaries` code never gets called, so we
have no chance to install the binaries.  There may be a way around this,
but I haven't found it.  `install_binaries` attempts to warn the user in
this situation.
