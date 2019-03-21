import numpy as np
import pandas as pd
from pymongo import MongoClient
import matplotlib as plt

#
# client = MongoClient("localhost", 27017)
# db = client["movies"]
# collection = db["douban"]
#
# data_list = pd.DataFrame(data=list(collection.find()))
# del data_list["_id"]
#
# # 改变列的顺序
# cols = list(data_list)
# cols.insert(0,cols.pop(cols.index('title')))
# cols.insert(1,cols.pop(cols.index("rate")))
# data = data_list.loc[:, cols]
#
# # 对列名进行重命名
# data_array = data.rename(columns={"title":"电影", "rate":"评分", "country":"地区"})
#
# print(data_array)
# from typing import Optional
#
#
# class TreeNode:
#     def __init__(self, value: int):
#         self.val = value
#         self.left = None
#         self.right = None
#
#
# class BinarySearchTree:
#     def __init__(self):
#         self._root = None
#
#     def find(self, value: int) -> Optional[TreeNode]:
#         node = self._root
#         while node and node.val != value:
#             node = node.left if node.val > value else node.right
#         return node
#
#     def insert(self, value: int):
#         if not self._root:
#             self._root = TreeNode(value)
#             return
#         parent = None
#         node = self._root
#         while node:
#             parent = node
#             node = node.left if node.val > value else node.right
#         new_node = TreeNode(value)
#         if parent.val > value:
#             parent.left = new_node
#         else:
#             parent.right = new_node
#
#     def delete(self, value: int):
#         node = self._root
#         parent = None
#         while node and node.val != value:
#             parent = node
#             node = node.left if node.val > value else node.right
#         if not node: return
#
#         # 要删除的节点有两个子节点
#         if node.left and node.right:
#             successor = node.right
#             successor_parent = node
#             while successor.left:
#                 successor_parent = successor
#                 successor = successor.left
#             node.val = successor.val
#             parent, node = successor_parent, successor
#
#         # 删除节点是叶子节点或者仅有一个子节点
#         child = node.left if node.left else node.right
#         if not parent:
#             self._root = child
#         elif parent.left == node:
#             parent.left = child
#         else:
#             parent.right = child
counts = pd.value_counts()
