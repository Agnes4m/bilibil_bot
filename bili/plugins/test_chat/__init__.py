from nonebot import on_command

# from nonebot.adapters import Event
from nonebot.adapters.bilibili.event import Danmu_msg
from nonebot.matcher import Matcher

test = on_command("测试")


@test.handle()
async def _(event: Danmu_msg, matcher: Matcher):
    # event
    await matcher.finish("收到")
