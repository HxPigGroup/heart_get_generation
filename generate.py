import os
import sys
import random

yulu = 'yulu.tXt'
vci = 'vci.txt'

if __name__ == '__main__':
    if (os.path.exists(yulu) == 0):
        print('本地找不到yulu.txt文件')
        sys.exit(0)
    if (os.path.exists(vci) == 0):
        print('本地找不到vci.txt文件')
        sys.exit(0)
    yu_s = []
    fr = open(yulu, 'r', encoding='UTF-8')
    for line in fr.readlines():
        curLine = line.strip().split('、')
        if(len(curLine) == 1):
            continue
        s = ''
        for i in range(1, len(curLine)):
            s = s + curLine[i].strip("。")
        yu_s.append(s)

    v_ci = []
    fr = open(vci, 'r', encoding='UTF-8')
    for line in fr.readlines():
        curLine = line.strip().split('、')
        if (len(curLine) == 1):
            continue
        v_ci.append(curLine[0] + '了')

    print("请输入大纲方向(例：两会、团会)：  ")
    da_gang = input()

    tou = ['在这次'+da_gang+'中，让我', '通过这次'+da_gang+'，我', '在'+da_gang+'的领导下，我', '这次'+da_gang+'让我，']

    s_final = tou[random.randint(0, len(tou) - 1)]


    zhen = ['含意', '寓意', '涵义', '含义', '真理', '真义', '道理', '真谛']
    dao = ['真理', '真义', '道理', '真谛']
    for i in range(1):
        v = v_ci[random.randint(0, len(v_ci) - 1)]
        yu = yu_s[random.randint(0, len(yu_s) - 1)]
        shen = "深刻"
        if(random.randint(0, 1) == 1): shen = ""
        nn = zhen[random.randint(0, len(zhen) - 1)]
        #if(i==1): nn = dao[random.randint(0, len(dao) - 1)]
        s_final = s_final + v + '\"' + yu + '\"' + "的" + shen + nn

    qing = ['作为新时代的青年，', '作为新一代青年，', '作为当代青年，']
    s_final = s_final + '。' + qing[random.randint(0, len(qing) - 1)] + '我们应该'
    print('请输入大纲方向------政治向：0    科研向：1    历史向：2    社会服务向：3    团队合作向：4    进去创新向：5   自立自强向：6    随机：7\n')
    i = int(input())
    gang = ['坚持正确的政治方向，做中国化的马克思主义理论的追随者、先进文化和科学精神的传播者、社会主义和谐社会的践行者。',
            '以与时俱进的态度和勇于创新的精神投入到研究领域。',
            '牢记历史教训，为实现人民对美好生活的向往而不懈奋斗。',
            '坚持走群众路线，在密切联系人民群众的过程中实现自己的人生价值。',
            '树立团队合作意识，形成适应社会发展要求的和谐文化心态和实际工作能力。',
            '展示不断进取的风采，通过创新解决前进过程中出现的矛盾和问题。',
            '培养自强自立的社会责任感，在建设和谐社会的大潮中，勇于自任，敢于担当。']
    j = i
    if(i == 7):
        j = random.randint(0, len(gang)-1)
    s_final = s_final + gang[j]
    print("是否需要升华：0（否） 1（是）\n")
    shi_fou = int(input())
    if(shi_fou):
        s_final += "作为向着党的新时代青年，"
        shen_hua = ["血脉在人民，力量在人民。实现好、维护好、发展好最广大人民的根本利益，是我们肩负的重大历史任务。",
                    "把人民的信任与重托，转化为学习贯彻两会精神的具体行动，不断增进人民福祉、不断增加党的活力、不断提升国家实力。",
                    "发出时代“最美的声音”，道睿智谋事之言，献务实管用之策，将为改革发展凝聚强大动力，不断促进党心民意的交融汇聚，推动政治文明取得更大进步，走好复兴之路上的关键一程，让人民的获得感、幸福感和安全感持续增强。",
                    "就要坚持正确的价值取向，树牢正确的价值观，常怀律己之心、常修为官之德，讲原则、讲程序、讲公道，做到心有所畏、言有所戒、行有所止。",
                    "“后浪”萌新唯有汲取革命先烈们的精神力量，砥砺初心、拼搏奋进，才能书写一份无愧于时代、无愧于人民的光彩熠熠的历史答卷。"]
        s_final += shen_hua[random.randint(0, len(shen_hua)-1)]
    print(s_final)
    print('含标点字符字数：%d'%(len(s_final)))

    file_out = './output.txt'
    f = open(file_out, "w")

    f.write(s_final + '\n')
    f.write('含标点字符字数：' + str(len(s_final)))





