# Cash Account Helper

You can already take payment information like an address and register a [cash account](https://gitlab.com/cash-accounts/specification) at [cashaccount.info](https://cashaccount.info).
I really recommend you do.

This CLI and library will help you prepare cash account registrations that you can broadcast yourself.


## Installation

Requires python3 for now.

`pip install pycashaccount`


## Status / ToDo

It is very basic still. Please file an issue if you have additional use cases for it.

- ~~OP_RETURN output for electron-cash op_return markdown~~
- ~~OP_RETURN hex-like output~~
- ~~p2sh output~~
- support payment codes
- generate raw hex output that common node CLIs can use


## CLI (command line interface) usage after installation

For example, get the information required for a key hash and script hash accounts:

```bash
p2pkh="bitcoincash:qrme8l598x49gmjhn92dgwhk5a3znu5wfcf5uf94e9"
p2sh="bitcoincash:pp4d24pemra2k3mths8cjxpuu6yl3a5ctvcp8mdkm9"

cashaccount keyhash name1 "$p2pkh"
cashaccount scripthash name2 "$p2sh" --opreturn-hex
```

Generally:

```bash
cashaccount payment_type name payment_info --formatting
```

Get help:

```bash
cashaccount --help

cashaccount keyhash --help
```


## CLI usage directly from repository

Same usage as the installed cli, except you can call it from the `cli` script at the repository root:

```bash
./cli --help
```


## Library usage

Look at `cashaccount/cli.py` for usage.

For example, create a registration from a name and payment information.

```python
from cashaccount import KeyHashInfo, Registration, opreturn

name = 'emergent_reasons'
info = KeyHashInfo('bitcoincash:qrme8l598x49gmjhn92dgwhk5a3znu5wfcf5uf94e9')
registration = Registration(name, info)
print(registration)
print(opreturn(registration))
```


## Contributions

Code contributions are welcome:

- Fork the repository and submit a pull request from your fork.
- Install test requirements `pip install -r requirements-test.txt`
- Update tests to cover any changes
- Confirm all tests pass before submitting a Pull Request (e.g. `pytest --cov-report term-missing --cov=cashaccount test/`)

Support donations are also welcome:

- `🌵emergent_reasons#100` (my first cash account - it points to `bitcoincash:qz3aq0uhltztqyjy2esa0lshadg9pf87yu7yealu3a`
- `☯Jonathan#100` (the primary creator of the cash account specification - it points to `bitcoincash:qr4aadjrpu73d2wxwkxkcrt6gqxgu6a7usxfm96fst`)
- [Electron Cash](https://electroncash.org/) If you are using electron cash special OP_RETURN features to post transactions, the team has donation information on the site.
