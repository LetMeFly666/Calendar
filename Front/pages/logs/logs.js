/*
 * @Author: LetMeFly
 * @Date: 2022-01-23 09:53:58
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-01-27 22:28:34
 */
// logs.js
const util = require('../../utils/util.js')

Page({
    data: {
        logs: []
    },
    onLoad() {
        this.setData({
            logs: (wx.getStorageSync('logs') || []).map(log => {
                return {
                    date: util.formatTime(new Date(log)),
                    timeStamp: log
                }
            })
        })
    }
})
