import argparse
import io
import unittest
from contextlib import redirect_stdout

import adcs_audit


class SafeDisplayTests(unittest.TestCase):
    def test_escapes_terminal_controls_and_line_breaks(self):
        self.assertEqual(
            adcs_audit.safe_display("host\x1b[31m\r\nnext"),
            r"host\x1b[31m\r\nnext",
        )

    def test_escapes_bidi_control_but_preserves_printable_unicode(self):
        self.assertEqual(
            adcs_audit.safe_display("café\u202eexample"),
            r"café\u202eexample",
        )

    def test_run_displays_target_and_output_safely(self):
        args = argparse.Namespace(target="host\n[ forged ]", output="report\x1b[2J")
        output = io.StringIO()

        with redirect_stdout(output):
            result = adcs_audit.run(args)

        self.assertEqual(result, 0)
        self.assertIn(r"[*] target : host\n[ forged ]", output.getvalue())
        self.assertIn(r"[*] output : report\x1b[2J", output.getvalue())
        self.assertNotIn("\x1b", output.getvalue())
        self.assertNotIn("\r", output.getvalue())


if __name__ == "__main__":
    unittest.main()
