"""Bilingual strings."""

STRINGS = {
    "en": {
        "title": "Rock Paper Scissors Lizard Spock",
        "main_menu": "[P]lay  [H]elp  [S]ettings  S[c]ores  [Q]uit",
        "choice": "Choice: ",
        "bye": "Bye!",
        "unknown": "Unknown choice.",
        "help_title": "Help",
        "help_text": "Choose rock, paper, scissors, lizard, or spock. Shortcuts: r/p/s/l/k. Win more rounds than the computer.",
        "press_enter": "Press Enter to continue...",
        "settings": "Settings",
        "settings_menu": "1.Language  2.Sound  3.Volume  4.Difficulty  [B]ack",
        "lang": "Language",
        "sound": "Sound",
        "volume": "Volume",
        "difficulty": "Difficulty",
        "on": "on",
        "off": "off",
        "scores": "Scores",
        "no_scores": "No scores yet.",
        "name_prompt": "Name for score: ",
        "saved": "Score saved.",
        "not_saved": "Score not saved.",
        "round_status": "Round {round}/{total} | You {wins} - Computer {losses} | Draws {draws} | Score {score}",
        "move_prompt": "Move r/p/s/l/k or q: ",
        "invalid_move": "Invalid move.",
        "round_draw": "Draw: both chose {move}.",
        "round_win": "You win: {player} {verb} {computer}. +{points}",
        "round_loss": "You lose: {computer} {verb} {player}.",
        "result_win": "Match won! Score {score}",
        "result_loss": "Match lost. Score {score}",
        "result_draw": "Match drawn. Score {score}",
        "move_rock": "rock",
        "move_paper": "paper",
        "move_scissors": "scissors",
        "move_lizard": "lizard",
        "move_spock": "spock",
    },
    "zh": {
        "title": "石头剪刀布蜥蜴斯波克",
        "main_menu": "[P]开始  [H]帮助  [S]设置  [C]排行  [Q]退出",
        "choice": "选择：",
        "bye": "再见！",
        "unknown": "未知选择。",
        "help_title": "帮助",
        "help_text": "选择石头、布、剪刀、蜥蜴或斯波克。快捷键：r/p/s/l/k。赢得比电脑更多的回合。",
        "press_enter": "按回车继续...",
        "settings": "设置",
        "settings_menu": "1.语言  2.音效  3.音量  4.难度  [B]返回",
        "lang": "语言",
        "sound": "音效",
        "volume": "音量",
        "difficulty": "难度",
        "on": "开",
        "off": "关",
        "scores": "排行榜",
        "no_scores": "暂无分数。",
        "name_prompt": "输入名字保存分数：",
        "saved": "分数已保存。",
        "not_saved": "未保存分数。",
        "round_status": "第 {round}/{total} 回合 | 你 {wins} - 电脑 {losses} | 平局 {draws} | 分数 {score}",
        "move_prompt": "出招 r/p/s/l/k 或 q：",
        "invalid_move": "无效出招。",
        "round_draw": "平局：双方都是 {move}。",
        "round_win": "你赢了：{player} {verb} {computer}。+{points}",
        "round_loss": "你输了：{computer} {verb} {player}。",
        "result_win": "比赛胜利！分数 {score}",
        "result_loss": "比赛失败。分数 {score}",
        "result_draw": "比赛平局。分数 {score}",
        "move_rock": "石头",
        "move_paper": "布",
        "move_scissors": "剪刀",
        "move_lizard": "蜥蜴",
        "move_spock": "斯波克",
    },
}

VERBS_ZH = {
    "crushes": "压碎",
    "covers": "覆盖",
    "cuts": "剪断",
    "decapitates": "斩首",
    "poisons": "毒倒",
    "eats": "吃掉",
    "disproves": "反驳",
    "smashes": "砸烂",
    "vaporizes": "气化",
}


def t(lang, key, **kwargs):
    text = STRINGS.get(lang, STRINGS["en"]).get(key, key)
    try:
        return text.format(**kwargs)
    except Exception:
        return text


def move_name(lang, move):
    return t(lang, "move_" + move)


def verb(lang, word):
    if lang == "zh":
        return VERBS_ZH.get(word, word)
    return word
