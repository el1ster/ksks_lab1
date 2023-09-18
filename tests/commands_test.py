import unittest
import io
import unittest.mock
from server import parse_command, process_command


class TestCommands(unittest.TestCase):

    def test_parse_command_valid(self):
        # Test valid command
        command_bytes = b'draw pixel:1,2,red'
        result = parse_command(command_bytes)
        self.assertEqual(result, ('draw pixel', ['1', '2', 'red']))

    def test_parse_command_invalid(self):
        command_bytes = b'invalid command'
        result = parse_command(command_bytes)
        self.assertIsNone(result)

    def test_process_command_draw_pixel(self):
        command = ('draw pixel', ['1', '2', 'red'])
        expected_output = "Виконано команду: draw pixel, x0: 1, y0: 2, color: red"

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            process_command(command)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_process_command_invalid_command(self):
        command = ('draw pixel', ['1', '2', '3', 'red'])
        expected_output = "Помилка: невірна кількість параметрів"

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            process_command(command)
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
