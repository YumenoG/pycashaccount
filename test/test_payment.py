import unittest

import cashaccount.payment as pay


class TestKeyHashInfo(unittest.TestCase):
    CASHADDRESS = 'bitcoincash:qrme8l598x49gmjhn92dgwhk5a3znu5wfcf5uf94e9'
    LEGACY = '1Pa5CCeYCpWXFJXRnhZpmhJRuFg184HGHz'
    HEX160 = 'f793fe8539aa546e579954d43af6a76229f28e4e'
    CASHACCOUNT_HEX = '01' + HEX160

    def test_makes_correct_cashaccount_hex(self):
        # allow cashaddress
        self.assertEqual(pay.KeyHashInfo(self.CASHADDRESS).cashaccount_hex(), self.CASHACCOUNT_HEX)
        # allow missing bitcoincash prefix
        self.assertEqual(pay.KeyHashInfo(self.CASHADDRESS.replace('bitcoincash:', '')).cashaccount_hex(), self.CASHACCOUNT_HEX)
        # allow legacy
        self.assertEqual(pay.KeyHashInfo(self.LEGACY).cashaccount_hex(), self.CASHACCOUNT_HEX)

    def test_makes_correct_base_info(self):
        self.assertEqual(pay.KeyHashInfo(self.CASHADDRESS).base(), self.CASHADDRESS)

    def test_raises_ValueError_for_invalid_addresses(self):
        with self.assertRaises(ValueError):
            pay.KeyHashInfo('invalid address')
        with self.assertRaises(ValueError):
            pay.KeyHashInfo(TestScriptHashInfo.CASHADDRESS)

    def test_string_has_useful_info(self):
        expected = ('Key Hash (P2PKH) Info\n'
                    'base:            {}\n'
                    'cashaccount hex: {}'.format(self.CASHADDRESS, self.CASHACCOUNT_HEX))
        info = pay.KeyHashInfo(self.CASHADDRESS)
        self.assertEqual(str(info), expected)


class TestScriptHashInfo(unittest.TestCase):
    CASHADDRESS = 'bitcoincash:pp4d24pemra2k3mths8cjxpuu6yl3a5ctvcp8mdkm9'
    LEGACY = '3BRu7EhouApLkW1EZ64T9o9yMuX5Rexz6f'
    HEX160 = '6ad55439d8faab476bbc0f89183ce689f8f6985b'
    CASHACCOUNT_HEX = '02' + HEX160

    def test_makes_correct_cashaccount_hex(self):
        self.assertEqual(pay.ScriptHashInfo(self.CASHADDRESS).cashaccount_hex(), self.CASHACCOUNT_HEX)
        # allow missing bitcoincash prefix
        self.assertEqual(pay.ScriptHashInfo(self.CASHADDRESS.replace('bitcoincash:', '')).cashaccount_hex(), self.CASHACCOUNT_HEX)
        # allow legacy
        self.assertEqual(pay.ScriptHashInfo(self.LEGACY).cashaccount_hex(), self.CASHACCOUNT_HEX)

    def test_makes_correct_base_info(self):
        self.assertEqual(pay.ScriptHashInfo(self.CASHADDRESS).base(), self.CASHADDRESS)

    def test_raises_ValueError_for_invalid_addresses(self):
        with self.assertRaises(ValueError):
            pay.ScriptHashInfo('invalid address')
        with self.assertRaises(ValueError):
            pay.ScriptHashInfo(TestKeyHashInfo.CASHADDRESS)

    def test_string_has_useful_info(self):
        expected = ('Script Hash (P2SH) Info\n'
                    'base:            {}\n'
                    'cashaccount hex: {}'.format(self.CASHADDRESS, self.CASHACCOUNT_HEX))
        info = pay.ScriptHashInfo(self.CASHADDRESS)
        self.assertEqual(str(info), expected)


class TestBaseInfo(unittest.TestCase):
    def test_raises_errors_if_abstract_methods_not_implemented(self):
        info = pay._Info()
        with self.assertRaises(NotImplementedError):
            info.base()
        with self.assertRaises(NotImplementedError):
            info.cashaccount_hex()
        with self.assertRaises(NotImplementedError):
            str(info)
