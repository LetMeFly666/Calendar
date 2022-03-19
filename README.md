<!--
 * @Author: LetMeFly
 * @Date: 2022-01-27 22:13:45
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-03-19 19:46:07
-->
{% raw %}

# Calendar

微信小程序——默默无闻的日历罢了

<center><img src="Docs/MiniProgramCode.jpg" /></center>

**项目地址：** [https://github.com/LetMeFly666/Calendar](https://github.com/LetMeFly666/Calendar)

**在线文档：** [https://docs.diary.letmefly.xyz/](https://docs.diary.letmefly.xyz/)

## 配置说明

### 环境准备

完全使用该项目之前，请具备以下条件

1. 服务器
   >
   > 1. 拥有一台服务器
   >
   > 2. 拥有公网ip
   >
   > 3. 完成备案
   >
   > 4. 开启了https（微信小程序的限制）

2. MySQL
   >
   > 1. 配置好了MySQL环境
   >
   > 2. 为该项目创建了一个database
   >
   > 3. 为该项目创建了一个用户，且该用户只具有操作此库的权限（减小可能的SQL注入造成的损失）

3. python
   > 
   > 1. 配置好了python环境
   >
   > 2. 安装了django（pip install django）、requests、django-crontab

### 使用方法

1. 将项目克隆到本地```git clone git@github.com:LetMeFly666/Calendar.git```

2. 将```.\Front\```作为微信小程序的前端文件夹，将其上传至微信小程序开发平台，审核发布或设为体验

3. 在微信小程序管理平台设置好图标、名称等信息，配置服务器中添加自己的服务器

4. 在微信小程序管理平台选择“功能 -> 订阅消息”，在“公共模板库”中找到“日程提醒”并选用，选择三个“关键词”(“日程时间”、“提醒内容”、“备注”)，“提交”并在“我的模板”中Copy“模板ID”

5. 进入```.\Back\```，创建Secrets.py，在Secrets.py中，配置以下信息
   > SECRET_KEY = 'django-insecure-jafljalfsf*@46s' # 一串随机字符
   >
   > DATABASE_DBNAME = '数据库名称'
   >
   > DATABASE_USER = '数据库用户名'
   >
   > DATABASE_PASSWORD = '数据库密码'
   >
   > DATABASE_HOST = '数据库服务主机'
   >
   > DATABASE_PORT = '数据库端口'
   >
   > APP_ID = '微信小程序的AppID'
   >
   > APP_SECRET = '微信小程序的AppSecret'
   >
   > TEMPLATE_ID_DIARY_REMINDER = '微信消息订阅模板id'

5. （启动mysql服务并)进行初始化```python manage.py makemigrations```、```python manage.py migrate```、```python manage.py crontab add```，之后运行即可(```python manage.py runserver```)

<large><b><font color="#f47920">喜欢了别忘了给个star哦</font></b></large>

## Docs

项目文档、笔记等

## Front

前端代码，即在微信小程序开发工具中的那一套

前端全局配置笔记：[https://letmefly.xyz/Notes/WXminiProgram/](https://letmefly.xyz/Notes/WXminiProgram/)

### 前端函数

<small><u>“前端函数”中的介绍以 .\Front\ 作为根目录</u></small>

#### formatTime

**位置：** utils/util.js

**功能：** 将javascript的Date转化为“yyyy-MM-dd hh:mm:ss”格式的字符串

**示例：**

```javascript
const dateNow = new Date();
console.log(formatTime(dateNow));

// 2022-02-13 17:18:54
```

#### LetMeFly_request

**位置：** utils/util.js

**功能：** （微信小程序不支持cookie），此函数为二次封装的wx.request，使请求自动带上Storage中的session

**示例：**

```javascript
LetMeFly_request({
    url: 'https://diary.letmefly.xyz/GetAllDiaries/',
    success: function(msg) {
        const { diaries } = msg.data;
        console.log(diaries);
    }
});

// ["第一个日记", "第二个日记", "66666"]
```

**注释：** 服务器接收到微信小程序中的sessionid后，就可以取出session中保存的信息

#### Subscribe1Reminder

**位置：** utils/util.js

**功能：** 让用户订阅一次消息提醒

**示例：**

```javascript
Subscribe1Reminder();

// （微信小程序将会询问是否订阅）
```

**注释：** 当前函数仅支持订阅一总类型的消息，即为“日程到期提醒”

## Back

后端代码，即后端逻辑，采用python的django实现。

### 后端函数接口

#### login

**url：** /login/

**函数：** Apps.Functions.User.login

```
登录函数，实现微信小程序的登陆功能
函数根据登陆请求中的code向微信服务器索要用户openid和session_key
    openid - 每个用户独一无二，唯一不变，用来唯一标识每个用户
    session_key - 用来“数据签名校验”、“数据加密解密”等，会过期(但此次登陆结束之前不会过期)

Parameters:
    request - http request
        request.GET - {"code": (wx.login -> msg) msg.code}
    
Returns:
    JsonResponse - {"code": 0}
```

#### add1diary

**url：** /AddADiary/

**函数：** Apps.Functions.User.add1diary

```
添加一个日记

Parameters:
    request - http request
        request.session - 包含登录时保存到小程序Storage中的sessionid，由此来获取用户的userid
        json.loads(request.body) - {"content": 要添加的日记的内容}

Returns:
    JsonResponse - {"code": 状态码}
        0 - 发送成功
        1 - 内容为空
```

#### getAllDiaries

**url：** /GetAllDiaries/

**函数：** Apps.Functions.User.getAllDiaries

```
获取所有日记

Parameters:
    request - http request
        request.session - 包含登录时保存到小程序Storage中的sessionid，由此来获取用户的userid

Returns:
    JsonResponse - {"code": 0, "diaries": diaries}
        diaries - [日记1, 日记2, 日记3, ...]
            日记1 - {"content": 日记内容, "id": 日记id, "publishTime": 发布时间, "remindTime": 提醒时间}
```

#### get1diary

**url：** /Get1Diary/

**函数：** Apps.Functions.User.get1diary

```
获取一个日记

Parameters:
    request - http request
        session - session
        diaryId - 要操作的日记的id

Returns:
    JsonResponse - http response
        成功 - {"code": 0, "diary": 日记}
            日记 - {"content": 日记内容, "id": 日记id, "publishTime": 发布时间, "remindTime": 提醒时间}
        失败 - {"code": 非0}
            code - 1 没有权限
```

#### del1diary

**url：** /Del1Diary/

**函数：** Apps.Functions.User.del1diary

```
删除一条日记

Parameters:
    request - http request
        session - session
        diaryId - 要操作的日记的id

Returns:
    code - 状态码
        0 - 删除成功
        1 - 没有权限或日记不存在
```

#### getAccessToken

**url：** 无

**函数：** Apps.Functions.Server.getAccessToken

```
获取小程序全局唯一后台接口调用凭据（access_token）

Returns:
    json - 调用结果
        正常调用 - {"access_token": "ACCESS_TOKEN", "expires_in": 7200} (过期时间当前为2h，后期可能会有所调整)
        系统繁忙 - {"errcode": 40001, "errmsg": ...}
```

#### send1Message

**url：** 无

**函数：** Apps.Functions.Server.send1Message

```
推送一次消息给用户

Parameters:
    toWho - 用户的openid
    templateId - 模板的template_id
    data - 要替换的模板中的内容
        {"date4": {"value": "2022-02-14 16:58"}, "thing1": {"value": "..."}, ...}

Returns:
    code - 状态码
        0 - 发送成功
        1 - 用户拒收（用户撤销了订阅 或 用户未订阅）
        2 - 不合法的用户openid
        -1 - 其他错误
```


#### send1Message_DiaryReminder

**url：** 无

**函数：** Apps.Functions.Server.send1Message_DiaryReminder

```
推送一次用户设置的提醒给用户

Parameters:
    toWho - 用户的openid
    date - 提醒时间
    content - 消息内容 （微信要求20字以内，若超过将会被截取为{{前17个字}...}）
    jumpto - 用户点击消息卡片所跳转到的页面，默认我“我的日记页面”

Returns:
    code - 状态码
        0 - 发送成功
        1 - 用户拒收（用户撤销了订阅 或 用户未订阅）
        2 - 不合法的用户openid
        -1 - 其他错误
```

### 后端数据库

#### 用户

```python
class user(models.Model):
    userid = models.CharField(verbose_name="openid", max_length=40, unique=True)
    session_key = models.CharField(verbose_name="session_key", max_length=40)
    remark = models.CharField(verbose_name="备注", max_length=50, null=True)
```

#### 日记

```python
class diaries(models.Model):
    userid = models.CharField(verbose_name="openid", max_length=40)
    content = models.CharField(verbose_name="日记内容", max_length=1024)
    publish_time = models.DateTimeField(verbose_name="发布时间", auto_now_add=True)
    remind_time = models.DateTimeField(verbose_name="提醒时间", null=True)
```

## TODO

- [ ] <code>icon</code> 和 <code>source/Img</code>重复性冗余，待整合

- [ ] <code>user/usser</code>误拼

- [ ] 发行版<code>pages/user/usser</code>页面不能获取用户头像和昵称。自21年起就不能直接获取用户头像和信息了，必须使用wx.getUserProfile来获取。但是wx.getUserProfile每次调用都需要弹窗获得用户的同意，除非获取一次后就把头像、昵称保存到服务器。这就需要增加不少的后端代码。我猜，这就是为什么很多小程序头像都是失效图片的原因吧。

- [ ] 从“我的日记”页面进入一个日记并日记后会跳转到新的“我的日记”页面，新的“我的日记”页面不会展示刚刚删除的日记。但是如果用户点击两次“返回”，就会先返回到刚刚删除日记的那个页面，然后再次返回就会回到删除日记之前的“我的日记”页面。这个页面中的日记仍会显示，若用户再次点击此条日记就会访问一条已经删除的日记儿出现错误。

- [x] “我的日记”页面的内容应该以时间为依据倒序显示，即最新发布的最前。

- [x] 采用自定义url的图片，不修改源码可实现背景图片的更换

{% endraw %}