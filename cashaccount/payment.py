import base58

import cashaddress


class _Info:
    TYPE_BYTE = None  # override with fixed value
    NAME = None       # override with fixed value

    def base(self):
        """Return a human string for sites like cashaccount.info"""
        raise NotImplementedError

    def _data_hex(self):
        """Return the data payload of the cash account hex."""
        raise NotImplementedError

    def cashaccount_hex(self):
        """Return the full payment info string as <Payment Type + Payment Data>."""
        return '{:02x}{}'.format(self.TYPE_BYTE, self._data_hex().lower())

    def __str__(self):
        return ('{}\n'
                'base:            {}\n'
                'cashaccount hex: {}'.format(self.NAME, self.base(), self.cashaccount_hex()))


class KeyHashInfo(_Info):
    """Key Hash data is the 20 byte hash160 address data (no version prefix, no checksum suffix)."""
    TYPE_BYTE = 0x01
    NAME = 'Key Hash (P2PKH) Info'

    def __init__(self, address_string):
        address = _normalize(address_string)
        self._validate_version(address.version)
        self._address = address
        self._hash160_hex = _extract_hash160(address)

    def base(self):
        return self._address.cash_address()

    def _data_hex(self):
        return self._hash160_hex

    @staticmethod
    def _validate_version(v):
        if not v.startswith('P2PKH'):
            raise ValueError('expected a P2PKH address but got {}'.format(v))


class ScriptHashInfo(KeyHashInfo):
    TYPE_BYTE = 0x02
    NAME = 'Script Hash (P2SH) Info'

    @staticmethod
    def _validate_version(v):
        if not v.startswith('P2SH'):
            raise ValueError('expected a P2SH address but got {}'.format(v))


def _normalize(address_string):
    """Convert legacy or cashaddr string to an address object.

    Raises ValueError for invalid address strings.
    """
    if _looks_like_cashaddr_without_prefix(address_string):
        address_string = 'bitcoincash:{}'.format(address_string)

    # get an address object that is independent of the input format
    try:
        return cashaddress.convert.Address.from_string(address_string)
    except cashaddress.convert.InvalidAddress as e:
        raise ValueError('unable to interpret address: {}'.format(e))


def _looks_like_cashaddr_without_prefix(s):
    if s[0] not in ['p', 'q']:
        return False
    return True


def _extract_hash160(address):
    no_checksum = base58.b58decode_check(address.legacy_address())
    no_version_no_checksum = no_checksum[1:]
    return no_version_no_checksum.hex()
