import jieba
from nerkit.StanzaApi import StanzaWrapper

sw=StanzaWrapper()

def get_opinion(text,user_dictionary_path="",opinion_words='',lang='zh'):
    if user_dictionary_path!="":
        jieba.load_userdict(user_dictionary_path)
    # opinion_words=['表示','认为','说','介绍','提出','透露','指出','强调','：']
    if len(text)<30:
        return []
    list_sentence=sw.tokenize_sentence(text,lang=lang)
    list_result=[]
    list_seg=[]
    list_ner=[]
    for sentence in list_sentence:
        # print(sentence)
        if len(sentence)<30:
            continue
        sentence=sentence.strip()
        sub_sentences=sentence.split("\n")
        for sub_sentence in sub_sentences:
            sub_sentence=sub_sentence.strip()
            if len(sub_sentence)<=20:
                continue
            ners=sw.ner_chinese(sub_sentence)
            words=jieba.cut(sub_sentence,cut_all=False)
            found_opinion=False
            list_word=[]
            for w in words:
                list_word.append(w)
                if w in opinion_words:
                    found_opinion=True
            found_person=False
            for item in ners:
                if item['type']=='PERSON':
                    found_person=True
                    break
            if found_person and found_opinion and len(list_word)>20:
                list_result.append(sub_sentence)
                # print(sub_sentence)
                # print(' '.join(list_word))
                list_seg.append(list_word)
                list_ner.append(ners)
                # print()
    return list_result,list_seg,list_ner