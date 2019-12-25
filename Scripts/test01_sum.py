import pytest,os,sys
sys.path.append(os.getcwd())
import yaml
# os.sep可以获取系统路径分隔符,因为window和linux路径分隔符不一样

# def get_yaml():
#     my_list = []
#     with open("./data"+os.sep+"value_sum.yml",encoding="utf-8") as f:
#         data = yaml.safe_load(f)
#         for i in data.values():
#             my_list.append(tuple(i.values()))
from Base.getData import GetData


def get_yaml():
    my_list = []
    data = GetData()
    for i in data.get_yaml_data("value_sum.yml").values():
        my_list.append(tuple(i.values()))
    return my_list

    # return my_list

class TestSum:
    @pytest.mark.parametrize("a,b,c",get_yaml())
    def test_sum(self,a,b,c):
        print(a,b,c)
        assert a+b==c