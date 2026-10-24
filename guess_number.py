"""运行 py guess_number.py，开始猜数字。"""

import random


def play(secret=None, input_fn=input, output_fn=print):
    """允许传入固定答案，方便自动测试。"""
    if secret is None:
        secret = random.randint(1, 100)
    attempts = 0
    output_fn("我想好了一个 1～100 的整数，来猜猜吧！输入 q 退出。")
    while True:
        try:
            text = input_fn("请输入你的猜测：").strip()
        except (EOFError, KeyboardInterrupt):
            output_fn("游戏结束，下次再来！")
            return
        if text.lower() == "q":
            output_fn("游戏结束，下次再来！")
            return
        try:
            guess = int(text)
        except ValueError:
            output_fn("请输入整数，例如 50；或输入 q 退出。")
            continue
        if not 1 <= guess <= 100:
            output_fn("数字要在 1～100 之间哦。")
            continue
        attempts += 1
        if guess < secret:
            output_fn("小了，再试试！")
        elif guess > secret:
            output_fn("大了，再试试！")
        else:
            output_fn(f"猜对了！答案是 {secret}，你一共猜了 {attempts} 次。")
            return


if __name__ == "__main__":
    play()
