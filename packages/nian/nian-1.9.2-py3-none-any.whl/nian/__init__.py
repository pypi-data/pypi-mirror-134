#初慕苏流年
#Q1274210585
#群556766602
import os
import sys
import requests,json,urllib,re,base64
from concurrent.futures import ThreadPoolExecutor
import threading
import time
print('[warning]当前版本均为测试功能！')
def wy(music,s,t):aaaa=json.loads(requests.get("http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s="+music+"&type=1&offset=0&total=true&limit=20").text);aa=[aaaa["result"]["songs"][i]["id"] for i in range(6)];a=int(s);a=["http://music.163.com/song/media/outer/url?id="+str(aa[a])+".mp3",aaaa["result"]["songs"][a]["name"]+"-"+aaaa["result"]["songs"][s]["artists"][0]["name"]] if t==True else "http://music.163.com/song/media/outer/url?id="+str(aa[a])+".mp3";return a
def kg(music,s,t):b=music;a=json.loads(requests.get("http://msearchcdn.kugou.com/api/v3/search/song?showtype=14&highlight=em&pagesize=30&tag_aggr=1&tagtype=%E5%85%A8%E9%83%A8&plat=0&sver=5&keyword={}&correct=1&api_ver=1&version=9108&page=1&area_code=1&tag=1&with_res_tag=1".format(b)).text[23:-21]);aa=[a["data"]["info"][i]["hash"] for i in range(6)];bb=[a["data"]["info"][i]["album_id"] for i in range(6)];c,s=int(s),requests.Session();headers={"Host": "www.kugou.com","Connection": "keep-alive","Cache-Control": "max-age=0","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; PBAT00 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36","dnt": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","Referer": "http://www.kugou.com/yy/index.php?r=play/getdata&hash=f8784ebfbae36b324ec1e3441b6156b4&album_id=1645030&_=","Accept-Encoding": "gzip, deflate","Accept-Language": "zh-CN,en-US;q=0.9","Cookie": "kg_mid=99d022a988b55c42e89a27dfa084fdac; kg_dfid=0Qi8qz2gH29M3dfNNl2aQ6cD; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; KuGooRandom=66531611627702529; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1611627606; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1611636395","X-Requested-With": "mark.via","If-Modified-Since": "","If-None-Natch": ""};a=[json.loads(s.get("http://www.kugou.com/yy/index.php?r=play/getdata&hash="+aa[c]+"&album_id="+bb[c]+"&_",headers=headers,allow_redirects=False).text)["data"]["play_url"],a["data"]["info"][c]["filename"]] if t==True else json.loads(s.get("http://www.kugou.com/yy/index.php?r=play/getdata&hash="+aa[c]+"&album_id="+bb[c]+"&_",headers=headers,allow_redirects=False).text)["data"]["play_url"];return a
#def dy(url):print("测试功能,随时删除");url_string=url;print("解析302地址中......");r = requests.head(url_string, stream=True);print("获取视频ID中......");a="https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids="+r.headers['Location'][38:57];print("获取链接ID中......");b="https://aweme.snssdk.com/aweme/v1/play/?video_id="+json.loads(requests.get(a).text)["item_list"][0]["video"]["vid"]+"&ratio=720p&line=0";return b
#抖音主页 dyzy 新功能！！！

def dyzy(url):
    a=requests.head(url,stream=True)
    b=re.findall('&sec_uid=(.*?)&did',a.headers['location'])
    #https://www.iesdouyin.com/share/user/65619434591?with_sec_did=1&u_code=2b2ajceda7hb&sec_uid=MS4wLjABAAAAkNW8tWhCYYzv2e8G43uI46mnSQH2NKXBGHfnJcpINAg&did=MS4wLjABAAAAGaiKVkT8beqe-wGq4l7N3c1-8t-3vGTHUwJbCetQjng&iid=MS4wLjABAAAAAFFb9CzHLceZZDHZyTlw3uVT2eZi2xz6q-XuGU7QJlqcUF3V0PH9SHWltw0NTrQ6&timestamp=1621932323&utm_source=copy&utm_campaign=client_share&utm_medium=android&share_app_name=douyin
    #主页
    #https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAkNW8tWhCYYzv2e8G43uI46mnSQH2NKXBGHfnJcpINAg&count=21&max_cursor=0&aid=1128&_signature=BfCy5AAAZWEyk7w6JGwabQXwsv&dytk=
    #json
    #CJeumwAAaEE.9KBFoVN2NwiXro这个sigh？
    print("测试功能,随时失效  [Debug mode]")
    #print(b)
    url="https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid="+b[0]+"&count=100&max_cursor=0&aid=1128&_signature=BfCy5AAAZWEyk7w6JGwabQXwsv&dytk="
    headers={"Host": "www.iesdouyin.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; PBAT00 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt": "1","x-requested-with": "mark.via","sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","accept-encoding": "gzip, deflate","accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"}
    a=requests.get(url,headers=headers).text
    b=re.findall('"vid":"(.*?)"',a)
    c=["https://aweme.snssdk.com/aweme/v1/play/?video_id="+i+"&ratio=720p&line=0" for i in b]
    return c
def import_(path):
    dirs = os.listdir(path)
    o=''
    with open('_init_.py','w+') as w:
        for i in dirs:
            o+=f"from {path.replace('/','.')}.{i.split('.')[0]} import *\n"
        w.write(o)
    import _init_

#酷我
def kw(song):
    keyword = requests.utils.quote(song)
    s = requests.session()
    url = 'https://kuwo.cn/'
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'zh-CN,zh;q=0.9','Cache-Control': 'no-cache','Connection': 'keep-alive','Host': 'kuwo.cn','Pragma': 'no-cache','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',}
    s.get(url, headers=headers)
    csrf = s.cookies.get_dict()['kw_token']
    url = f'https://kuwo.cn/api/www/search/searchMusicBykeyWord?key={keyword}&pn=1&rn=30&httpsStatus=1'
    headers = {'csrf': csrf,'Referer': f'https://kuwo.cn/search/list?key={keyword}','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',}
    r = s.get(url, headers=headers).json()
    #print(r)
    for i in r['data']['list']:
        ...#print(i['rid'])
    rid=r['data']['list'][0]['rid']
    #rid = jsonpath.jsonpath(r, '$..rid')[0]
    url = f'http://m.kuwo.cn/newh5app/api/mobile/v2/music/src/{rid}'
    headers={'Host': 'm.kuwo.cn','Connection': 'keep-alive','Cache-Control': 'max-age=0','Upgrade-Insecure-Requests': '1','User-Agentz': 'Mozilla/5.0 (Linux; Android 8.1.0; PBAT00 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-gpc': '1','dnt': '1','save-data': 'on','X-Requested-With': 'mark.via.gp','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',}
    try:
        r = s.get(url, headers=headers).json()
        music_url = r.get("data").get("url")
    except:
        return None
    return music_url
#歌单解析
def listqq(url: str) -> list:
    headers={
    'Host': 'i.y.qq.com',
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; PBAT00 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36',
    }
    a=requests.get(url,headers=headers).text
    l__=re.findall("(?<=\"songlist\":).*?(?=},\"seoData\")",a)[0]
    list_=eval(l__.replace('null', '""'))
    l_=[]
    for i in list_:
        l_.append(i['name'])
    return l_
#多线程，批量获取评论，歌词
#参数 1            2              3
#    函数: def 循环次数: int  函数参数: list
def thrs(*args) -> list:
    pool = ThreadPoolExecutor(max_workers=args[1])
    thr=[]
    arg_=[]
    i=args[2:]
    for o in range(len(i[0])):
        arg=''
        for p in i:
            if type(p[o])==str:
                p[o]='"'+p[o]+'"'
            arg=arg+str(p[o])+','
        arg_.append(arg)
    for i in range(args[1]):
        out=eval(f'thr.append(pool.submit(args[0], {arg_[i]}))')
    pool.shutdown()
    for i in range(args[1]):
        try:
            thr.append(thr[i].result())
        except:
            thr.append('')
    return thr[args[1]+1:]
#歌词搜索
def lyr(mid: str, songid: int) -> str:
    header={'Host': 'c.y.qq.com', 'accept': 'application/json', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; PBAT00 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36', 'origin': 'https://y.qq.com', 'x-requested-with': 'mark.via', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://y.qq.com/', 'accept-encoding': 'gzip, deflate', 'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}
    songlyr=json.loads(requests.get(f"https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg?_=1640081854858&cv=4747474&ct=24&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=1&uin=1274210585&g_tk_new_20200303=548998976&g_tk=548998976&loginUin=1274210585&songmid={mid}&musicid={songid}",headers=header).text)['lyric']
    return base64.b64decode(songlyr).decode()
#音乐评论
def cet(songid: int, page: int) -> dict:
    url = f"https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid={songid}&cmd=8&needmusiccrit=0&pagenum={page}&pagesize=25"
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','referer':': https://y.qq.com/','origin':'https://y.qq.com'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        json_list = res.json()['comment']['commentlist']
        comment_list = []
        for item in json_list:
            content = item['rootcommentcontent'].strip()
            nick = item['nick'].strip()
            date = time.strftime("%Y-%m-%d",time.localtime(item['time']))
            comment_list.append({'nick':nick,'content':content,'date':date})
        return comment_list
#音乐搜索
def qq(music: str) -> list:
    def purl(songmid):
        url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?'
        middata = 'data={"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":1248959521,"g_tk_new_20200303":1832066374,"g_tk":1832066374},"req_1":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"6846657260","songmid":["%s"],"songtype":[0],"uin":"1248959521","loginflag":1,"platform":"20"}}}' % (songmid)
        try:
            r = requests.get(url+middata, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',})
            r.encoding = 'utf-8'
            return json.loads(r.text).get('req_1').get('data').get('midurlinfo')[0].get('purl')
        except:
            print('获取purl失败')
            return ''
    info=requests.get(f'https://c.y.qq.com/soso/fcgi-bin/search_for_qq_cp?_=1640068893155&g_tk=5381&uin=&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=h5&needNewCode=1&w={music}&zhidaqu=1&catZhida=1&t=0&flag=1&ie=utf-8&sem=1&aggr=0&perpage=20&n=20&p=1&remoteplace=txt.mqq.all',headers={'Host': 'c.y.qq.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; PBAT00 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-gpc': '1', 'dnt': '1', 'save-data': 'on', 'x-requested-with': 'mark.via', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': 'https://i.y.qq.com/', 'accept-encoding': 'gzip, deflate', 'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'}).text
    info=json.loads(info)
    nian=info["data"]["song"]["list"]
    info=[]
    pool = ThreadPoolExecutor(max_workers=len(nian))
    thr=[]
    for i in nian:
        thr.append(pool.submit(purl, i['songmid']))
    #关闭线程池
    pool.shutdown()
    for i in range(len(nian)):
        purl=thr[i].result()
        i=nian[i]
        info.append([i['songname']+'-'+i['singer'][0]['name'],#歌名
                     i['singer'][0]['mid'],#mid
                     i['songid'],#歌曲id
                     i['songmid'],#歌曲mid
                     i['albummid'],#almid
                     "https://dl.stream.qqmusic.qq.com/"+purl,#播放链接
                     f"http://y.gtimg.cn/music/photo_new/T002R800x800M000{i['albummid']}.jpg",#图片
                     f"http://y.qq.com/#type=song&id={i['songid']}",#跳转链接
                      ])
    return info
#结果处理
def tyset(info: list) -> list:
    out=[]
    for i in info:
        out.append({
            'name': i[0],
            'mid': i[1],
            'songid': i[2],
            'songmid': i[3],
            'almid': i[4],
            'url': i[5],
            'img': i[6],
            'jump': i[7],
        })
    return out