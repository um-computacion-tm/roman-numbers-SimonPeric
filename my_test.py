import unittest

from my_romanos import decimal2roman

class TestDecimalToRoman(unittest.TestCase):

    def test_uno(self):

        resultado = decimal2roman(1)

        self.assertEqual(resultado, 'I')


    def test_diez(self):

        resultado = decimal2roman(10)

        self.assertEqual(resultado, 'X')


    def test_cinco(self):

        resultado = decimal2roman(5)

        self.assertEqual(resultado, 'V')


    def test_dos(self):

        resultado = decimal2roman(2)

        self.assertEqual(resultado, 'II')


    def test_tres(self):

        resultado = decimal2roman(3)

        self.assertEqual(resultado, 'III')


    def test_4(self):

        resultado = decimal2roman(4)

        self.assertEqual(resultado, 'IV')


    def test_6(self):

        resultado = decimal2roman(6)

        self.assertEqual(resultado, 'VI')


    def test_7(self):

        resultado = decimal2roman(7)

        self.assertEqual(resultado, 'VII')


    def test_8(self):

        resultado = decimal2roman(8)

        self.assertEqual(resultado, 'VIII')


    def test_9(self):

        resultado = decimal2roman(9)

        self.assertEqual(resultado, 'IX')


    def test_11(self):

        resultado = decimal2roman(11)

        self.assertEqual(resultado, 'XI')


    def test_13(self):

        resultado = decimal2roman(13)

        self.assertEqual(resultado, 'XIII')


    def test_16(self):

        resultado = decimal2roman(16)

        self.assertEqual(resultado, 'XVI')


    def test_24(self):

        resultado = decimal2roman(24)

        self.assertEqual(resultado, 'XXIV')


    def test_35(self):

        resultado = decimal2roman(35)

        self.assertEqual(resultado, 'XXXV')


    def test_46(self):

        resultado = decimal2roman(46)

        self.assertEqual(resultado, 'XLVI')


    def test_57(self):

        resultado = decimal2roman(57)

        self.assertEqual(resultado, 'LVII')


    def test_68(self):

        resultado = decimal2roman(68)

        self.assertEqual(resultado, 'LXVIII')


    def test_89(self):

        resultado = decimal2roman(89)

        self.assertEqual(resultado, 'LXXXIX')


    def test_99(self):

        resultado = decimal2roman(99)

        self.assertEqual(resultado, 'XCIX')


    def test_100(self):

        resultado = decimal2roman(100)

        self.assertEqual(resultado, 'C')


    def test_111(self):

        resultado = decimal2roman(111)

        self.assertEqual(resultado, 'CXI')

    def test_222(self):

        resultado = decimal2roman(222)

        self.assertEqual(resultado, 'CCXXII')

    def test_333(self):

        resultado = decimal2roman(333)

        self.assertEqual(resultado, 'CCCXXXIII')

    def test_444(self):

        resultado = decimal2roman(444)

        self.assertEqual(resultado, 'CDXLIV')

    def test_555(self):

        resultado = decimal2roman(555)

        self.assertEqual(resultado, 'DLV')

    def test_666(self):

        resultado = decimal2roman(666)

        self.assertEqual(resultado, 'DCLXVI')

    def test_999(self):

        resultado = decimal2roman(999)

        self.assertEqual(resultado, 'CMXCIX')

    def test_1999(self):

        resultado = decimal2roman(1999)

        self.assertEqual(resultado, 'MCMXCIX')


if __name__ == '__main__':

    unittest.main()