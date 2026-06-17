# 石头剪刀布蜥蜴斯波克 / Rock Paper Scissors Lizard Spock

一个使用 Python 标准库实现的控制台对战小游戏。玩家和电脑进行多回合 Rock Paper Scissors Lizard Spock 对决，支持中英双语、难度设置、音效、音量、排行榜和自动化测试。

A pure Python standard-library console game. Play multi-round Rock Paper Scissors Lizard Spock against the computer, with bilingual zh/en UI, difficulty settings, terminal sound, volume control, score history, and automated tests.

## 功能 / Features

- 纯 Python 标准库，无第三方依赖 / Pure Python stdlib, no third-party dependencies
- 中英双语界面 / Bilingual zh/en interface
- 三档难度：easy / normal / hard / Three difficulty levels
- 经典五手势规则 / Classic five-move RPSLS rules
- 连胜加分 / Streak bonus scoring
- JSON 持久化设置和排行榜 / Persistent JSON settings and top scores
- 终端铃声音效，音量 0-3 / Terminal bell sound with volume 0-3
- 自动化测试覆盖核心规则、菜单、设置、音效和排行榜 / Tests cover core rules, menus, settings, sound, and scores

## 快速开始 / Quick start

```bash
cd ~/games/rpsls
python3 game.py
```

## 操作 / Controls

主菜单 / Main menu:

| 输入 / Input | 作用 / Action |
|---|---|
| `p` | 开始游戏 / play |
| `h` | 帮助 / help |
| `s` | 设置 / settings |
| `c` | 排行榜 / scores |
| `q` | 退出 / quit |

出招 / Moves:

| 快捷键 / Key | 英文 / English | 中文 / Chinese |
|---|---|---|
| `r` | rock | 石头 |
| `p` | paper | 布 |
| `s` | scissors | 剪刀 |
| `l` | lizard | 蜥蜴 |
| `k` | spock | 斯波克 |
| `q` | quit round | 退出本局 |

## 规则 / Rules

- rock crushes scissors / lizard
- paper covers rock, disproves spock
- scissors cuts paper, decapitates lizard
- lizard poisons spock, eats paper
- spock smashes scissors, vaporizes rock

中文界面会显示对应的中文动作描述。
The Chinese UI displays localized action verbs.

## 难度与计分 / Difficulty and scoring

| 难度 / Difficulty | 回合数 / Rounds | 基础胜利分 / Base win points |
|---|---:|---:|
| easy | 3 | 10 |
| normal | 5 | 15 |
| hard | 7 | 20 |

每次胜利得分 / Win points:

```text
base + (current_win_streak - 1) * 5
```

平局得 2 分，失败不得分。比赛结束后，如果玩家胜场多于电脑则获胜。
Draws give 2 points. Losses give 0. The player wins the match by winning more rounds than the computer.

## 测试 / Tests

```bash
cd ~/games/rpsls
python3 -m py_compile game.py rpsls.py i18n.py settings.py score.py sound.py
python3 tests/run_tests.py
```

当前测试数量 / Current test count: 58.

## 文件结构 / Project layout

```text
rpsls/
├── game.py          # 主菜单与对局 / menus and gameplay
├── rpsls.py         # 核心规则 / core rules
├── i18n.py          # 中英文本 / bilingual strings
├── settings.py      # 设置保存 / settings persistence
├── score.py         # 排行榜 / scoreboard
├── sound.py         # 终端音效 / terminal sound
└── tests/
    ├── test_core.py
    ├── test_game.py
    ├── test_modules.py
    └── run_tests.py
```
