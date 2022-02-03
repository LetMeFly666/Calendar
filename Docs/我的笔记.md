[TOC]

# 我的小程序笔记

在做学习并制作微信小程序的时候，记录了一些笔记，同时也遇到了一些BUG。

**有时候重启一下BUG就好了**(有时候重新点一下“编译”即可)。

<details>
<summary>WebAssembly..的莫名其妙报错</summary>
显示“WAServiceMainContext.js:2 TypeError: Cannot delete property 'WebAssembly' of...”的话，可能是调试基础库的版本问题。版本刚才是2.21.4，后面显示一共“灰度中”，不知道怎么回事，于是换成2.22.0，后面显示的70.96%，应该是使用的人比较多，然后报错就没有了。
</details>

## 服务端

### 用户登录、session_key、openid

使用<code>wx.login</code>获取用户<code>code</code>

```javascript
wx.login({
    success: function(msg) {
        const code = msg.code;
        // 之后把code发送到服务器即可
    }
});
```

服务器获取到<code>code</code>后，通过GET请求```https://api.weixin.qq.com/sns/jscode2session?appid={{AppID}}&secret={{AppSecret}}&js_code={{code}}&grant_type=authorization_code```获得<code>session_key</code>和<code>openid</code>

**openid**：

每个微信用户对应唯一不变的openid

**session_key**：

session_key用来“数据签名校验”、“数据加密解密”等。

若出现校验失败或解密失败，则可能是因为session_key过期。

> session_key的过期机制：
>
> 1. 重新登陆时session_key**可能**会过期。是否过期与微信后台 *刷新机制的最短周期* 有关。请勿重复进行登陆操作以免导致旧的session_key过期。
>
> 2. 微信不会告诉开发者session_key是否过期，具体过期时间由用户登陆小程序的频率决定。
>
> 3. 可在客户端使用<code>wx.checkSession</code>判断session_key是否过期
>
>    ```javascript
>    wx.checkSession({
>        success () {
>            //session_key 未过期，并且在本生命周期一直有效
>        },
>        fail () {
>            // session_key 已经失效，需要重新执行登录流程
>            wx.login() //重新登录
>        }
>    })
>    ```
>
>    


## 数据绑定

在对应页面的js中，

```javascript
Page({
    data: {
        'msg': 'Hello World'
    }
})
```

则可在对应的wxml中，

```html
<view>{{msg}}</view>
```

引用data中的msg。

小程序中将会显示

```
Hello World
```

**其中```{{}}```中支持字符串拼接、算术运算、逻辑判断等。**


## wx:for

```html
<view wx:for="{{数组或要循环的对象}}" wx:for-item="循环项的名称" wx:for-index="循环项的索引">
    索引{{循环项的索引}}是：{{循环项的名称}}
</view>
```

例如在js的data中有：

```javascript
array: ["太阳", "月亮"]
```

在wxml中有：

```html
<view wx:for="{{array}}" wx:for-item="item" wx:for-index="index">
    索引{{index}}是：{{item}}
</view>
```

渲染结果为：

```html
<view>
    索引0是：太阳
</view>
<view>
    索引1是：月亮
</view>
```

小程序中会有如下结果：

```
索引0是：太阳
索引1是：月亮
```

也就是说小程序会把<code>view</code>标签也渲染上。若不想渲染上<code>view等标签</code>，可以使用<code>block</code>。<code>block</code>不会被渲染成真正的dom元素。

```html
<block wx:for="{{array}}" wx:for-item="item" wx:for-index="index">索引{{index}}是：{{item}}</block>
```

渲染结果为：

```html
"索引0是：太阳"
"索引1是：月亮"
```

小程序中会有如下结果：

```
索引0是：太阳索引1是：月亮
```

### wx:key 

⽤来提⾼数组渲染的性能

可以绑定以下两种：

1. 循环项中的唯⼀属性，如：

   ```javascript
   array: [{id: 0, name: "炒饭"}, {id: 1, name: "炒面"}]
   ```

   ```html
   wx:key="id"
   ```

2. *this

   意思是 item 本⾝，*this代表的必须是唯一的字符串和数组

## wx:if

在框架中，使⽤ <code>wx:if="{{condition}}"</code> 来判断是否需要渲染该代码块：

```html
<view wx:if="{{false}}">1</view>
<view wx:elif="{{true}}">2</view>
<view wx:else>3</view>
```

### hidden

```html
<view hidden="{{condition}}"> True </view>
```

## 事件绑定

### input的事件绑定

```html
<input bindInput="ha" />
```

```javascript
Page({
    ha(e) {
        console.log(e);
    }
})
```

则input输入框中有输入变化时，会调用ha函数。

另外几种绑定方式：

```html
<input bindinput="ha" />
<input bindinput="ha2" />
<input bindinput="ha3" />
```

```javascript
function fa(e) {
    console.log(e);
}

Page({
    ha(e) {
        console.log(e);
    },
    ha2: function(e) {
        console.log(e);
    },
    ha3: fa
});
```

#### 和值绑定

假设data中有num，要想把input框中的数据和num绑定，有两种方式：

```html
<input />
<view>{{num}}</view>
```

想要达到的效果：input框中的数据一旦发生变化，num就随之改变

##### 通过函数

设置data中的数据的值，方式是：```this.setData({要设置的值的名称: 要设置的值})```

```html
<input type="number" bindinput="fun" />
<view>{{num}}</view>
```

```javascript
Page({
    data: {
        num: 0
    },
    fun(e) {
        const newNum = e.detail.value;
        this.setData({
            num: newNum
        })
    }
})
```

##### 通过model

直接在<code>input</code>中设置<code>model:value="{{num}}"</code>

```html
<input type="number" model:value="{{num}}" />
<view>{{num}}</view>
```

```javascript
Page({
    data: {
        num: 0
    },
})
```

这样同样能达到上述效果。但是每次对输入框中的值进行修改，控制台都会报一个warning，说是input框未绑定输入处理函数。

因此若想要把警告取消掉，绑定一个没有实际功能的函数即可。

```html
<input type="number" model:value="{{num}}" bindinput="fakeFunction"/>
<view>{{num}}</view>
```

```javascript
Page({
    data: {
        num: 0
    },
    fakeFunction(e) {
        // 什么功能都没有
    }
})
```

### button的事件绑定

假设想要实现：两个按钮，一个加一个减，点击加号数字加一，点击减号数字减一。

若要通过一个函数实现，则函数必须知道点击的是哪个按钮。

但是若<code>bindtap="f(1)"</code>，则微信小程序会傻傻地把<code>f(1)</code>当成函数名，然后说没有函数“f(1)”，而不是去调用f(1)(e)。

#### 通过data-属性传递参数

因此可以在按钮上设置属性<code>data-operation</code>来实现。

```html
<view>{{num}}</view>
<button bindtap="f" data-operation="{{1}}">+</button>
<button bindtap="f" data-operation="{{-1}}">-</button> 
```

```javascript
Page({
    data: {
        num: 0
    },
    f(e) {
        /* 这个就是data-operation中的值 */
        const operation = e.currentTarget.dataset.operation;
        this.setData({
            num: this.data.num + operation
        });
    }
})
```

这样就实现了点击<code>+</code>时num+1，点击<code>-</code>时num+(-1)。

<code>button</button>上的属性<code>data-operation</code>的值会被传递到函数的<code>e.currentTarget.dataset.operation</code>

同理，若

```html
<button bindtap="f" data-num="{{1}}" data-name="+">+</button>
```

```javascript
Page({
    f(e) {
        console.log(e.currentTarget.dataset);
    }
})
```

则每次点击加号按钮，控制台都会输出

```javascript
{name: "+", num: 1}
```
