/*
 * @Author: LetMeFly
 * @Date: 2022-01-23 09:53:58
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-01-26 21:06:43
 */
// app.js
App({
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
  },
  globalData: {
    userInfo: null
  },
})
