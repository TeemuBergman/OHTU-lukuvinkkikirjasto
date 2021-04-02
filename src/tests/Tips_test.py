import unittest
from tips import Tips


class TestTips(unittest.TestCase):
    def setUp(self):
        self.tips = Tips()

    def test_add_tip(self):
        tip = self.tips.add_tip("Arto Paasilinna", "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111")
        self.assertEqual(tip, True)

    def test_too_long_name(self):
        tip = self.tips.add_tip("Arto Paasilinna ja perään aivan liian monta merkkiä että tulee false tästä tarkastuksesta kun on 101!", "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111")
        self.assertEqual(tip, False)

    def test_too_long_url(self):
        tip = self.tips.add_tip("Arto Paasilinna", "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111/jaturhaa-koodia-peraan-etta-tulee-hylky/kun-merkkeja-tahan-tulee-201-etta-on-juurikin/raja-arvon-ylittava-maara-merkkeja")
        self.assertEqual(tip, False)

    def test_non_allowed_character_in_name(self):
        tip = self.tips.add_tip("Arto=Paasilinna", "https://www.wsoy.fi/kirja/arto-paasilinna/hurmaava-joukkoitsemurha/9789510426111")
        self.assertEqual(tip, False)