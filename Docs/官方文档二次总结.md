[TOC]



# 微信小程序笔记

微信小程序的一些笔记，很多在<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/">官方文档</a>中都可找到

但是与官网**有所不同**，一些是从实际的角度出发而记录的

本笔记在线版本：[https://letmefly.xyz/Notes/WXminiProgram/](https://letmefly.xyz/Notes/WXminiProgram/)


## 安装

[下载页面](https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html)


## 项目目录<a id="XiangMuMuLu">ㅤ</a>

```
.
│  app.js                  ------------------------ 项目的全局文件
│  app.json                ------------------------ 项目的全局文件
│  app.wxss                ------------------------ 项目的全局文件
│  project.config.json     ------------------------ 项目的配置信息
│  sitemap.json            ------------------------ 哪些页面可以被索引
│
├─pages                    ------------------------ 存放页面的文件夹
│  ├─index                 ------------------------ 页面index(下面有4个文件)
│  │      index.js         ------------------------ index页面的函数脚本
│  │      index.json       ------------------------ index页面的配置信息
│  │      index.wxml       ------------------------ index页面的页面代码
│  │      index.wxss       ------------------------ index页面的样式
│  │
│  └─logs                  ------------------------ logs页面
│          logs.js         ------------------------ (同index页面下的4个文件)
│          logs.json
│          logs.wxml
│          logs.wxss
│
└─utils                    ------------------------ 其他的包
        util.js
```

### app.json

<table>
<thead><tr><th>属性</th> <th>类型</th> <th>必填</th> <th>描述</th> <th>最低版本</th></tr></thead> 
<tbody><tr><td><a href="#entryPagePath">entryPagePath</a></td> <td>string</td> <td>否</td> <td>小程序默认启动首页</td> <td></td></tr> 
<tr><td><a href="#pages">pages</a></td> <td>string[]</td> <td>是</td> <td>页面路径列表</td> <td></td></tr> 
<tr><td><a href="#window">window</a></td> <td>Object</td> <td>否</td> <td>全局的默认窗口表现</td> <td></td></tr> 
<tr><td><a href="#tabBar">tabBar</a></td> <td>Object</td> <td>否</td> <td>底部 <code>tab</code> 栏的表现</td> <td></td></tr> 
<tr><td><a href="#networkTimeout">networkTimeout</a></td> <td>Object</td> <td>否</td> <td>网络超时时间</td> <td></td></tr> 
<tr><td><a href="#debug">debug</a></td> <td>boolean</td> <td>否</td> <td>是否开启 debug 模式，默认关闭</td> <td></td></tr> 
<tr><td><a href="#functionalPages">functionalPages</a></td> <td>boolean</td> <td>否</td> <td>是否启用插件功能页，默认关闭</td> <td>2.1.0</td></tr> 
<tr><td><a href="#subpackages">subpackages</a></td> <td>Object[]</td> <td>否</td> <td>分包结构配置</td> <td>1.7.3</td></tr> 
<tr><td><a href="#workers">workers</a></td> <td>string</td> <td>否</td> <td><code>Worker</code> 代码放置的目录</td> <td>1.9.90</td></tr> 
<tr><td><a href="#requiredBackgroundModes">requiredBackgroundModes</a></td> <td>string[]</td> <td>否</td> <td>需要在后台使用的能力，如「音乐播放」</td> <td></td></tr> 
<tr><td><a href="#plugins">plugins</a></td> <td>Object</td> <td>否</td> <td>使用到的插件</td> <td>1.9.6</td></tr> 
<tr><td><a href="#preloadRule">preloadRule</a></td> <td>Object</td> <td>否</td> <td>分包预下载规则</td> <td>2.3.0</td></tr> 
<tr><td><a href="#resizable">resizable</a></td> <td>boolean</td> <td>否</td> <td>PC 小程序是否支持用户任意改变窗口大小（包括最大化窗口）；iPad 小程序是否支持屏幕旋转。默认关闭</td> <td>2.3.0</td></tr> 
<tr><td><a href="#usingComponents">usingComponents</a></td> <td>Object</td> <td>否</td> <td>全局<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/" class="FIXME:">自定义组件</a>配置</td> <td>开发者工具 1.02.1810190</td></tr> 
<tr><td><a href="#permission">permission</a></td> <td>Object</td> <td>否</td> <td>小程序接口权限相关设置</td> <td>微信客户端 7.0.0</td></tr> 
<tr><td><a href="#sitemapLocation">sitemapLocation</a></td> <td>string</td> <td>是</td> <td>指明 sitemap.json 的位置</td> <td></td></tr> 
<tr><td><a href="#style">style</a></td> <td>string</td> <td>否</td> <td>指定使用升级后的weui样式</td> <td>2.8.0</td></tr> 
<tr><td><a href="#useExtendedLib"><b class="LetMeFly" title="前面href中大小写不一致"><font color="warning">useExtendedLib</font></b></a></td> <td>Object</td> <td>否</td> <td>指定需要引用的扩展库</td> <td>2.2.1</td></tr> 
<tr><td><a href="#entranceDeclare">entranceDeclare</a></td> <td>Object</td> <td>否</td> <td>微信消息用小程序打开</td> <td>微信客户端 7.0.9</td></tr> 
<tr><td><a href="#darkmode">darkmode</a></td> <td>boolean</td> <td>否</td> <td>小程序支持 DarkMode</td> <td>2.11.0</td></tr> 
<tr><td><a href="#themeLocation">themeLocation</a></td> <td>string</td> <td>否</td> <td>指明 theme.json 的位置，darkmode为true为必填</td> <td>开发者工具 1.03.2004271</td></tr> 
<tr><td><a href="#lazyCodeLoading">lazyCodeLoading</a></td> <td>string</td> <td>否</td> <td>配置自定义组件代码按需注入</td> <td>2.11.1</td></tr> 
<tr><td><a href="#singlePage">singlePage</a></td> <td>Object</td> <td>否</td> <td>单页模式相关配置</td> <td>2.12.0</td></tr> 
<tr><td>supportedMaterials</td> <td>Object</td> <td>否</td> <td><a href="https://developers.weixin.qq.com/miniprogram/dev/framework/material/support_material.html" class="FIXME:">聊天素材小程序打开</a>相关配置</td> <td>2.14.3</td></tr> 
<tr><td>serviceProviderTicket</td> <td>string</td> <td>否</td> <td><a href="https://developers.weixin.qq.com/doc/oplatform/Third-party_Platforms/2.0/operation/thirdparty/customized_service_platform_guidelines.html" target="_blank" rel="noopener noreferrer">定制化型服务商<span></span></a>票据</td> <td></td></tr> 
<tr><td><a href="#embeddedAppIdList">embeddedAppIdList</a></td> <td>string[]</td> <td>否</td> <td>半屏小程序 appId</td> <td>2.20.1</td></tr> 
<tr><td><a href="#halfPage">halfPage</a></td> <td>Object</td> <td>否</td> <td>视频号直播半屏场景设置</td> <td>2.18.0</td></tr></tbody>
</table>


#### entryPagePath<a id="entryPagePath">ㅤ</a>

微信小程序的主页(启动的页面)。

若无此项，则会以```"pages"```中的第一个为准。

#### pages<a id="pages">ㅤ</a>

如<a href="#XiangMuMuLu">项目目录</a>中共有两个页面，则pages应写为：

```json
"pages": [
    "pages/index/index", 
    "pages/logs/logs"
]
```


#### window<a id="window">ㅤ</a>

用于设置小程序的状态栏、导航条、标题、窗口背景色

<table><thead>
<tr><th>属性</th> <th>类型</th> <th>默认值</th> <th>描述</th> <th>最低版本</th></tr></thead> <tbody>
<tr><td>navigationBarBackgroundColor</td> <td>HexColor</td> <td>#000000</td> <td>导航栏背景颜色，如 <code>#000000</code></td> <td></td></tr> 
<tr><td>navigationBarTextStyle</td> <td>string</td> <td>white</td> <td>导航栏标题颜色，仅支持 <code>black</code> / <code>white</code></td> <td></td></tr> 
<tr><td>navigationBarTitleText</td> <td>string</td> <td></td> <td>导航栏标题文字内容</td> <td></td></tr> 
<tr><td>navigationStyle</td> <td>string</td> <td>default</td> <td>导航栏样式，仅支持以下值：<br><code>default</code> 默认样式<br> <code>custom</code> 自定义导航栏，只保留右上角胶囊按钮。参见注 2。</td> <td>iOS/Android 微信客户端 6.6.0，Windows 微信客户端不支持</td></tr> 
<tr><td>backgroundColor</td> <td>HexColor</td> <td>#ffffff</td> <td>窗口的背景色</td> <td></td></tr> 
<tr><td>backgroundTextStyle</td> <td>string</td> <td>dark</td> <td>下拉 loading 的样式，仅支持 <code>dark</code> / <code>light</code></td> <td></td></tr> 
<tr><td>backgroundColorTop</td> <td>string</td> <td>#ffffff</td> <td>顶部窗口的背景色，仅 iOS 支持</td> <td>微信客户端 6.5.16</td></tr> 
<tr><td>backgroundColorBottom</td> <td>string</td> <td>#ffffff</td> <td>底部窗口的背景色，仅 iOS 支持</td> <td>微信客户端 6.5.16</td></tr> 
<tr><td>enablePullDownRefresh</td> <td>boolean</td> <td>false</td> <td>是否开启全局的下拉刷新。<br>详见 <a href="https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onpulldownrefresh" class="FIXME:">Page.onPullDownRefresh</a></td> <td></td></tr> 
<tr><td>onReachBottomDistance</td> <td>number</td> <td>50</td> <td>页面上拉触底事件触发时距页面底部距离，单位为 px。<br>详见 <a href="https://developers.weixin.qq.com/miniprogram/dev/reference/api/Page.html#onreachbottom" class="FIXME:">Page.onReachBottom</a></td> <td></td></tr> 
<tr><td>pageOrientation</td> <td>string</td> <td>portrait</td> <td>屏幕旋转设置，支持 <code>auto</code> / <code>portrait</code> / <code>landscape</code> <br>详见 <a href="https://developers.weixin.qq.com/miniprogram/dev/framework/view/resizable.html" class="FIXME:">响应显示区域变化</a></td> <td>2.4.0 (auto) / 2.5.0 (landscape)</td></tr> 
<tr><td><a href="#restartStrategy" class="FIXME:">restartStrategy</a></td> <td>string</td> <td>homePage</td> <td>重新启动策略配置</td> <td>2.8.0</td></tr>
<tr><td>initialRenderingCache</td> <td>string</td> <td></td> <td>页面<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/view/initial-rendering-cache.html" class="FIXME:">初始渲染缓存</a>配置，支持 <code>static</code> / <code>dynamic</code></td> <td>2.11.1</td></tr> 
<tr><td>visualEffectInBackground</td> <td>string</td> <td>none</td> <td>切入系统后台时，隐藏页面内容，保护用户隐私。支持 <code>hidden</code> / <code>none</code></td> <td>2.15.0</td></tr></tbody></table>

##### restartStrategy<a id="restartStrategy">ㅤ</a>

> 基础库 2.8.0 开始支持，低版本需做兼容处理。

<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/operating-mechanism.html#_2-1-重新启动策略" class="FIXME:">重新启动策略配置</a>

|可选值| 含义|
|--|--|
|homePage|（默认值）如果从这个页面退出小程序，下次将从首页冷启动|
|homePageAndLatestPage|如果从这个页面退出小程序，下次冷启动后立刻加载这个页面，页面的参数保持不变（不可用于 tab 页）|

例：

```json
{
    "window": {
        "navigationBarBackgroundColor": "#ffffff",
        "navigationBarTextStyle": "black",
        "navigationBarTitleText": "微信接口功能演示",
        "backgroundColor": "#eeeeee",
        "backgroundTextStyle": "light"
    }
}
```


#### tabBar<a id="tabBar">ㅤ</a>

小程序底部或顶部可以有tab栏指定切换页面

<table><thead>
<tr><th>属性</th> <th>类型</th> <th>必填</th> <th>默认值</th> <th>描述</th> <th>最低版本</th></tr></thead> <tbody>
<tr><td>color</td> <td>HexColor</td> <td><a class="LetMeFly"><font color="warning">否</font></a></td> <td><a class="LetMeFly"><font color="warning">black</font></a></td> <td>tab 上的文字默认颜色，仅支持十六进制颜色</td> <td></td></tr> 
<tr><td>selectedColor</td> <td>HexColor</td> <td><a class="LetMeFly"><font color="warning">否</font></a></td> <td><a class="LetMeFly"><font color="warning">#1aad19</font></a></td> <td>tab 上的文字选中时的颜色，仅支持十六进制颜色</td> <td></td></tr> 
<tr><td>backgroundColor</td> <td>HexColor</td> <td><a class="LetMeFly"><font color="warning">否</font></a></td> <td><a class="LetMeFly"><font color="warning">white</font></a></td> <td>tab 的背景色，仅支持十六进制颜色</td> <td></td></tr> 
<tr><td>borderStyle</td> <td>string</td> <td>否</td> <td>black</td> <td>tabbar 上边框的颜色， 仅支持 <code>black</code> / <code>white</code></td> <td></td></tr> 
<tr><td><a class="LetMeFly" href="#list_my"><font color="warning">list</font></a></td> <td>Array</td> <td>是</td> <td></td> <td>tab 的列表，详见 <code>list</code> 属性说明，最少 2 个、最多 5 个 tab</td> <td></td></tr> 
<tr><td>position</td> <td>string</td> <td>否</td> <td>bottom</td> <td>tabBar 的位置，仅支持 <code>bottom</code> / <code>top</code></td> <td></td></tr> 
<tr><td>custom</td> <td>boolean</td> <td>否</td> <td>false</td> <td>自定义 tabBar，见<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/ability/custom-tabbar.html" class="FIXME:">详情</a></td> <td>2.5.0</td></tr></tbody></table>

##### list <a id="list_my">ㅤ</a>

数组。能配置[2, 5]个tab，每个tab都是一个对象，其值如下：

<table><thead>
<tr><th>属性</th> <th>类型</th> <th>必填</th> <th>说明</th></tr></thead> <tbody>
<tr><td>pagePath</td> <td>string</td> <td>是</td> <td>页面路径，必须在 pages 中先定义</td></tr> 
<tr><td>text</td> <td>string</td> <td>是</td> <td>tab 上按钮文字</td></tr> 
<tr><td>iconPath</td> <td>string</td> <td>否</td> <td>图片路径，icon 大小限制为 40kb，建议尺寸为 81px * 81px，不支持网络图片。<br><strong>当 <code>position</code> 为 <code>top</code> 时，不显示 icon。</strong></td></tr> 
<tr><td>selectedIconPath</td> <td>string</td> <td>否</td> <td>选中时的图片路径，icon 大小限制为 40kb，建议尺寸为 81px * 81px，不支持网络图片。<br><strong>当 <code>position</code> 为 <code>top</code> 时，不显示 icon。</strong></td></tr></tbody></table>


#### networkTimeout<a id="networkTimeout">ㅤ</a>

网络请求的Timeout(超时时间)，单位ms

<table><thead>
<tr><th>属性</th> <th>类型</th> <th>必填</th> <th>默认值</th> <th>说明</th></tr></thead> <tbody>
<tr><td>request</td> <td>number</td> <td>否</td> <td>60000</td> <td><a href="https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html" class="FIXME:">wx.request</a> 的超时时间，单位：毫秒。</td></tr> 
<tr><td>connectSocket</td> <td>number</td> <td>否</td> <td>60000</td> <td><a href="https://developers.weixin.qq.com/miniprogram/dev/api/network/websocket/wx.connectSocket.html" class="FIXME:">wx.connectSocket</a> 的超时时间，单位：毫秒。</td></tr> 
<tr><td>uploadFile</td> <td>number</td> <td>否</td> <td>60000</td> <td><a href="https://developers.weixin.qq.com/miniprogram/dev/api/network/upload/wx.uploadFile.html" class="FIXME:">wx.uploadFile</a> 的超时时间，单位：毫秒。</td></tr> 
<tr><td>downloadFile</td> <td>number</td> <td>否</td> <td>60000</td> <td><a href="https://developers.weixin.qq.com/miniprogram/dev/api/network/download/wx.downloadFile.html" class="FIXME:">wx.downloadFile</a> 的超时时间，单位：毫秒。</td></tr></tbody></table>

#### debug<a id="debug">ㅤ</a>

可以在开发者工具中开启 debug 模式，在开发者工具的控制台面板，调试信息以 info 的形式给出，其信息有 Page 的注册，页面路由，数据更新，事件触发等。可以帮助开发者快速定位一些常见的问题。

#### functionalPages<a id="functionalPages">ㅤ</a>

> 基础库 2.1.0 开始支持，低版本需做兼容处理

插件所有者小程序需要设置这一项来启用<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/functional-pages.html" class="FIXME:">插件功能页</a>




#### subpackages<a id="subpackages">ㅤ</a>

> 微信客户端 6.6.0 ，基础库 1.7.3 及以上版本支持

启用<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages.html" class="FIXME:">分包加载</a>时，声明项目分包结构。

> 写成 subPackages 也支持。

#### workers<a id="workers">ㅤ</a>

基础库 1.9.90 开始支持，低版本需做兼容处理。

使用 <a href="https://developers.weixin.qq.com/miniprogram/dev/framework/workers.html" class="FIXME:">Worker</a> 处理多线程任务时，设置 <code>Worker</code> 代码放置的目录

#### requiredBackgroundModes<a id="requiredBackgroundModes">ㅤ</a>

> 微信客户端 6.7.2 及以上版本支持

申明需要后台运行的能力，类型为数组。目前支持以下项目：

> + audio: 后台音乐播放
>
> + location: 后台定位

如：

```json
"requiredBackgroundModes": {
    "pages": ["pages/index/index"],
    "requiredBackgroundModes": ["audio", "location"]
}
```

**注**：在此处申明了后台运行的接口，开发版和体验版上可以直接生效，正式版还需通过审核。

#### plugins<a id="plugins">ㅤ</a>

> 基础库 1.9.6 开始支持，低版本需做兼容处理。

声明小程序需要使用的<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/using.html" class="FIXME:">插件</a>。

#### preloadRule<a id="preloadRule">ㅤ</a>

> 基础库 2.3.0 开始支持，低版本需做兼容处理。

声明<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages/preload.html" class="FIXME:">分包预下载</a>的规则。

#### resizable<a id="resizable">ㅤ</a>

> 基础库 2.3.0 开始支持，低版本需做兼容处理。

在 iPad 上运行的小程序可以设置支持<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/view/resizable.html" class="FIXME:">屏幕旋转</a>。

在 PC 上运行的小程序，用户可以按照任意比例拖动窗口大小，也可以在小程序菜单中最大化窗口

#### usingComponents<a id="usingComponents">ㅤ</a>

> 开发者工具 1.02.1810190 及以上版本支持

在 app.json 中声明的自定义组件视为全局自定义组件，在小程序内的页面或自定义组件中可以直接使用而无需再声明。

**注意**：全局声明的自定义组件会视为被所有页面依赖，会在所有页面启动时进行初始化，且会占用主包大小。只被个别页面或分包引用的自定义组件应尽量在页面配置中声明。

#### permission<a id="permission">ㅤ</a>

> 微信客户端 7.0.0 及以上版本支持

小程序接口权限相关设置。字段类型为 <code>Object</code>，结构为：

|属性|	类型|	必填	|默认值|	描述|
|--|--|--|--|--|
|scope.userLocation|	<a href="#PermissionObject">PermissionObject</a>|	否|	|	位置相关权限声明|


##### PermissionObject 结构 <a id="PermissionObject">ㅤ</a>

|属性|	类型|	必填	|默认值|	描述|
|--|--|--|--|--|
|desc|	string|	是|	|	小程序获取权限时展示的接口用途说明。最长 30 个字符|

例：

```json
{
    "pages": ["pages/index/index"],
    "permission": {
        "scope.userLocation": {
            "desc": "你的位置信息将用于小程序位置接口的效果展示" // 高速公路行驶持续后台定位
        }
    }
}
```

#### sitemapLocation<a id="sitemapLocation">ㅤ</a>

指明 sitemap.json 的位置；默认为 'sitemap.json' 即在 app.json 同级目录下名字的 <code>sitemap.json</code> 文件

#### style<a id="style">ㅤ</a>

> 基础库 2.8.0 开始支持，低版本需做兼容处理。

微信客户端 7.0 开始，UI 界面进行了大改版。小程序也进行了基础组件的样式升级。app.json 中配置 <code>"style": "v2"</code>可表明启用新版的组件样式。

本次改动涉及的组件有 <code>button icon radio checkbox switch slider</code>。可前往小程序示例进行体验。

#### useExtendedLib<a id="useExtendedLib">ㅤ</a>

> 基础库 2.2.1 开始支持，低版本需做兼容处理。

> 最新的 nightly 版开发者工具开始支持，同时基础库从支持 npm 的版本（2.2.1）起支持

指定需要引用的扩展库。目前支持以下项目：

> + kbone: <a href="https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/extended/kbone/" class="FIXME:">多端开发框架</a>
>
> + weui: <a href="https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/extended/weui/" class="FIXME:">WeUI 组件库</a>

指定后，相当于引入了对应扩展库相关的最新版本的 npm 包，同时也不占用小程序的包体积。rc工具版本支持分包引用。用法如下：

```json
{
  "useExtendedLib": {
    "kbone": true,
    "weui": true
  }
}
```

#### entranceDeclare<a id="entranceDeclare">ㅤ</a>

> 微信客户端 7.0.9 及以上版本支持，iOS 暂不支持

聊天位置消息用打车类小程序打开，<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/location-message.html" class="FIXME:">详情参考</a>。

```json
"entranceDeclare": {
    "locationMessage": {
        "path": "pages/index/index",
        "query": "foo=bar"
    }
}
```

#### darkmode<a id="darkmode">ㅤ</a>

> 开发者工具 1.03.2004271 及以上版本支持，基础库 2.11.0 及以上版本支持

微信iOS客户端 7.0.12 版本、Android客户端 7.0.13 版本正式支持 DarkMode，可通过配置"darkmode": true表示当前小程序可适配 DarkMode，所有基础组件均会根据系统主题展示不同的默认样式，navigation bar 和 tab bar 也会根据开发者的配置自动切换。

配置后，请根据<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/ability/darkmode.html" class="FIXME:">DarkMode 适配指南</a>自行完成基础样式以外的适配工作。

```json
{
    "darkmode": true
}
```

#### themeLocation<a id="themeLocation">ㅤ</a>

自定义 <a href="https://developers.weixin.qq.com/miniprogram/dev/framework/ability/darkmode.html#变量配置文件-theme-json" class="FIXME:">theme.json</a> 的路径，当配置<code>"darkmode":true</code>时，当前配置文件为必填项。

```json
{
    "themeLocation": "/path/to/theme.json"
}
```

#### lazyCodeLoading<a id="lazyCodeLoading">ㅤ</a>

目前仅支持值 <code>requiredComponents</code>，代表开启小程序<a href="https://developers.weixin.qq.com/miniprogram/dev/framework/ability/lazyload.html#按需注入" class="FIXME:">「按需注入」</a>特性。

```json
{
    "lazyCodeLoading": "requiredComponents"
}
```

#### singlePage<a id="singlePage">ㅤ</a>

> 基础库 2.11.3 及以上版本支持，目前分享到朋友圈 (Beta) 后打开会进入单页模式

单页模式相关配置

|属性	|类型	|必填	|默认值	|描述|
|--|--|--|--|--|
|navigationBarFit	|String|	否|	默认自动调整，若原页面是自定义导航栏，则为 float，否则为 squeezed|	导航栏与页面的相交状态，值为 float 时表示导航栏浮在页面上，与页面相交；值为 squeezed 时表示页面被导航栏挤压，与页面不相交|

#### embeddedAppIdList<a id="embeddedAppIdList">ㅤ</a>

指定小程序可通过<a href="https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.openEmbeddedMiniProgram.html" class="FIXME:">wx.openEmbeddedMiniProgram</a>打开的小程序名单。

```python
{
    "embeddedAppIdList": ["wxe5f52902cf4de896"]
}
```

#### halfPage<a id="halfPage">ㅤ</a>

|属性|	类型|	必填|	默认值|	描述|
|--|--|--|--|--|
|firstPageNavigationStyle|	string|	否	|	|视频号直播打开的第一个页面的全屏状态使用自定义顶部，支持 default / custom|

```json
{
    "halfPage": {
        "firstPageNavigationStyle": "custom"
    }
}
```