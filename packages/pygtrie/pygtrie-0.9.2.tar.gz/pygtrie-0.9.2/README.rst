pygtrie
=======

pygtrie is a Python library implementing a trie data structure.

Trie data structure, also known as radix or prefix tree, is a tree
associating keys to values where all the descendants of a node have
a common prefix (associated with that node).

The trie module contains :class:`trie.Trie`, :class:`trie.CharTrie`
and :class:`trie.StringTrie` classes each implementing a mutable
mapping interface, i.e. :class:`dict` interface.  As such, in most
circumstances, :class:`trie.Trie` could be used as a drop-in
replacement for a :class:`dict`, but the prefix nature of the data
structure is trie’s real strength.

The module also contains :class:`trie.PrefixSet` class which uses
a trie to store a set of prefixes such that a key is contained in the
set if it or its prefix is stored in the set.

Features
--------

- A full mutable mapping implementation.

- Supports iterating over as well as deleting a subtrie.

- Supports prefix checking as well as shortest and longest prefix
  look-up.

- Extensible for any kind of user-defined keys.

- A PrefixSet supports “all keys starting with given prefix” logic.

- Can store any value including None.

Installation
------------

To install bz2file, run::

    pip install pygtrie

Or download the sources and save ``trie.py`` file with your project.
