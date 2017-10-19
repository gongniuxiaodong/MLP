# from gensim.models import word2vec
# import logging
# # 主程序
# logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO)
# # sentences = word2vec.Text8Corpus(u'e:/Downloads/testch.txt')  # 加载语料
# # model = word2vec.Word2Vec(sentences, size=200)  # 训练skip-gram模型，默认window=5
# model=word2vec.Word2Vec.load('e:/Downloads/y')
# print(model)
# # 计算两个词的相似度/相关程度
# try:
#     y1 = model.similarity(u"coffee", u"soap")
# except KeyError:
#     y1 = 0
# print(u"【国家】和【国务院】的相似度为：", y1)
# print("-----\n")
# #
# # 计算某个词的相关词列表
# y2 = model.most_similar(u"控烟", topn=20)  # 20个最相关的
# print(u"和【控烟】最相关的词有：\n")
#
# for item in y2:
#     print(item[0],item[1])
# print("-----\n")
# # 寻找对应关系
# print(u"书-不错，质量-")
# y3 = model.most_similar([u'质量', u'不错'], [u'书'], topn=3)
# for item in y3:
#     print(item[0], item[1])
# print("----\n")
# # 寻找不合群的词
# y4 = model.doesnt_match(u"书 书籍 教材 很".split())
# print(u"不合群的词：", y4)
# print("-----\n")
# # 保存模型，以便重用
# model.save(u"书评.model")
# # 对应的加载方式
# # model_2 =word2vec.Word2Vec.load("text8.model")
#
# # 以一种c语言可以解析的形式存储词向量
# # model.save_word2vec_format(u"书评.model.bin", binary=True)
# # 对应的加载方式
# # model_3 =word2v

# from  keras.preprocessing import text
# from  keras.preprocessing.text import Tokenizer
# text1 = "are you ok? if you're ok, try good"
# b = text.text_to_word_sequence(text1,filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n',lower=True,split=" ")
# print(b)
# c = text.one_hot(text1,200,filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n',lower=True,split=" ")
# print(c)
# tokenizer = Tokenizer(num_words=100,filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n',lower=True,split=" ",char_level=False)
# tokenizer.fit_on_texts(text1)
# print(tokenizer.word_counts)
# print(tokenizer.word_index)
# print(tokenizer.word_docs)
# print(tokenizer.document_count)
# print(tokenizer.texts_to_matrix(text1))
# print(tokenizer.texts_to_sequences(text1))


print (u'\u8fd0\u52a8\u573a\u4e0a\u6709\u4e00\u4e2a\u53f3\u624b\u62ff\u7740\u7403\u62cd\u7684\u5973\u4eba\u5728\u6253\u7f51\u7403", "\u5bbd\u655e\u7684\u7403\u573a\u4e0a\u6709\u4e00\u4e2a\u53f3\u624b\u62ff\u7740\u7403\u62cd\u7684\u8fd0\u52a8\u5458\u5728\u6253\u7f51\u7403", "\u4e00\u4e2a\u6234\u7740\u5e3d\u5b50\u7684\u5973\u4eba\u5728\u8fd0\u52a8\u573a\u4e0a\u6253\u7f51\u7403", "\u4e00\u4e2a\u53f3\u624b\u62ff\u7740\u7403\u62cd\u7684\u5973\u4eba\u5728\u5e72\u51c0\u7684\u8fd0\u52a8\u573a\u4e0a\u6253\u7f51\u7403", "\u5e73\u5766\u7684\u7403\u573a\u4e0a\u6709\u4e00\u4f4d\u53f3\u624b\u62ff\u7740\u7403\u62cd\u7684\u5973\u58eb\u5728\u6253\u7f51\u7403')
