import unittest

from guess_number import play


class GuessNumberTests(unittest.TestCase):
    def run_game(self, answers, secret=42):
        answers = iter(answers)
        messages = []
        play(secret, lambda prompt: next(answers), messages.append)
        return messages

    def test_hints_and_win(self):
        messages = self.run_game(["20", "60", "42"])
        self.assertIn("小了，再试试！", messages)
        self.assertIn("大了，再试试！", messages)
        self.assertIn("一共猜了 3 次", messages[-1])

    def test_invalid_inputs_do_not_count(self):
        messages = self.run_game(["hello", "", "1.5", "0", "101", "42"])
        self.assertEqual(messages.count("请输入整数，例如 50；或输入 q 退出。"), 3)
        self.assertEqual(messages.count("数字要在 1～100 之间哦。"), 2)
        self.assertIn("一共猜了 1 次", messages[-1])

    def test_quit(self):
        self.assertEqual(self.run_game([" Q "])[-1], "游戏结束，下次再来！")

    def test_boundaries(self):
        for secret in (1, 100):
            with self.subTest(secret=secret):
                self.assertIn("猜对了", self.run_game([str(secret)], secret)[-1])

    def test_input_interrupted(self):
        for error in (EOFError, KeyboardInterrupt):
            with self.subTest(error=error):
                def interrupted(prompt):
                    raise error
                messages = []
                play(42, interrupted, messages.append)
                self.assertEqual(messages[-1], "游戏结束，下次再来！")


if __name__ == "__main__":
    unittest.main()
