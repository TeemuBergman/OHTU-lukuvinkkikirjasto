import unittest
from tips import Tips

class DB_wrapper_stub():
    def __init__(self):
        pass

    def insert(self, fields: dict):
        return True


    # kun varsinaine metodi on valmis muutetaan paluuarvo.
    def display_all_tips(self):
        return None

    # kun varsinaine metodi on valmis muutetaan paluuarvo.
    def search_by_writer_name(self, nimi):
        return None




class TestTips(unittest.TestCase):
    def setUp(self):
        self.tips = Tips(DB_wrapper_stub())

    def test_add_tip(self):
        tip = self.tips.add_tip(
            "Arto Paasilinna", "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111")
        self.assertEqual(tip, True)

    def test_too_long_name(self):
        tip = self.tips.add_tip("Arto Paasilinna ja perään aivan liian monta merkkiä että tulee false tästä tarkastuksesta kun on 101!",
                                "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111")
        self.assertEqual(tip, False)

    def test_too_long_url(self):
        tip = self.tips.add_tip(
            "Arto Paasilinna", "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111/jaturhaa-koodia-peraan-etta-tulee-hylky/kun-merkkeja-tahan-tulee-201-etta-on-juurikin/raja-arvon-ylittava-maara-merkkeja")
        self.assertEqual(tip, False)

    def test_non_allowed_character_in_name(self):
        tip = self.tips.add_tip(
            "Arto=Paasilinna", "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111")
        self.assertEqual(tip, False)
