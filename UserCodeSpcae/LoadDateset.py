# _*_ coding: utf-8 _*_
# Python Version 3.9.1
"""
@Author   : Daniel.Wang
@Data     :  2:14 AM
@FileName : LoadDateset.py
@E-mail   : daomiao.wang@live.com
@Site     : Dept. of Electronic Engineering, Fudan University
@Blog     : wangdaomiao.me
desc:
"""

from sklearn import datasets

# download digits dataset
digits = datasets.load_digits()

# creat feature matrix
features_matrix = digits.data

# creat target vector
target_vector = digits.target

print(features_matrix[0])


