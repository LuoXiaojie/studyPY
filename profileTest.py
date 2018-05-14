#coding=utf-8
__metaclass__ = type
import profile, pstats
from my_math import product

if __name__ == '__main__':
    #性能测试文件保留在my_math.profile
    profile.run('product(1,2)', 'my_math.profile')
    p = pstats.Stats('my_math.profile')
    p.print_stats()