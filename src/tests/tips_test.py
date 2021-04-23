import unittest
from src.tips import Tips


class DBWrapperStub:
    def __init__(self):
        pass

    def insert(self, fields: dict):
        return True

    # kun varsinaine metodi on valmis muutetaan paluuarvo.
    def display_all_tips(self, user_id):
        return [('Arto Paasilinna', 'www.testi.fi', 'Testi')]

    # kun varsinaine metodi on valmis muutetaan paluuarvo.
    def search_by_writer_name(self, nimi, user_id):
        return [('Arto Paasilinna', 'www.testi.fi', 'Testi')]

    def delete_tip(self,fields):
      return True

    def display_all_tips_all_users(self):
        return [('Arto Paasilinna', 'www.testi.fi', 'Testi')]


  


class TestTips(unittest.TestCase):
    def setUp(self):
        self.tips = Tips(DBWrapperStub())

    def test_add_tip(self):
        tip = self.tips.add_tip(
            "Arto Paasilinna", "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111", "Ylpeys ja ennakkoluulo")
        self.assertEqual(tip, True)

    def test_too_long_name(self):
        tip = self.tips.add_tip(
            "Arto Paasilinna ja perään aivan liian monta merkkiä että tulee false tästä tarkastuksesta kun on 101!",
            "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111", "Ylpeys ja ennakkoluulo")
        self.assertEqual(tip, False)

    def test_too_long_url(self):
        tip = self.tips.add_tip(
            "Arto Paasilinna",
            "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111/jaturhaa-koodia-peraan-etta-tulee-hylky/kun-merkkeja-tahan-tulee-201-etta-on-juurikin/raja-arvon-ylittava-maara-merkkeja", "Ylpeys ja ennakkoluulo")
        self.assertEqual(tip, False)

    def test_non_allowed_character_in_name(self):
        tip = self.tips.add_tip(
            "Arto=Paasilinna", "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111", "Ylpeys ja ennakkoluulo")
        self.assertEqual(tip, False)


    def test_illegal_name_search_by_writer_name(self):
        tip = self.tips.search_by_writer_name("Arto Paasilinna&")
        self.assertEqual(tip, None)

    def test_legal_name_search(self):
      self.assertEqual(self.tips.search_by_writer_name("Arto Paasilinna"), [('Arto Paasilinna', 'www.testi.fi', 'Testi')])

    def test_delete_method(self):
      self.assertEqual(self.tips.delete_tip(1), True)

    def test_display_all_all_users(self):
        self.assertEqual(self.tips.display_all_all_users(), [('Arto Paasilinna', 'www.testi.fi', 'Testi')])