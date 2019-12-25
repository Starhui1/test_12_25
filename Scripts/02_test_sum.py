import pytest, yaml, os, sys

sys.path.append(os.getcwd())

from Base.getData import GetData

"""定义方法"""


def get_sum_data():
    # 定义存储数据列表
    sum_list = []
    # 读取sum.yml数据
    data = GetData().get_yml_data("sum.yml")
    for i in data.values():
        # 追加数据到列表
        sum_list.append(tuple(i.values()))
    return sum_list


# print(get_sum_data())

"""
data={
    'test_sum1': {'a': 1, 'b': 2, 'c': 3}, 
    'test_sum2': {'a': 2, 'b': 3, 'c': 5}, 
    'test_sum3': {'a': 3, 'b': 4, 'c': 5}}

0.定义空列表 sum_list = []
1. 取data.values()   -> data_list =[{'a': 1, 'b': 2, 'c': 3},{'a': 2, 'b': 3, 'c': 5},{'a': 3, 'b': 4, 'c': 5}]
2. for i in data_list:
     i.values() -> [1,2,3] / [2,3,5] / [3,4,5]
    # 转换类型
    tuple(i.values()) ->(1,2,3) / (2,3,5) / (3,4,5)
    # 追加数据到列表
    sum_list.append(tuple(i.values()))
3.返回 sum_list
"""


class TestSum:
    @pytest.mark.parametrize("a,b,c", get_sum_data())
    def test_sum(self, a, b, c):
        """
        判断两个数之和 a+b==c
        :param a:
        :param b:
        :param c:
        :return:
        """
        print("{}+{}={}".format(a, b, c))

        assert a + b == c
