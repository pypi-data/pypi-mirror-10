# GetName

Get cat/dog/superhero/supervillain names.

I just combine [@sindresorhus][]'s four staffs into this one.

* [cat-names][]
* [dog-names][]
* [superheroes][]
* [supervillains][]

## Install

```shell
$ pip install getname
```

## Usage

### API

`random(the_type, gender, showall)`

* type: cat/dog/superhero/supervillian.
* gender: female/male, **only** for dog names.
* showall: True/False, show all the names.

```python
>>> from getname import random_name
>>> random_name('cat')
u'Angel'
>>> random_name('dog', gender='female')
u'Maggie'
>>> random_name('superhero', showall=True)
[u'3-D Man', u'A-Bomb', u'A.I.M.', ...]
```

### CLI

```shell
$ getname dog
Angel
$ getname dog -f
Lady
$ getname dog --showall
[u'Max', u'Buddy',...]
```

Use `getname -h` to get help message about each usage.

```shell
Usage: getname [OPTIONS] COMMAND [ARGS]...

  Get popular cat/dog/superhero/supervillain names.

Options:
  -v, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  cat      Get popular cat names.
  dog      Get popular dog names.
  superhero     Get superhero names.
  supervillain  Get supervillain names.
```

Use `getname cat/dog/superhero/supervillain -h` to get help message about the specified type.

## Tests

```shell
$ pip install -r dev-requirements.txt
$ invoke test
```

## Credits

All the glories should belong to [@sindresorhus][], I just port it to python :)

## License

MIT.

[@sindresorhus]: https://github.com/sindresorhus
[dog-names]: https://github.com/sindresorhus/dog-names
[cat-names]: https://github.com/sindresorhus/cat-names
[superheroes]: https://github.com/sindresorhus/superheroes
[supervillains]: https://github.com/sindresorhus/supervillains
