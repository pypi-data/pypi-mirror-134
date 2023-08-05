[![Build Status][build_img]][ci]


About
=====

A pure-Python (3 and 2) package for manipulating:

- [Binary decision diagrams](
    https://en.wikipedia.org/wiki/Binary_decision_diagram) (BDDs).
- [Multi-valued decision diagrams](
    https://dx.doi.org/10.1109/ICCAD.1990.129849) (MDDs).

as well as [Cython](https://cython.org) bindings to the C libraries:

- [CUDD](
    https://web.archive.org/web/20180127051756/http://vlsi.colorado.edu/~fabio/CUDD/html/index.html)
  (also read [the introduction](
    https://web.archive.org/web/20150317121927/http://vlsi.colorado.edu/~fabio/CUDD/node1.html),
  and note that the original link for CUDD is <http://vlsi.colorado.edu/~fabio/CUDD/>)
- [Sylvan](https://github.com/utwente-fmt/sylvan) (multi-core parallelization)
- [BuDDy](https://sourceforge.net/projects/buddy/)

These bindings expose almost identical interfaces as the Python implementation.
The intended workflow is:

- develop your algorithm in pure Python (easy to debug and introspect),
- use the bindings to benchmark and deploy

Your code remains the same.


Contains:

- All the standard functions defined, e.g.,
  by [Bryant](https://www.cs.cmu.edu/~bryant/pubdir/ieeetc86.pdf).
- Dynamic variable reordering using [Rudell's sifting algorithm](
    http://www.eecg.toronto.edu/~ece1767/project/rud.pdf).
- Reordering to obtain a given order.
- Parser of quantified Boolean expressions in either
  [TLA+](https://en.wikipedia.org/wiki/TLA%2B) or
  [Promela](https://en.wikipedia.org/wiki/Promela) syntax.
- Pre/Image computation (relational product).
- Renaming variables.
- Zero-suppressed binary decision diagrams (ZDDs) in CUDD
- Conversion from BDDs to MDDs.
- Conversion functions to [`networkx`](https://networkx.org) and
  [`pydot`](https://pypi.org/project/pydot) graphs.
- BDDs have methods to `dump` and `load` them using [JSON](
    https://wikipedia.org/wiki/JSON), or [`pickle`](
    https://docs.python.org/3/library/pickle.html).
- BDDs dumped by CUDD's DDDMP can be loaded using fast iterative parser.
- [Garbage collection](
    https://en.wikipedia.org/wiki/Garbage_collection_(computer_science))
  that combines reference counting and tracing


If you prefer to work with integer variables instead of Booleans, and have
BDD computations occur underneath, then use the module
[`omega.symbolic.fol`](
    https://github.com/tulip-control/omega/blob/main/omega/symbolic/fol.py)
from the [`omega` package](
    https://github.com/tulip-control/omega/blob/main/doc/doc.md).

If you are interested in computing minimal covers (two-level logic minimization)
then use the module `omega.symbolic.cover` of the `omega` package.
The method `omega.symbolic.fol.Context.to_expr` converts BDDs to minimal
formulas in disjunctive normal form (DNF).


Documentation
=============

In the [Markdown](https://en.wikipedia.org/wiki/Markdown) file
[`doc.md`](https://github.com/tulip-control/dd/blob/main/doc.md).

The [changelog](https://en.wiktionary.org/wiki/changelog) is in
the file [`CHANGES.md`](
    https://github.com/tulip-control/dd/blob/main/CHANGES.md).


Examples
========


The module `dd.autoref` wraps the pure-Python BDD implementation `dd.bdd`.
The API of `dd.cudd` is almost identical to `dd.autoref`.
You can skip details about `dd.bdd`, unless you want to implement recursive
BDD operations at a low level.


```python
from dd.autoref import BDD

bdd = BDD()
bdd.declare('x', 'y', 'z', 'w')

# conjunction (in TLA+ syntax)
u = bdd.add_expr(r'x /\ y')  # symbols `&`, `|` are supported too
    # note the "r" before the quote, which signifies a raw string and is
    # needed to allow for the backslash
print(u.support)
# substitute variables for variables (rename)
rename = dict(x='z', y='w')
v = bdd.let(rename, u)
# substitute constants for variables (cofactor)
values = dict(x=True, y=False)
v = bdd.let(values, u)
# substitute BDDs for variables (compose)
d = dict(x=bdd.add_expr(r'z \/ w'))
v = bdd.let(d, u)
# as Python operators
v = bdd.var('z') & bdd.var('w')
v = ~ v
# quantify universally ("forall")
u = bdd.add_expr(r'\A x, y:  (x /\ y) => y')
# quantify existentially ("exist")
u = bdd.add_expr(r'\E x, y:  x \/ y')
# less readable but faster alternative,
# (faster because of not calling the parser;
# this may matter only inside innermost loops)
u = bdd.var('x') | bdd.var('y')
u = bdd.exist(['x', 'y'], u)
assert u == bdd.true, u
# inline BDD references
u = bdd.add_expr(r'x /\ {v}'.format(v=v))
# satisfying assignments (models):
# an assignment
d = bdd.pick(u, care_vars=['x', 'y'])
# iterate overal all assignments
for d in bdd.pick_iter(u):
    print(d)
# how many assignments
n = bdd.count(u)
# write to and load from JSON file
filename = 'bdd.json'
bdd.dump(filename, roots=[u])
other_bdd = BDD()
roots = other_bdd.load(filename)
print(other_bdd.vars)
```

To run the same code with CUDD installed, change the first line to:

```python
from dd.cudd import BDD
```

Most useful functionality is available via methods of the class `BDD`.
A few of the functions can prove handy too, mainly `to_nx`, `to_pydot`.
Use the method `BDD.dump` to write a `BDD` to a `pickle` file, and
`BDD.load` to load it back. A CUDD dddmp file can be loaded using
the function `dd.dddmp.load`.

A `Function` object wraps each BDD node and decrements its reference count
when disposed by Python's garbage collector. Lower-level details are
discussed in the documentation.

For using ZDDs, change the first line to

```python
from dd.cudd_zdd import ZDD as BDD
```


Installation
============


## pure-Python

From the [Python Package Index (PyPI)](https://pypi.org) using the
package installer [`pip`](https://pip.pypa.io):

```shell
pip install dd
```

Locally:

```shell
pip install .
```

For graph layout, install also [graphviz](https://graphviz.org).

The `dd` package remains compatible with Python 2.7,
except for few places where Python 3 is required.


## Cython bindings


### Wheel files with compiled CUDD


As of `dd` version 0.5.3, [`manylinux2014_x86_64`](
    https://www.python.org/dev/peps/pep-0599/)
[wheel files](https://www.python.org/dev/peps/pep-0427/) are
[available from PyPI](https://pypi.org/project/dd/#files) for some Python
versions. These wheel files contain the module `dd.cudd` with the CUDD
library compiled and linked.
If you have a Linux system and Python version compatible with one of the
available wheels, then `pip install dd` will install `dd.cudd`, so you need
not compile CUDD. Otherwise, see below.


### `dd` fetching CUDD

By default, the package installs only the Python modules.
You can select to install any Cython extensions using
the `setup.py` options:

- `--cudd`: build module of CUDD BDDs
- `--cudd_zdd`: build module of CUDD ZDDs
- `--sylvan`: build module of Sylvan BDDs
- `--buddy`: build module of BuDDy BDDs

Pass `--fetch` to `setup.py` to tell it to download, unpack, and
`make` CUDD v3.0.0. For example:

```shell
pip download dd --no-deps
tar xzf dd-*.tar.gz
cd dd-*/
python setup.py install --fetch --cudd --cudd_zdd
```

The path to an existing CUDD build directory can be passed as an argument:

```shell
python setup.py install --cudd="/home/user/cudd"
```

If you prefer defining installation directories, then follow [Cython's instructions](
    https://cython.readthedocs.io/en/latest/src/tutorial/clibraries.html#compiling-and-linking)
to define `CFLAGS` and `LDFLAGS` before running `setup.py`.
You need to have copied `CuddInt.h` to the installation's include location
(CUDD omits it).

If building from the repository, then first install `cython`. For example:

```shell
git clone git@github.com:tulip-control/dd
cd dd
pip install cython  # not needed if building from PyPI distro
python setup.py install --fetch --cudd
```

The above options can be passed to `pip` too, using the [`--install-option`](
    https://pip.pypa.io/en/latest/cli/pip_install/#per-requirement-overrides)
in a requirements file, for example:

```
dd >= 0.1.1 --install-option="--fetch" --install-option="--cudd"
```

The command line behavior of `pip` [is currently different](
    https://github.com/pypa/pip/issues/1883), so

```shell
pip install --install-option="--fetch" dd
```

will propagate option `--fetch` to dependencies, and so raise an error.


### User installing build dependencies

If you build and install CUDD, Sylvan, or BuDDy yourself, then ensure that:

- the header files and libraries are present, and
- suitable compiler, include, linking, and library flags are passed,
either by setting [environment variables](
    https://en.wikipedia.org/wiki/Environment_variable)
prior to calling `pip`, or by editing the file [`download.py`](
    https://github.com/tulip-control/dd/blob/main/download.py).

Currently, `download.py` expects to find Sylvan under `dd/sylvan` and built with [Autotools](https://en.wikipedia.org/wiki/GNU_Build_System)
(for an example, see `.github/workflows/main.yml`).
If the path differs in your environment, remember to update it.

Scripts are available that fetch, build, and install the Cython bindings:
- [`examples/install_dd_cudd.sh`](
    https://github.com/tulip-control/dd/blob/main/examples/install_dd_cudd.sh)
- [`examples/install_dd_sylvan.sh`](
    https://github.com/tulip-control/dd/blob/main/examples/install_dd_sylvan.sh)
- [`examples/install_dd_buddy.sh`](
    https://github.com/tulip-control/dd/blob/main/examples/install_dd_buddy.sh)


### Licensing of the compiled modules `dd.cudd` and `dd.cudd_zdd` in the wheel

These notes apply to the compiled modules `dd.cudd` and `dd.cudd_zdd` that are
contained in the [wheel file](https://www.python.org/dev/peps/pep-0427/) on
PyPI (namely the files `dd/cudd.cpython-39-x86_64-linux-gnu.so` and
`dd/cudd_zdd.cpython-39-x86_64-linux-gnu.so` in the [`*.whl` file](
    https://pypi.org/project/dd/#files), which can
be obtained using [`unzip`](http://infozip.sourceforge.net/UnZip.html)).
These notes do not apply to the source code of the modules
`dd.cudd` and `dd.cudd_zdd`.
The source distribution of `dd` on PyPI is distributed under a 3-clause BSD
license.

The following libraries and their headers were used when building the modules
`dd.cudd` and `dd.cudd_zdd` that are included in the wheel:

- [Python](https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz),
- [CUDD](https://sourceforge.net/projects/cudd-mirror/files/cudd-3.0.0.tar.gz/download).

The licenses of Python and CUDD are included in the wheel archive.

Cython [does not](https://github.com/cython/cython/blob/master/COPYING.txt)
add its license to C code that it generates.

GCC was used to compile the modules `dd.cudd` and `dd.cudd_zdd` in the wheel,
and the GCC [runtime library exception](
    https://github.com/gcc-mirror/gcc/blob/master/COPYING.RUNTIME#L61-L66)
applies.

The modules `dd.cudd` and `dd.cudd_zdd` in the wheel dynamically link to the:

- Linux kernel (in particular [`linux-vdso.so.1`](
    https://man7.org/linux/man-pages/man7/vdso.7.html)),
  which allows system calls (see the kernel's file [`COPYING`](
    https://github.com/torvalds/linux/blob/master/COPYING) and the explicit
  syscall exception in the file [`LICENSES/exceptions/Linux-syscall-note`](
    https://github.com/torvalds/linux/blob/master/LICENSES/exceptions/Linux-syscall-note))
- [GNU C Library](https://www.gnu.org/software/libc/) (glibc) (in particular
  `libpthread.so.0`, `libc.so.6`, `/lib64/ld-linux-x86-64.so.2`), which uses
  the [LGPLv2.1](https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=COPYING.LIB;hb=HEAD)
  that allows dynamic linking, and other [licenses](
    https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=LICENSES;hb=HEAD).
  These licenses are included in the wheel file and apply to the GNU C Library
  that is dynamically linked.


## Installing the development version

For installing the development version of `dd` from the `git` repository,
an alternative to cloning the repository and installing from the cloned
repository is to [use `pip` for doing so](
    https://pip.pypa.io/en/stable/cli/pip_install/#argument-handling):

```shell
pip install https://github.com/tulip-control/dd/archive/main.tar.gz
```

or with [`pip` using `git`](
    https://pip.pypa.io/en/stable/topics/vcs-support/#git)
(this alternative requires that `git` be installed):

```shell
pip install git+https://github.com/tulip-control/dd
```

A `git` URL can be passed also to [`pip download`](
    https://pip.pypa.io/en/stable/cli/pip_download/#overview),
for example:

```shell
pip download --no-deps https://github.com/tulip-control/dd/archive/main.tar.gz
```

The extension `.zip` too can be used for the name of the [archive file](
    https://en.wikipedia.org/wiki/Archive_file)
in the URL. Analogously, with `pip` using `git`:

```shell
pip download --no-deps git+https://github.com/tulip-control/dd
```

Note that the naming of paths *within* the archive file downloaded from
GitHub in this way will differ, depending on whether `https://` or
`git+https://` is used.


Tests
=====

Use [`pytest`](https://pypi.org/project/pytest). Run with:

```shell
cd tests/
pytest -v --continue-on-collection-errors .
```

Tests of Cython modules that were not installed will fail.
The code is covered well by tests.


License
=======
[BSD-3](https://opensource.org/licenses/BSD-3-Clause), see file `LICENSE`.


[build_img]: https://github.com/tulip-control/dd/actions/workflows/main.yml/badge.svg?branch=main
[ci]: https://github.com/tulip-control/dd/actions
