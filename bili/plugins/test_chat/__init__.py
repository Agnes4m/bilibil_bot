from nonebot import get_bot, get_driver, on_command, require

require("nonebot_plugin_apscheduler")
# from nonebot.adapters import Event
# from nonebot.adapters.bilibili.bot import Bot
# from nonebot.matcher import Matcher
from nonebot_plugin_apscheduler import scheduler  # noqa: E402, I001


driver = get_driver()
test = on_command("测试")


async def auto_cup():
    await get_bot().send("你好")


scheduler.add_job(auto_cup, "cron", hour=0, minute=1, id="auto_cup")


@driver.on_bot_disconnect
async def _():
    scheduler.remove_job("auto_cup")
