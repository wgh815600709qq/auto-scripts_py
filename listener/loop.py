
import sched
import time
# 初始化sched模块的 scheduler 类

# 第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。

schedule = sched.scheduler(time.time, time.sleep)

