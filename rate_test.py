import requests as re

for i in range(10):
    re.get("http://127.0.0.1:5001/api/books")

# for i in range(1, 11):
#     params = {"author": f"Peter{i}"}
#     data_ = re.put(f"http://127.0.0.1:5001/api/books/{i}", data=params)

# print(data_)
