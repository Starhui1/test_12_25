import yaml

with open("./value_sum.yml",encoding="utf-8") as f:
    # 加载yaml文件
    data = yaml.safe_load(f)
    # 打印数据
    print(data)
    # 打印类型
    # print(type(data.get("info")))