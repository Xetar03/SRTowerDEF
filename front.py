#!/bin/python3

import asyncio
import websockets

async def handler(websocket):
	while True:
		message = await websocket.recv()
		print(message)

async def main():
	url = "ws://192.168.1.161:12345"
	async with websockets.connect(url) as ws:
		await handler(ws)
		await asyncio.Future()
		await ws.send(input("inp: "))

asyncio.run(main())
