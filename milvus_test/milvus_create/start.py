import json
from pymilvus import Collection, db, connections
import numpy as np
from zhipuai import ZhipuAI
from pymilvus import MilvusClient

# 替换为您的实际 API 密钥
api_key = "8fb21e517a965b10cf87b7fdadf18a74.UVLbxTJXdL3YLxcT"

# 初始化 ZhipuAI 客户端
client = ZhipuAI(api_key=api_key)
text  = ["你好"]
conn = connections.connect(host="127.0.0.1", port=19530)
db.using_database("sample_db")
coll_name = 'word_vector'
# 加载集合，不加载就不能插入数据
collection = Collection(coll_name)
collection.load()
mids, embedings, counts, descs = [], [], [], []
idx = 1
# 调用嵌入创建 API
response = client.embeddings.create(
    model="embedding-2",  # 替换为您想要使用的模型名称
    input=text  # 传递单个文本
)
# print([response.data[0].embedding])
collection = Collection(coll_name)
# 1. 设置一个Milvus客户端
search_params = {"metric_type": "IP", "params": {"nprobe": 10}}
# 确保集合已经被加载并且不是空的
if not collection.is_empty:
    # 构建查询参数
    res = collection.search(
        anns_field="embeding",
        # 搜索的字段，这里假设有一个文本字段叫做 description
        data=[response.data[0].embedding],
        # 返回 TopK 个最相关的结果
        limit=10,
        param={"metric_type": "IP", "params": {}} # 搜索参数
    )
    
    # 将输出转换为格式化的JSON字符串

print(res)
