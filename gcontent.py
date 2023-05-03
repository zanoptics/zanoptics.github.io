#存储规则:除了readme,边栏等文件,同一目录下要么只有文件file要么只有目录dir
import os
def dirend(relp):
    #找到不包含dir的dir,用fdlist存路径,包含dir的dir路径用ddlist存
    global fdlist
    global ddlist
    #生成器返回(路径,[dirname_list],[filename_list])
    temp=next(os.walk(relp))
    #编写入口侧边栏
    plen=len(temp[0].split('\\'))
    if plen==2:
        with open('_sidebar.md','a',encoding='utf-8') as f1:
            f1.write(f'- [**{os.path.basename(temp[0])}**](/'+temp[0].replace('\\','/')+'/README.md)\n')
    elif plen>2:
        with open('_sidebar.md','a',encoding='utf-8') as f1:
            f1.write((plen-2)*2*' '+f'- [{os.path.basename(temp[0])}](/'+temp[0].replace('\\','/')+'/README.md)\n')
    else:
        with open('_sidebar.md','w',encoding='utf-8') as f1:
            f1.write('- [**首页**](/README.md)\n')
    #判断有无dir
    if temp[1] and temp[1] !=['figure']:
        #若有,将路径按特定格式加入ddlist
        ddlist.append('/'+temp[0].replace('\\','/'))
        #编写dir文件夹的侧边栏
        sp=temp[0]+'\\_sidebar.md'
        with open(sp,'w',encoding='utf-8') as sf:
            sf.write(f'- [**首页**](/README.md)\n- [**{os.path.basename(temp[0])}**](/'+temp[0].replace('\\','/')+'/README.md)\n')
            for i in temp[1]:
                if(i not in ['figure']):
                    sf.write(f'- [{i}](/'+temp[0].replace('\\','/')+f'/{i}/README.md)\n')
        #若有,对每个dir递归
        for i in temp[1]:
            if(i not in ['figure']):
                dirend(relp+f'\\{i}')
    else:
        #若除了figure无,将路径按特定格式加入fdlist
        fdlist.append('/'+temp[0].replace('\\','/'))
        # 创建存图片的文件夹figure
        figp=temp[0]+'\\figure'
        if not os.path.exists(figp):
            os.mkdir(figp)
        #编写file文件夹侧边栏
        sp=temp[0]+'\\_sidebar.md'
        with open(sp,'w',encoding='utf-8') as sf:
            sf.write(f'- [**首页**](/README.md)\n')
            sf.write(f'- [**{os.path.basename(temp[0])}**](/'+temp[0].replace('\\','/')+'/README.md)\n')
            for i in temp[2]:
                if(i not in ['README.md','_navbar.md','_sidebar.md']):
                    sf.write(f'- [{i[0:-3]}](/'+temp[0].replace('\\','/')+f'/{i})\n')
    #子目录README文件
    rp=temp[0]+'\\README.md'
    if not os.path.exists(rp):
        with open(rp,'a',encoding='utf-8') as rf:
            rf.write(f'# {os.path.basename(temp[0])}\n## 简介\n## 注意事项')
    #复制导航栏文件(它会自动发送get请求,加载navbar,最好复制过来)
    np=temp[0]+'\\_navbar.md'
    if not os.path.exists(np):
        with open(np,'a',encoding='utf-8') as nf:
            with open('_navbar.md','r',encoding='utf-8') as copy:
                nf.write(copy.read())
if __name__ == '__main__':
    fdlist=[]
    ddlist=[]
    dirend('doc')
    print('不包含dir的dir的路径表 fdlist:\n',fdlist)
    print('包含dir的dir的路径表 ddlist:\n',ddlist)
    with open('fdlist.txt','w',encoding='utf-8') as f:
        f.write(str(fdlist))
    with open('ddlist.txt','w',encoding='utf-8') as f:
        f.write(str(ddlist))
    os.system('pause')