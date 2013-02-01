#!/usr/bin/ python
# -*- coding: utf-8 -*-
# Auther: lomatus@163.com
# 
# Decription: Class for binding API of Denglu.cc 
# Denglu.cc is an social login and commnets service provider of China
#
class Denglu():
    appID = ''
    apiKey = ''
    enableSSL = True
    domain = 'http://open.denglu.cc'
    http_usr_agent = ''
    apiPath = {
          'bind' : '/api/v3/bind',
          'unbind' : '/api/v3/unbind',
          'login' : '/api/v3/send_login_feed',
          'getUserInfo' : '/api/v4/user_info',
          'share' : '/api/v4/share',
          'getMedia' : '/api/v3/get_media',
          'unbindAll' : '/api/v3/all_unbind',
          'getBind' : '/api/v3/bind_info',
          'getInvite' : '/api/v3/friends',
          'getRecommend' : '/api/v3/recommend_user',
          'sendInvite' : '/api/v3/invite',
         'latestComment' : '/api/v4/latest_comment', # 最新评论
          'getComments' : '/api/v4/get_comment_list', # 评论列表，用于数据本地化
          'getCommentState' : '/api/v4/get_change_comment_ids' # 评论状态列表
     }
    charset = ''
    providers = {
          'google' : '/transfer/google',
          'windowslive' : '/transfer/windowslive',
          'sina' : '/transfer/sina',
          'tencent' : '/transfer/tencent',
          'sohu' : '/transfer/sohu',
          'netease' : '/transfer/netease',
          'renren' : '/transfer/renren',
          'kaixin001' : '/transfer/kaixin001',
          'douban' : '/transfer/douban',
          'yahoo' : '/transfer/yahoo',
          'qzone' : '/transfer/qzone',
          'alipay' : '/transfer/alipay',
          'taobao' : '/transfer/taobao',
          'tianya' : '/transfer/tianya',
          'alipayquick' : '/transfer/alipayquick',
          'guard360' : '/transfer/guard360',
          'tianyi' : '/transfer/tianyi',
          'facebook' : '/transfer/facebook',
          'twitter' : '/transfer/twitter'
     }
    user = ''
    __VERSION__ = '1.0'
    signatureMethod = 'MD5'

    #  构造函数
    #  @param appID     灯鹭后台分配的appID {@link http://open.denglu.cc}
    #  @param apiKey     灯鹭后台分配的apiKey {@link http://open.denglu.cc}
    #  #param charset 系统使用的编码类型utf-8 或gbk
    #  @param signatureMethod     签名算法，暂时只支持MD5
    #  
    def __init__(self, appID,  apiKey,  charset,  signatureMethod = 'MD5'):
      self.appID = appID
      self.apiKey = apiKey
      self.signatureMethod = signatureMethod
      self.charset = charset
      self.setEnableSSL = True

    # 
    # 获取登陆/绑定链接
    # 
    # @param isBind
    #           是否用于绑定（非绑定则为登录）
    # @param Provider
    #         通过Denglu.Provider p = Denglu.Provider.guess(mediaNameEn) 获取。
    #         mediaNameEn获取媒体列表中得到
    # @param uid
    #            用户网站的用户ID，绑定时需要
    # @throws DengluException
    # 
    def getAuthUrl( self, Provider,  isBind = False, uid = 0 ):
      authUrl = self.domain
      if slef.providers[Provider] is None:
           authUrl += self.providers[Provider]
      else:
           array = {'errorCode': 1,'errorDescription' : 'Please update your denglu-scripts to the latest version!'}
           return array
      if isBind and uid :
           authUrl += '?uid='+uid
      return authUrl


    # /**
    #  * 最新评论
    #  *
    # */
    def latestComment( self, count ):
      return self.callApi('latestComment',{'appid':self.appID, 'count': count}, 12)

    # /**
    #  * 返回自己应用的评论列表，用于本地化保存评论数据。
    #  *
    #  * @param commentid 若指定此参数，则返回ID比commentid大的评论（即比commentid时间晚的评论），默认为0。 
    #  * @param count    返回的记录条数，默认为50。 
    #  *
    #  * 返回值 eg: 
    #      {
    #           "postid":"1",
    #           "content":"我是一条评论",
    #           "mediaID":3,
    #           "createTime":"2012-04-26 12:38:14",
    #           "state":0,
    #           "commentID":38751,
    #           "userImage":"http://tp4.sinaimg.cn/2132511355/50/0/1",
    #                "userName":"testapis",
    #           "mediaUserID":1224050,
    #           "homepage":"http://weibo.com/2132511355",
    #           "ip":"106.3.63.172",
    #           "parent":
    #           {
    #                "postid":"1",
    #                "content":"我是它的父级评论",
    #                "mediaID":101,
    #                "commentID":38749,
    #                "userName":"水脉烟香",
    #                "userEmail":"xxx@qq.com",
    #                "mediaUserID":3529900,
    #                "homepage":"http://www.smyx.net/",
    #                "ip":"123.116.124.167"
    #           }
    #      }
    #  */
    def getComments( self, commentid,  count = 50):
      return self.callApi('getComments',{'appid': self.appID, 'commentid':commentid, 'count':count} )

    # /**
    #  * 返回自己应用的评论更新状态，比如评论被删除、审核，可以同步评论状态到本地。
    #  *
    #  * @param time 时间 单位为1小时，数字类型
    #  * 返回结果 灯鹭评论ID
    #  * 返回结果 0——正常评论，1——待审，2——垃圾评论，3——回收站，4——删除
    #  *
    #  * 返回值 eg: 
    #      {"582997":0,"571330":1,"571277":2,"583028":0}
    #  */
    def getCommentState(self, time):
      return self.callApi('getCommentState',{'appid':self.appID, 'time':time} )

    #  *
    #  * 根据token获取用户信息
    #  *
    #  * @param token
    #  *
    #  * 返回值 eg:
    #  * {
    #  *           "mediaID":7,                                   // 媒体ID
    #  *           "createTime":"2011-05-20 16:44:19",          // 创建时间
    #  *           "friendsCount":0,                              // 好友数
    #  *           "location":null,                              // 地址
    #  *           "favouritesCount":0,                         // 收藏数
    #  *           "screenName":"denglu",                         // 显示姓名
    #  *           "profileImageUrl":"http://head.xiaonei.com/photos/0/0/men_main.gif",          // 个人头像
    #  *           "mediaUserID":61,                              // 用户ID
    #  *           "url":null,                                        // 用户博客/主页地址
    #  *           "city":null,                                   // 城市
    #  *           "description":null,                              // 个人描述
    #  *           "createdAt":"",                                   // 在媒体上的创建时间
    #  *           "verified":0,                                   // 认证标志
    #  *           "name":null,                                   // 友好显示名称
    #  *           "domain":null,                                   // 用户个性化URL
    #  *           "province":null,                              // 省份
    #  *           "followersCount":0,                              // 粉丝数
    #  *           "gender":1,                                        // 性别 1--男，0--女,2--未知
    #  *           "statusesCount":0,                              // 微博/日记数
    #  *           "personID":120                                   // 个人ID
    #  * }
    #  *
    def getUserInfoByToken( self, token,  refresh = False):
      return self.callApi('getUserInfo', {'token':token} )

    #  *
    #  * 获取当前应用ID绑定的所有社会化媒体及其属性
    #  * 返回值 eg:
    #  * [
    #  *           {
    #  *                "mediaID":7,                                                                                          // ID
    #  *                "mediaIconImageGif":"http://test.denglu.cc/images/denglu_second_icon_7.gif",          // 社会化媒体亮色Icon
    #  *                "mediaIconImage":"http://test.denglu.cc/images/denglu_second_icon_7.png",               // 社会化媒体亮色Icon
    #  *                "mediaNameEn":"renren",                                                                                // 社会化媒体的名称的拼音
    #  *                "mediaIconNoImageGif":"http://test.denglu.cc/images/denglu_second_icon_no_7.gif",     // 社会化媒体灰色Icon
    #  *                "mediaIconNoImage":"http://test.denglu.cc/images/denglu_second_icon_no_7.png",          // 社会化媒体灰色Icon
    #  *                "mediaName":"人人网",                                                                                // 社会化媒体的名称
    #  *                "mediaImage":"http://test.denglu.cc/images/denglu_second_7.png",                         // 社会化媒体大图标
    #  *                "shareFlag":0,                                                                                          // 是否有分享功能 0是1否
    #  *                "apiKey":"704779c3dd474a44b612199e438ba8e2"                                                       // 社会化媒体的应用apikey
    #  *           }
    #  * ]
    #  *
    def getMedia(self):
      return self.callApi('getMedia',{'appid':slef.appID} )

    #  *
    #  *
    #  * 获得同一用户的多个社会化媒体用户信息
    #  *
    #  * @param uid
    #  *               用户网站的用户ID(可选)
    #  *
    #  * @param muid
    #  *               社会化媒体的用户ID
    #  *
    #  * @return 返回值
    #  *                     eq: {
    #  *                     {'mediaUserID'=>100,'mediaID'=>10,'screenName'=>'张三'),
    #  *                     {'mediaUserID'=>101,'mediaID'=>11,'screenName'=>'李四'),
    #  *                     {'mediaUserID'=>102,'mediaID'=>12,'screenName'=>'王五')
    #  *                     )
    #  *
    def getBind( self,  muid,  uid=None ):
      if muid is None:
           return self.callApi('getBind', { 'appid':self.appID, 'uid':uid}  )
      return self.callApi('getBind',{ 'appid':self.appID, 'muid':muid} )

    #  *
    #  *
    #  * 获取可以邀请的媒体用户列表
    #  *
    #  * @param uid
    #  *               用户网站的用户ID(可选)
    #  *
    #  * @param muid
    #  *               社会化媒体的用户ID
    #  *
    #  * @return 返回值
    #  *                     eq: {
    #  *                     {'mediaUserID'=>100,'mediaID'=>10,'screenName'=>'张三'),
    #  *                     {'mediaUserID'=>101,'mediaID'=>11,'screenName'=>'李四'),
    #  *                     {'mediaUserID'=>102,'mediaID'=>12,'screenName'=>'王五')
    #  *                     )
    #  *
    def getInvite( slef, muid,  uid=None ):
      if muid is None :
           return self.callApi('getInvite',{'appid':self.appID, 'uid':uid} )
      return self.callApi('getInvite',{ 'appid':self.appID, 'muid':muid} )

    # /**
    #  *
    #  * 获取可以推荐的媒体用户列表
    #  *
    #  * @param uid
    #  *               用户网站的用户ID(可选)
    #  *
    #  * @param muid
    #  *               社会化媒体的用户ID
    #  *
    #  * @return 返回值
    #  *                     eq: {
    #  *                     {'mediaUserID'=>100,'mediaID'=>10,'screenName'=>'张三'),
    #  *                     {'mediaUserID'=>101,'mediaID'=>11,'screenName'=>'李四'),
    #  *                     {'mediaUserID'=>102,'mediaID'=>12,'screenName'=>'王五')
    #  *                     )
    #  *
    #  */
    def getRecommend( self, muid,  uid=None ):
      if muid is None :
           return self.callApi('getRecommend',{'appid':self.appID, 'uid':uid} )
      return self.callApi('getRecommend',{'appid':self.appID, 'muid':muid} )

    # /**
    #  *
    #  * 发送邀请
    #  *
    #  * @param muid
    #  *               社会化媒体的用户ID
    #  *
    #  * @param uid
    #  *               用户网站的用户ID(可选)
    #  *
    #  * @return 返回值 eg: {"result": "1"}
    #  *
    #  */
    def sendInvite( self, invitemuids,  muid,  uid=None):
      if muid is None:
           return self.callApi('sendInvite',{'appid':self.appID, 'uid':uid, 'invitemuid':invitemuids} )
      return self.callApi('sendInvite',{ 'appid':self.appID, 'muid':muid, 'invitemuid':invitemuids} )

    # /**
    #  * 用户绑定多个社会化媒体账号到已有账号上
    #  *
    #  * @param mediaUID
    #  *            社会化媒体的用户ID
    #  * @param uid
    #  *            用户网站那边的用户ID
    #  * @param uname
    #  *            用户网站的昵称
    #  * @param uemail
    #  *            用户网站的邮箱
    #  * @return 返回值 eg: {"result": "1"}
    #  */
    def bind(self, mediaUID, uid, uname, uemail):
      return self.callApi('bind',{'appid':self.appID,'muid':mediaUID,'uid':uid,'uname':uname,'uemail':uemail} )

    # /**
    #  * 用户解除绑定社会化媒体账号
    #  *
    #  * @param mediaUID    社会化媒体的用户ID
    #  *
    #  * 返回值 eg: {"result": "1"}
    #  */
    def unbind(self, mediaUID):
      return self.callApi('unbind',{'appid':self.appID,'muid':mediaUID} )

    # /**
    #  * 发送登录的新鲜事
    #  *
    #  * @param mediaUserID
    #  *               从灯鹭获取的mediaUserID
    #  *
    #  * 返回值 eg: {"result": "1"}
    #  */
    def sendLoginFeed( self,mediaUserID):
      return  self.callApi('login',{'muid':mediaUserID,'appid':self.appID})

    # /**
    #  * 用户发布帖子、日志等信息时，可以把此信息分享到第三方
    #  *
    #  * @param mediaUserID
    #  * @param content    分享显示的信息
    #  * @param url    查看信息的链接
    #  * @param uid    网站用户的唯一性标识ID
    #  * @param imageurl    图片URL
    #  * @param videourl    视频URL
    #  * @param param1      文章ID, 用于同步微博的评论抓取回来
    #  *
    #  * 返回值 eg: {"result": "1"}
    #  */
    def share( self, mediaUserID, content, url, uid, imageurl = '', videourl = '', param1 = ''):
      return self.callApi('share',{'appid':self.appID,'muid':mediaUserID,'uid':uid,'content':content,'imageurl':imageurl,'videourl':videourl,'param1':param1,'url':url} )

    # /**
    #  * 用户解除所有绑定社会化媒体账号
    #  * @param uid 网站用户的唯一性标识ID
    #  *
    #  * 返回值 eg: {"result": "1"}
    #  */
    def unbindAll(self, uid):
      return self.callApi('unbindAll',{'uid':uid,'appid':self.appID} )

    # /**
    #  * 为HTTP请求加签名 签名算法： 
    #  * A、将请求参数格式化为“key=value”格式
    #  * B、将上诉格式化好的参数键值对，以字典序升序排列后，拼接在一起；“key=valuekey=value”
    #  * C、在上拼接好的字符串末尾追加上应用的api Key D、上述字符串的MD5值即为签名的值
    #  *
    #  * @param request
    #  */
    #  ksort in python : http://www.php2python.com/wiki/function.ksort/
    @staticmethod
    def ksort(dicts):
      return [(k,dicts[k]) for k in sorted(dicts.keys())]

    def signRequest(self, request):
        #print request
        self.ksort(request)
        sig = ''
        for key in request:
           sig += key+"="+request[key]
        sig += self.apiKey
        import hashlib
        return hashlib.md5(sig).hexdigest()

    # function is_array in python
    def is_array(var):
        lambda var: isinstance(var, (list, tuple))

    # /**
    #  * 将外部传进来的参数转换成http格式
    #  * @param param 数组
    #  */
    def createPostBody( self, param ):
        for key in param :
            v = param[key]
            #if is_array( v ):
            param[key] = ','.join(v)
            # PHP function strtolower = python string.lower()
            if self.charset.lower != 'utf-8' :
                param[key] = v.decode('utf-8').encode('gbk')
        # time() in python as time:
        import time
        t = int(time.time())
        param['timestamp'] = str(t)+'000'
        param['appid'] = self.appID
        param['sign_type'] = self.signatureMethod
        param['sign']  = self.signRequest(param)

        arr = []
        for key in param :
           v = param[key]
           import urllib
           # print urllib.quote_plus(s)
           # Array.append ( item ) add for each
           arr.append( key+'='+urllib.quote_plus(v) )
        return '&'.join(arr)  # ' '.join(array)

    # /**
    #  * 发送http请求并获得返回信息
    #  * @param method 请求的api类型
    #  * @param request 该请求所发送的参数
    #  * @param return 本请求是否有返回值
    #  */
    def callApi( self, method,request={} ):
        apiPath = self.getApiPath(method)
        post = self.createPostBody(request)
        result = self.makeRequest(apiPath,post)
        result = self.parseJson(result)
        if self.charset.lower() =='gbk':
            result = result.utf8_encode("GBK")
        if is_array(result) and result['errorCode'] != None:
            self.throwAPIException(result)
        return result

    # /**
    #  * 编码转换
    #  * @param str 需要转换的字符串
    #  * @param to 要转换成的编码
    #  * @param from 字符串的初始编码
    #  */
    #  str.decode('utf-8').encode('gbk')
    #  str.decode('gbk').encode('utf-8')
    

    # /**
    #  *抛出异常
    #  *@param result
    #  *
    #  */
    def throwAPIException(result):
        e = DengluException(result)
        Exception(e)

    # /**
    #  * 发送HTTP请求并获得响应
    #  * @param url 请求的url地址
    #  * @param request 发送的http参数
    #  */
    # ///////function makeRequest(request)
    # import types
    # def function_exists(fun):
    #     '''As in PHP, fun is tested as a name, not an object as is common in Python.'''
    #     try:
    #         ret = type(eval(str(fun)))
    #         return ret in (types.FunctionType, types.BuiltinFunctionType)
    #     except NameError:
    #         return False
    def makeRequest( self, url, post = '' ):
        returns = ''
        import urlparse # print urlparse.urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
        matches = urlparse.urlparse(url)
        host = matches[1]
        query = matches[4]
        path = matches[2]
        if query is None:
            query = ''
        path = ( path =='') and  path +( query =='' ) and '?'+ query or '' or '/'
        port = 80
        #  Translat to UrlLib2 from Curl
        import urllib2,httplib
        httplib.HTTPConnection._http_vsn = 10
        httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'
        req = urllib2.Request(url+path)
        req.add_header('User-Agent', 'denglu')
        usr_agent = self.http_usr_agent
        headers = {}
        if post is not None :
            req.get_method = lambda: "POST"
            headers = {"Accept":"*/*","Accept-Language":"zh-cn","Content-Type":"application/x-www-form-urlencoded","User-Agent: ":usr_agent,"Host":host,"Content-Length":len(post),"Connection":"Close","Cookie:":""}
        else :
            req.get_method = lambda: "GET"
            headers = {"Accept":"*/*","Accept-Language":"zh-cn","User-Agent":usr_agent,"Host":host,"Connection":"Close","Cookie":""}
        req = urllib2.Request(url,None,headers)
        print post   # req.headers
        openurl = urllib2.urlopen( req, timeout = 30,data=post)
        try:
            returns = openurl.load()
            return returns
        except urllib2.HTTPError,e:
            print e.code
            print e.read()
            #return pyOauth2Error
            #return {'errorCode':1,'errorDescription':"Your website can't connect to denglu server!"}



    # /**
    #  * 从apiPath数组里获得相应method的实际调用地址
    #  *
    #  * @param method
    #  */
    def getApiPath( self, method ):
      return self.domain+self.apiPath[method]

    # /**
    #  * 解析JSON字符串
    #  *
    #  * 把从接口获取到的数据转换成json格式，在解析中进行接口返回错误分析
    #  *
    #  * @param input
    #  */
    def parseJson(input):
        import json
        return json.loads(input)

    # /**
    #  *
    #  * @param input
    #  */
    def base64Encode(input):
      return input.encode('base64')

    # /**
    #  *
    #  * @param input
    #  */
    def base64Decode(input):
      return input.decode('base64')

    # /**
    #  *
    #  * @param input
    #  */

    def getapiKey():
      return self.apiKey

    # /**
    #  *
    #  * @param newVal
    #  */
    def setapiKey(newVal):
      self.apiKey = newVal


    def getappID():
      return self.appID

    # /**
    #  *
    #  * @param newVal
    #  */
    def setappID(newVal):
        self.appID = newVal

    def setEnableSSL():
        if function_exists('curl_init') and function_exists('curl_exec') :
            self.enableSSL = true


# /**
#  *异常类
# * 错误类型对照表
#  * Code Description
#  * 1      参数错误，请参考API文档
#  * 2      站点不存在
#  * 3      时间戳有误
#  * 4      只支持md5签名
#  * 5      签名不正确
#  * 6      token已过期
#  * 7      媒体用户不存在
#  * 8      媒体用户已绑定其他用户
#  * 9      媒体用户已解绑
#  * 10      未知错误
#  */

class DengluException():

     errorCode = ''
     errorDescription = ''

     def __init__( self, result ):
        self.result = result
        self.errorCode = result['errorCode']
        self.errorDescription = result['errorDescription']

     def geterrorCode(self):
          return self.errorCode

     # /**
     #  *
     #  * @param newVal
     #  */
     def seterrorCode(self,newVal):
          self.errorCode = newVal

     def geterrorDescription(self):
          return self.errorDescription
