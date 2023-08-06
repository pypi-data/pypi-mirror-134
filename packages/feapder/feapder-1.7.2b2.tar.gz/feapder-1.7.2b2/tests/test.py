# from feapder import Request
# from feapder.buffer.request_buffer import RequestBuffer
#
# request_buffer = RequestBuffer(redis_key="xxxx")
#
# # 构造任务
# request = Request("url")
# # 添加任务
# request_buffer.put_request(request)
# # 推送
# request_buffer.flush()
#
def a():
    print(1)

import threading
threading.Thread(target=a).start()