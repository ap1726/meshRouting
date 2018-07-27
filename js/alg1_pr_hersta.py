# -*- coding:UTF-8 -*-
from browser import document
from browser.html import *
from collections import OrderedDict
from random import random
import math
import cmath
import copy

###################################################################
def startD():
    #init Start
    #init оптимальные пути м/у источник - адресат i-j
    document['resultArea'].html=""
    document['resultArea']<=H4("Результат")+BR()
    dlinaSoobsheniya=int(document["dlinaSoobsheniya"].value)
    propusknayaSposobnost=int(document["propusknayaSposobnost"].value)
    vhodniePotoki=int(document["vhodniePotoki"].value)
    H=float(document["kHersta"].value)
        #1/miu[byte] dlina paketa
    miu=1/dlinaSoobsheniya
    buf={}
    G={}
    d={}
    gamma={}
    count=int(document["count"].value)
    print('Количество узлов', count)
    print('Длина сообщения [кб]', dlinaSoobsheniya)
    print('Максимальная пропускная способность [кб]', propusknayaSposobnost)
    print('Максимальный трафик от источника до адресата [сообщений/сек]', vhodniePotoki)
    print('Коэффициент Хёрста', H)
    print('Средня длина пакета [кб]', miu)
    document['resultArea']<=P('Количество узлов: '+str(count))
    document['resultArea']<=P('Длина сообщения [кб]: '+str(dlinaSoobsheniya))
    document['resultArea']<=P('Максимальная пропускная способность [кб]: '+str(propusknayaSposobnost))
    document['resultArea']<=P('Максимальный трафик от источника до адресата [сообщений/сек]: '+str(vhodniePotoki))
    document['resultArea']<=P('Коэффициент Хёрста: '+str(H))
    document['resultArea']<=P('Средня длина пакета [кб]: '+str(miu))
    for ii in range(0,count):
        buf={}
        for jj in range(0,count):
            if document["input"+str(ii)+"_"+str(jj)].value=="Infinity": 
                buf.pop(jj+1)
                continue
            buf[jj+1]=int(document["input"+str(ii)+"_"+str(jj)].value)
            # print(document["input"+str(ii)+"_"+str(jj)].value)
        G[ii+1]=buf
    # gamma={
    # 1: {2: 50, 4: 60}, 
    # 2: {4: 40}, 
    # 3: {1: 30},
    # 4: {2: 20, 3: 10}
    # }#matrica vhodnih potokov
    for ii in range(0,count):
        buf={}
        for jj in range(0,count):
            if document["inputMatrix"+str(ii)+"_"+str(jj)].value=="Infinity": 
                buf.pop(jj+1)
                continue
            buf[jj+1]=int(document["inputMatrix"+str(ii)+"_"+str(jj)].value)
        gamma[ii+1]=buf
    print('\nПоток [сообщения/сек]')
    document['resultArea']<=P('\nПоток [сообщения/сек]')
    for i in gamma:
        print(i, ':', gamma[i])
        document['resultArea']<=(str(i)+' : '+str(gamma[i]))+BR()
    document['resultArea']<=BR() 
    N=len(G) #uzli 
    #N количество элементов в словаре (gamma) 
    #для сообщений, возникающих в узле i и предназначенных узлу j; обозначим:
    gammaObsh=0
    for k in gamma:
        for l in gamma[k]:
            gammaObsh+=gamma[k][l]
    print('\nПолный внешний трафик:',gammaObsh, '[сообщений/сек]\n')
    document['resultArea']<=P('Полный внешний трафик '+str(gammaObsh))
    """ 
    каждая линия связи из одного дуплексного канала связи с попускной
    способностью d[k][l] байт в секунду, k,l линия связи м/у узлами k-l
    если линии связи нет то d[k][l]=0 
    """
    d = G.copy()
    print('Граф пропускная способность')
    document['resultArea']<=('Граф пропускная способность:')+BR()
    for i in G:
        print(i, ':', G[i])
        document['resultArea']<=(str(i)+' : '+str(G[i]))+BR()
    document['resultArea']<=HR()
    print()
    #init End
    ##############################################################################
    def dijkstra(v, p, t, b, e, inMatrix):
        # print('\n  Обходим всех соседей текущей вершины')
        for x in inMatrix[v]: #для каждого соседа (х) текущей вершины (v)
            xm = p[v] + inMatrix[v][x] #новая метка соседа (xm) =
                                #метка текущей вершины (p[v]) +
                                #значение ребра vx (G[v][x])                   
            if not x in p: #если соседа (x) нет в словаре (p)
                p[x] = xm #записываем новую метку (xm) в словарь с ключем (x)
                b[x] = v  #как только метка пересчитывается, запоминаем 
                          #(следующая вершина: предыдущая вершина) в словаре (b)
            elif not x in t: #иначе если (x) не в (t)
                if p[x] > xm: #если старая метка соседа больше новой метки
                    p[x] = xm #новую метку записываем на место старой
                    b[x] = v #как только метка пересчитывается, запоминаем 
                             #(следующая вершина: предыдущая вершина) в словаре (b)    
            # print('текущей вершины v =', v, ' сосед x =', x, 'c меткой xm =', xm)
        # print('p =', p)
        # print('\n  Добавляем текущую вершину в список посещенных')
        t.append(v)            
        # print('t =', t) 
        if N <= len(t): # Условие выхода из функции
            print('Вершины и их метки =', p)
            print('Словарь для отслеживания пути =', b) 
            global s 
            s = [] #кратчайший путь
            s.insert(0, e) #вставляем (е) в список (s) по индексу (0)
            
            while True:
                if b[e] == -1: #значение ключа (-1) имеет начальная вершина
                               #вот её и ищем в словаре (b)
                    print('Кратчайший путь от начальной до конечной вершины =', s, '\n')
                    document['resultArea']<=('Вершины и их метки ='+str(p))+BR()
                    document['resultArea']<=('Словарь для отслеживания пути ='+str(b))+BR()
                    document['resultArea']<=('Кратчайший путь от начальной до конечной вершины ='+str(s))+BR()
                    document['resultArea']<=BR() 
                    break #выходим из цикла
                e = b[e] #теперь последней вершиной будет предыдущая
                s.insert(0, e) #вставляем (е) в список (s) по индексу (0)
            return s         
        # print('\n  Находим вершину с минимальной меткой за исключением тех, что уже в t')
        for d in p: #вершина (d) с минимальной меткой из словаря (p)
            if d not in t:
                dm = p[d] #метка вершины (d)
                break #пусть это будет первая вершина из словаря (p)
        
        for y in p: #для каждой вершины (y) из словаря (p)
            if p[y] < dm and not y in t: #если метка вершины (y) <
                                         #метки вершины (d) & (y) нет в (t)
                dm = p[y] #метку вершины (y) записываем в (dm)
                d = y #вершину (y) записываем в (d)
                # print('Вершина y =', y, 'с меткой dm =', dm)
        # print('Вершина d =', d, 'имеет минимальную метку dm =', dm, \
              # '\nтеперь текущей вершиной v будет вершина d')
        v = d #теперь текущей вершиной v будет вершина d
        # print('\n  Рекурсивно вызываем функцию Дейкстры с параметрами v, p, t, b, e')
        dijkstra(v, p, t, b, e, inMatrix)
    ##############################################################################
    def pMethod():
        print('######################## НАЧАЛО  ##################')
        #init
        fkl=0
        fklMatrica={}
        fklMatricaNew={}
        fklIJ={}
        Zij={}

        wkl=0
        wklMatrica={}
        fkl2=0
        fklMatrica2={}
        fklMatricaNew2={}
        fklIJ2={}
        Zij2={}
        T1=0
        T2=0
        #step1.1
        sigma1={}
        sigma2={}
        ii=1
        for k in gamma:
            for l in gamma[k]:
                buf2=[]
                buf2=sigma1.keys()
                if str(l)+"-"+str(k) in sigma1:
                    continue
                else:
                    sigma1[str(k)+"-"+str(l)] = gamma[k][l]
                    sigma2[ii]=k
                    sigma2[ii+1]=l
                ii=ii+2

        #step1.2
        sigma1=OrderedDict(sorted(sigma1.items(), key=lambda t: t[1], reverse=True))
        print('Пары сигма1 c трафиком в сообщ/сек:\n',sigma1, '\nsigma2=',sigma2,'\n')
        #step2.1 a
        dijkstraResult={}
        pathNumber=0
        ii=1
        for k in range(1,int(len(sigma2)/2)+1):
            t = [] #список посещённых вершин
            p = {} #словарь {открытая вершина : её метка}
            b = {} #словарь для отслеживания короткого пути
            v = sigma2[ii] #текущая вершина
            e = sigma2[ii+1] #конечная вершина
            ii=ii+2

            p[v] = 0
            b[v] = -1
            print('Маршрут №', k, ':')
            document['resultArea']<=P('Маршрут № '+str(k)+':')
            dijkstra(v, p, t, b, e, G)  #вызываем функцию Дейкстры
            buf1=s.copy()
            dijkstraResult[k]=buf1

        for kl in dijkstraResult:
            buf1={}
            i=1
            for ij in dijkstraResult[kl]:
                buf1[i]=ij
                i=i+1
            dijkstraResult[kl]=buf1

        print('Результат работы алгоритма Дейкстры:')
        for i in dijkstraResult:
            print('Маршрут потока №',i,':', dijkstraResult[i])
        print('dijkstraResult=',dijkstraResult, '\n')
        #step2.1 b
        for kl in dijkstraResult:
            fkl=0
            buf1={}
            for ij in range(1,len(dijkstraResult[kl])):
                fkl=fkl+gamma[dijkstraResult[kl][1]][dijkstraResult[kl][len(dijkstraResult[kl])]]/miu
                buf1[str(dijkstraResult[kl][ij])+'-'+str(dijkstraResult[kl][ij+1])]=fkl
                if fkl>=d[dijkstraResult[kl][ij]][dijkstraResult[kl][ij+1]]:
                    print(fkl, '>=', d[dijkstraResult[kl][ij]][dijkstraResult[kl][il+1]], 'Допустимого решения не существует!')
                    document['resultArea']<=B(str(fkl)+'>='+str(d[dijkstraResult[kl][ij]][dijkstraResult[kl][ij+1]])+'Допустимого решения не существует!')
                    continue
            fklMatrica[kl]=buf1
            fklIJ[kl]=fkl
            print('Величина потока в линии', kl, ':', fkl, 'кбайт/сек')
            document['resultArea']<=P('Величина потока в линии '+str(kl)+' : '+str(fkl) + ' кбайт/сек')

        print('fklIJ=',fklIJ)
        print('fklMatrica=', fklMatrica)
        print()
        #step2.2
        for ij in fklIJ:
            Zij[ij]=dlinaSoobsheniya/fklIJ[ij]
            print('Задержка между парой узлов в линии', ij, ':', Zij[ij], 'ms')
        print()
        #step3.1
        sigma3=OrderedDict(sorted(Zij.items(), key=lambda t: t[1], reverse=True))
        for i in sigma3:
            print('Задержка на маршруте №',i,':', sigma3[i], 'ms')
            document['resultArea']<=P('Задержка на маршруте № '+ str(i)+' : '+str(sigma3[i])+' ms')
        print()
        document['resultArea']<=HR()
        # step3.2. a 1 удалять не будем
        # step3.2. a 2 просто добавим везде кроме текущего

        def changeFkl(line,start,end):
            fklMatricaNew={}
            for kl in fklMatrica:
                buf1={}
                for ij in fklMatrica[kl]:
                    buf1[ij]=fklMatrica[kl][ij]
                    if kl!=line:
                        buf1[ij]=buf1[ij]+fklIJ[line]
                fklMatricaNew[kl]=buf1
            return fklMatricaNew   
        def getWkl(pathNumber,matrica):
            wkl={}
            wkl=copy.deepcopy(d)
            for kl in wkl:
                for ij in wkl[kl]:
                    try:
                        buff=str(kl)+'-'+str(ij)
                        for iii in matrica:
                            if matrica[iii].get(buff)!=None:
                                minus=matrica[iii].get(buff)
                                break
                            else:
                                minus=0
                    except Exception as e:
                        wkl[kl][ij]=999999
                        print(e)
                    else:
                        if wkl[kl][ij]>minus:
                            wkl[kl][ij]=(1/miu)*1/(wkl[kl][ij]-minus)
                        else:
                            wkl[kl][ij]=99999999
            for kl in d:
                buf1={}
                for ij in d[kl]:
                    buf1[ij]=wkl[kl][ij]
                wkl[kl]=buf1
            return wkl
        dijkstraResult2={}
        for ij in sigma3:     #step3.2
            fklMatricaNew=changeFkl(ij,sigma2[ij*2-1],sigma2[ij*2])
            print('Измененная матрица потоков (',ij,') \nfklMatricaNew=') 
            for i in fklMatricaNew: 
                print(i, ':', fklMatricaNew[i])
        #step3.2. a 3
            wklMatrica=getWkl(ij,fklMatricaNew)
            print('Веса линий связи (',ij,') \nWkl=')
            document['resultArea']<=('Веса линий связи ('+str(ij)+')'+BR()+' Wkl=')+BR()
            for i in wklMatrica: 
                print(i, ':', wklMatrica[i])
                document['resultArea']<=(str(i)+' : '+str(wklMatrica[i])+BR())
            print()
            document['resultArea']<=BR() 

        #step3.2 a 4
            t = [] #список посещённых вершин
            p = {} #словарь {открытая вершина : её метка}
            b = {} #словарь для отслеживания короткого пути
            v = sigma2[ij*2-1] #текущая вершина
            e = sigma2[ij*2] #конечная вершина

            p[v] = 0
            b[v] = -1
            print('Маршрут №', ij, ':')
            document['resultArea']<=('Оптимальный маршрут потока № '+str(ij)+' :')+BR()
            dijkstra(v, p, t, b, e, wklMatrica)  #вызываем функцию Дейкстры
            buf1=s.copy()
            dijkstraResult2[ij]=buf1
        for kl in dijkstraResult2:
            buf1={}
            i=1
            for ij in dijkstraResult2[kl]:
                buf1[i]=ij
                i=i+1
            dijkstraResult2[kl]=buf1 

        print('Результат работы алгоритма Дейкстры 2:')
        for i in dijkstraResult2:
            print('Оптимальный маршрут потока №',i,':', dijkstraResult2[i])
        print('dijkstraResult2=',dijkstraResult2, '\n')
        #step3.2 b
        for kl in dijkstraResult2:
            fkl2=0
            buf1={}
            for ij in range(1,len(dijkstraResult2[kl])):
                fkl2=fkl2+gamma[dijkstraResult2[kl][1]][dijkstraResult2[kl][len(dijkstraResult2[kl])]]/miu
                buf1[str(dijkstraResult2[kl][ij])+'-'+str(dijkstraResult2[kl][ij+1])]=fkl2
                if fkl2>=d[dijkstraResult2[kl][ij]][dijkstraResult2[kl][ij+1]]:
                    print(fkl2, '>=', d[dijkstraResult2[kl][ij]][dijkstraResult2[kl][ij+1]], 'Допустимого решения не существует!')
                    document['resultArea']<=B(str(fkl2)+'>='+str(d[dijkstraResult2[kl][ij]][dijkstraResult2[kl][ij+1]])+'Допустимого решения не существует!')
                    continue
            fklMatrica2[kl]=buf1
            fklIJ2[kl]=fkl2
            print('Величина потока в линии', kl, ':', fkl2, 'кбайт/сек')
            document['resultArea']<=P('Величина потока в линии '+ str(kl)+' : '+str(fkl2)+' кбайт/сек')
        print('fklIJ2=',fklIJ2)
        print('fklMatrica2=', fklMatrica2)
        print()
        #step3.3 
        buf1={}
        buf1=copy.deepcopy(d)
        summ=0
        summ2=0

        for kl in buf1:
            for ij in buf1[kl]:
                try:
                    buff=str(kl)+'-'+str(ij)
                    for iii in fklMatrica2:
                        if fklMatrica2[iii].get(buff)!=None:
                            minus=fklMatrica2[iii].get(buff)
                            break
                        else:
                            minus=0
                    summ=summ+(minus/(buf1[kl][ij]-minus))
                    T1=1/gammaObsh*summ
                except Exception as e:
                    print(e)
                else:
                    next

        for kl in buf1:
            for ij in buf1[kl]:
                try:
                    buff=str(kl)+'-'+str(ij)
                    for iii in fklMatrica2:
                        if fklMatrica2[iii].get(buff)!=None:
                            minus2=fklMatrica2[iii].get(buff)
                            break
                        else:
                            minus2=0
                    a=minus2/buf1[kl][ij]
                    b=(H-0.5)/(1-H)
                    c=1-minus2/buf1[kl][ij]
                    dd=H/(1-H)
                    summ2=summ2+(math.pow(a,b)/math.pow(c,dd))
                    T2=summ2/gammaObsh
                except Exception as e:
                    print(e)
                else:
                    next
        print('Средняя задержка сообщения в сети T1=')
        print(T1, 'ms\n')
        document['resultArea']<=P('Средняя задержка сообщения в сети T1='+str(T1)+'ms<br>')
        print('C коэффициентом Херста T2=')
        print(T2, 'ms\n')
        document['resultArea']<=P('C коэффициентом Херста='+str(H)+' T2='+str(T2)+'ms<br>')
        print('################## КОНЕЦ  ########################')
        return(T1, d, gamma, sigma2)
    ##############################################################################
    try:
        pMethod()
    except Exception as e:
        raise
    else:
        pass
    finally:
        pass
document["button5"].bind("click", startD)