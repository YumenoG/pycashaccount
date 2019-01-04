import unittest

import cashaccount.payment as pay


class TestKeyHashInfo(unittest.TestCase):
    P2PKH_CASHADDRESS = 'bitcoincash:qrme8l598x49gmjhn92dgwhk5a3znu5wfcf5uf94e9'
    P2PKH_LEGACY = '1Pa5CCeYCpWXFJXRnhZpmhJRuFg184HGHz'
    P2PKH_HEX160 = 'f793fe8539aa546e579954d43af6a76229f28e4e'
    P2PKH_INFO = '01' + P2PKH_HEX160

    P2SH_CASHADDRESS = 'bitcoincash:pp4d24pemra2k3mths8cjxpuu6yl3a5ctvcp8mdkm9'
    P2SH_LEGACY = '3BRu7EhouApLkW1EZ64T9o9yMuX5Rexz6f'
    P2SH_HEX160 = '6ad55439d8faab476bbc0f89183ce689f8f6985b'
    P2SH_INFO = '01' + P2SH_HEX160

    def test_works_for_p2pkh_cashaddress(self):
        self.assertEqual(pay.PaymentKeyHash(self.P2PKH_CASHADDRESS).hexlike(), self.P2PKH_INFO)
        # allow missing bitcoincash prefix
        self.assertEqual(pay.PaymentKeyHash(self.P2PKH_CASHADDRESS.replace('bitcoincash:', '')).hexlike(), self.P2PKH_INFO)

    def test_works_for_p2pkh_legacy(self):
        self.assertEqual(pay.PaymentKeyHash(self.P2PKH_LEGACY).hexlike(), self.P2PKH_INFO)

    def test_works_for_p2sh_cashaddress(self):
        self.assertEqual(pay.PaymentKeyHash(self.P2SH_CASHADDRESS).hexlike(), self.P2SH_INFO)
        # allow missing bitcoincash prefix
        self.assertEqual(pay.PaymentKeyHash(self.P2SH_CASHADDRESS.replace('bitcoincash:', '')).hexlike(), self.P2SH_INFO)

    def test_works_for_p2sh_legacy(self):
        self.assertEqual(pay.PaymentKeyHash(self.P2SH_LEGACY).hexlike(), self.P2SH_INFO)

    def test_raises_some_exception_for_invalid_addresses(self):
        with self.assertRaises(Exception):
            pay.PaymentKeyHash('invalid address')
        with self.assertRaises(Exception):
            pay.PaymentKeyHash('qstillinvalid')

    def test_string_has_useful_info(self):
        expected = 'Key Hash\n' \
                   'type: 1\n' \
                   'data: {}'.format(self.P2PKH_HEX160)
        info = pay.PaymentKeyHash(self.P2PKH_CASHADDRESS)
        self.assertEqual(str(info), expected)
