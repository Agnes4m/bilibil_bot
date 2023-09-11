import asyncio
import json

import websockets


async def connect_to_proxy():
    async with websockets.connect("wss://blive.deno.dev") as socket:
        # 进入房间命令
        await socket.send(
            json.dumps(
                {
                    "cmd": "enter",  # 命令名，必填
                    "rid": 5942370,  # 房间号，必填
                    "events": ["DANMU_MSG"],  # 监听这个房间中的事件列表，必填
                },
            ),
        )

        # 退出房间命令
        await socket.send(
            json.dumps(
                {
                    "cmd": "leave",  # 命令名，必填
                    "rid": 123,  # 房间号，必填
                },
            ),
        )

        # 退出所有房间
        await socket.send(
            json.dumps(
                {
                    "cmd": "exit",
                },
            ),
        )

        # 接收进入房间时`events`参数所指定的消息
        async for message in socket:
            print(message)
            data = json.loads(message.data)
            # 接收到的消息，格式为 { rid: 房间号, payload: {} }
            print(data)


# 运行协程
asyncio.run(connect_to_proxy())
