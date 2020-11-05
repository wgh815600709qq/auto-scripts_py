import asyncio

result_list = []


async def fun(var):
    return var + 1


def callbackFun(future):
    result_list.append(future.result())


task_list = []

for i in range(1, 5):
    cor = fun(i)
    task = asyncio.ensure_future(cor)
    task.add_done_callback(callbackFun)
    task_list.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task_list))
print(result_list)