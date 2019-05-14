1. employee.modulepy.py 是用到了装饰器（@property）的实现方式
2. employee.modulepy2.py 是没用到装饰器的实现方式
3. 主要改动：
    * promote(), demote() 加入判断： 如果员工已经离职（isHired = False） 则报错
    * 加入 fire(), hire(), isHired(), getIsHired(),setIsHired()
4. 不合理之处，题目说通过 setter 设置员工的状态，但这不合理，如果通过setIsHired() 函数改变员工在职状态，那和hire(),fire() 的作用冲突了
5. 第17行，我在employee初始化的时候设置 isHired状态为 True， 这可能合理，也可能不合理，