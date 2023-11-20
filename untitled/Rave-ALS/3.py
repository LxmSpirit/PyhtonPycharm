import jieba
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from pandas import DataFrame
import openpyxl as op

# 训练集
new_reply = pd.DataFrame(None, columns=["reply", "answer"])
reply = pd.read_excel("sum.xlsx").astype(str)

print("训练集读取成功！")
# 新数据
reply1 = pd.read_csv("result297.csv").astype(str)
new_reply1 = pd.DataFrame(None, columns=["reply", "answer"])
print("数据集读取成功")
# stopwords的引用

with open("stopwords.txt", "r", encoding="utf-8") as f:
    stops = f.readlines()
stopwords = [x.strip() for x in stops]

# 利用jieba对文本进行分段

new_reply["reply"] = reply.回答.apply(lambda s: " ".join(jieba.cut(s)))
new_reply["answer"] = reply["answer（人工阅读）"]
new_reply["reply"] = new_reply.reply.apply(lambda s: s if str(s) != "nan" else np.nan)
df = new_reply["reply"]
df = df.to_frame(name="reply")
df_isnull_remark = df[df["reply"].isnull()]
new_reply.dropna(subset=["reply"], inplace=True)
cut_list = new_reply["reply"].apply(lambda s: s.split(" "))
result = cut_list.apply(lambda s: [x for x in s if x not in stopwords])  # result类型为series

new_reply1["reply"] = reply1.回答.apply(lambda s: " ".join(jieba.cut(s)))

# new_reply1["answer"] = reply1["answer（人工）"]
new_reply1["reply"] = new_reply1.reply.apply(lambda s: s if str(s) != "nan" else np.nan)
cf = new_reply1["reply"]
cf = cf.to_frame(name="reply")
cf_isnull_remark = cf[cf["reply"].isnull()]
new_reply1.dropna(subset=["reply"], inplace=True)
cut_list1 = new_reply1["reply"].apply(lambda s: s.split(" "))
result1 = cut_list1.apply(lambda s: [x for x in s if x not in stopwords])  # result1类型为series

# x_train,x_test,y_train,y_test = train_test_split(result,new_reply["answer"],test_size = 0.25,random_state = 3)

x_train = result
y_train = new_reply["answer"]

# test_index = x_test.index
test_index = result1.index

x_train = x_train.reset_index(drop=True)
# print(type(x_test))       #x_test类型为series


words = []
for i in range(len(x_train)):
    words.append(' '.join(x_train[i]))

result1 = result1.reset_index(drop=True)

test_words = []

for i in range(len(result1)):
    test_words.append(' '.join(result1[i]))


cv = CountVectorizer(ngram_range=(1, 2))
cv.fit(words)
classifer = MultinomialNB()
classifer.fit(cv.transform(words), y_train)
# score = classifer.score(cv.transform(test_words),test)
a = classifer.predict_proba(cv.transform(test_words))


print("ok")
