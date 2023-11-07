import random
from pathlib import Path
from typing import Dict, List

import simpleaudio as sa

from blivedm.models.web import DanmakuMessage

try:
    import ujson as json
except ImportError:
    import json
player = None


async def play_mp3(mp3: Path):
    global player
    # 打开音频文件
    with Path(mp3).open("rb") as audio_file:
        # 读取音频文件信息
        nchannels, sampwidth, framerate, nframes = audio_file.getparams()[:4]

        # 创建音频缓冲区
        audio_data = audio_file.readframes(nframes)

        # 如果播放器对象还未创建，则创建播放器对象
        if player is None:
            player = sa.play_buffer(audio_data, nchannels, sampwidth, framerate)
        else:
            # 如果播放器对象已存在，则停止当前的播放并生成新的音频数据
            player.stop()
            player = sa.play_buffer(audio_data, nchannels, sampwidth, framerate)

        # 播放音频
        player.play()

        # 等待播放完成
        player.wait_done()
        mp3.unlink()


async def msg_push(msg_info: DanmakuMessage):
    """从字典中返回结果"""
    anime_thesaurus_path = Path("data/data.json")
    anime_thesaurus: Dict[str, List[str]] = json.load(
        anime_thesaurus_path.open("r", encoding="utf-8"),
    )
    send_msg = None
    keys = anime_thesaurus.keys()
    for key in keys:
        if key in msg_info.msg:
            send_msg: str = random.choice(anime_thesaurus[key]).replace(
                "你",
                msg_info.uname,
            )
            break
    if send_msg is None:
        return
    with Path("danmu.txt").open("w", encoding="utf-8") as f:
        f.write(send_msg)
