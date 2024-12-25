#!/usr/bin/python3

import asyncio
import websockets
import argparse

def checkArguments():
	"""Check program arguments and return program parameters."""
	# Parse options.
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--ip', default='localhost',
						help='websockets server host / ip')
	parser.add_argument('-p', '--port', default=12345,
						help='websockets server port')
	parser.add_argument('-v', '--verbose', action='store_true',
						help='verbose mode')
	return parser.parse_args()


async def clientHandler(websocket, path):
	"""Client Handler."""
	clients.add(websocket)

	# Wait message until client close connection.
	if args.verbose:
		print(str(websocket) + ' open connection')
		await websocket.send("test")
	while True:
		try:
			message = await websocket.recv()
			if args.verbose:
				print(str(websocket) + 'Message received: \"' + message +
					  '\" (' + str(websocket) + ')')
			for client in clients:
				await client.send(message)

		# Connection closed.
		except websockets.ConnectionClosed:
			if args.verbose:
				clients.remove(websocket)
				print(str(websocket) + ' close connection')
				break


# Entry point of the program.
clients = set()
args = checkArguments()
server = websockets.serve(clientHandler, args.ip, args.port)
print('Websockets server launch: ' + args.ip + ':' + str(args.port))
asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
