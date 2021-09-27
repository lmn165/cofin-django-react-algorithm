import unittest
from basic.models_oop import Calculator, Grade, Contacts

class TestCalculator(unittest.TestCase):
    cal = Calculator()
    cal.num1 = 8
    cal.num2 = 5

    def test_add(self):
        self.assertEqual(self.cal.add(), 13)

    def test_sub(self):
        self.assertEqual(self.cal.subtract(), 3)

    def test_multi(self):
        self.assertEqual(self.cal.multiple(), 40)

    def test_div(self):
        self.assertEqual(self.cal.divide(), 1.6)

    def test_mod(self):
        self.assertEqual(self.cal.remain(), 3)


class TestPerson(unittest.TestCase):
    pass


class TestGrade(unittest.TestCase):

    def test_grade(self):
        grade = Grade()
        grade.kor = 92
        grade.eng = 78
        grade.math = 85
        self.assertEqual(grade.return_grade(), 'B')


class TestContacts(unittest.TestCase):

    def test_contact(self):
        contact = Contacts('비트', '010-0000-0000', '강남', 'bit@bit.com')
        # print("\n"+contact.to_string())
        self.assertEqual(contact.to_string(), '비트, 010-0000-0000, 강남, bit@bit.com')

    def test_contacts(self):
        ls = []
        ls.append(Contacts.set_contact('비트', '010-0000-0000', '강남', 'bit@bit.com'))
        ls.append(Contacts.set_contact('Bit', '010-0000-1234', '강서', 'bit@gmail.com'))
        ls.append(Contacts.set_contact('Camp', '010-0000-5678', '강북', 'bit@naver.com'))
        # [print('\n' + i.to_string()) for i in ls]

    def test_del_contact(self):
        ls = []
        ls.append(Contacts.set_contact('비트', '010-0000-0000', '강남', 'bit@bit.com'))
        ls.append(Contacts.set_contact('Bit', '010-0000-1234', '강서', 'bit@gmail.com'))
        ls.append(Contacts.set_contact('Camp', '010-0000-5678', '강북', 'bit@naver.com'))
        ls = Contacts.del_contact(ls, '비트')
        # [print('\n'+i.to_string()) for i in ls]

if __name__ == '__main__':
    unittest.main()