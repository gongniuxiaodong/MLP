from gensim.models import word2vec as wv
# sentences=open('e:/Downloads/test.txt','r',encoding='utf-8')
sentences=wv.Text8Corpus('e:/Downloads/test.txt')
sentences.max_sentence_length
# model=wv.Word2Vec(sentences)
# y=model.similarity('soap','coffee')
# print(y)
# model.save('e:/Downloads/y.txt')
# new=wv.Word2Vec.load('e:/Downloads/y.txt')
# print(new.most_similar('other'))
# model=wv.Word2Vec(sen,min_count=5,size=50)

# mode=model['computer']
# for e in model.most_similar(u'food'):
#     print(e[0],e[1])