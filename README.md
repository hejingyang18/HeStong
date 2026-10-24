# HeStong
# 我的 GitHub 学习之旅

这是我的第一个 GitHub 仓库！

## 学习目标
- 学会使用 GitHub
- 学会 Python 编程
- 使用 Codex 辅助开发小游戏

## 学习记录
- Day 1：创建仓库，学习 Commit
- Day 2：用 Python 编写猜数字小游戏，运行自动测试，练习 Git 上传。

## 猜数字小游戏

需要 Python 3，无需安装第三方库。在 Windows PowerShell 中进入仓库文件夹后运行：

```powershell
py guess_number.py
```

电脑随机选择一个 1～100 的整数。输入猜测后，会提示大了或小了；猜中后显示有效猜测次数。输入 q 退出，输错内容不会计入次数。

运行自动测试：

```powershell
py -m unittest -v
```

## 第二课：Git 命令练习

首次下载仓库（已有本地仓库时不用重复执行）：

```powershell
git clone https://github.com/hejingyang18/HeStong.git
cd HeStong
```

修改文件并测试后，按顺序执行：

```powershell
git status
git add guess_number.py test_guess_number.py README.md .gitignore
git commit -m "Add Python guess number game and tests"
git push origin main
```

- `status`：查看哪些文件发生了变化。
- `add`：选择本次要提交的文件，放入暂存区。
- `commit`：在电脑上保存一个有说明的版本。
- `push`：将本地提交上传到 GitHub。

理解代码可以从三个地方开始：`random.randint(1, 100)` 生成答案；`while True` 重复接收输入；`if / elif / else` 判断猜测是小了、大了还是正确。
