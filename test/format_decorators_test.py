import format_decorators
import unittest


class FormatDecoratorTest(unittest.TestCase):
    def test_format_task(self):
        rows = [
            ["1", "NOTE", "THIS IS A NOTE", "2020-09-11 14:57:22"],
            ["2", "NOTE", "THIS IS ANOTHER NOTE", "2020-09-11 14:57:22"],
        ]
        formatted_rows = format_decorators.format_note(rows)
        self.assertEqual(
            "NOTE: 1    [Date set: 2020-09-11 14:57:22] THIS IS A NOTE",
            formatted_rows[0],
        )
