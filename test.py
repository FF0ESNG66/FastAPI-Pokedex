import asyncio


async def fetch_data():
    print('Star fetching...')
    await asyncio.sleep(2)
    print('Fetching is done!')
    return ({'data': 1})

async def print_numbers():
    for number in range(10):
        print(number)
        await asyncio.sleep(0.25)


async def main():
      task_1 = asyncio.create_task(fetch_data())
      task_2 = asyncio.create_task(print_numbers())

      value = await task_1
      print(value)
      await task_2

    


asyncio.run(main())




# Im just testing async stuff, you can ignore this