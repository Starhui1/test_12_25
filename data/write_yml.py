import yaml

data = {"n1":{"n2":{"n4":4},"n3":3}}
with open("./ww.yml","a",encoding="utf-8") as f:
    yaml.safe_dump(data,f,encoding="utf-8",allow_unicode=True)
    