#!/usr/bin/env python3
import unittest

from .GuiShareTest import GuiShareTest

class Local404PublicModeRateLimitTest(unittest.TestCase, GuiShareTest):
    @classmethod
    def setUpClass(cls):
        test_settings = {
            "close_after_first_download": False,
            "public_mode": True
        }
        cls.gui = GuiShareTest.set_up(test_settings)

    @classmethod
    def tearDownClass(cls):
        GuiShareTest.tear_down()

    def test_gui(self):
        self.run_all_common_setup_tests()
        self.run_all_share_mode_tests(True, True)
        self.hit_404(True)

if __name__ == "__main__":
    unittest.main()
