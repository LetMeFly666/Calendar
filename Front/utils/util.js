/*
 * @Author: LetMeFly
 * @Date: 2022-01-23 09:53:58
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-02-03 21:23:47
 */
const formatTime = date => {
    const year = date.getFullYear()
    const month = date.getMonth() + 1
    const day = date.getDate()
    const hour = date.getHours()
    const minute = date.getMinutes()
    const second = date.getSeconds()

    return `${[year, month, day].map(formatNumber).join('/')} ${[hour, minute, second].map(formatNumber).join(':')}`
}

const formatNumber = n => {
    n = n.toString()
    return n[1] ? n : `0${n}`
}

const LetMeFly_request = (parameter) => {
    /* 为request请求自动带上session */
    if (!parameter.header) {
        parameter.header = {};
    }
    parameter.header['cookie'] = wx.getStorageSync("sessionid");
    wx.request(parameter);
}

module.exports = {
    formatTime,
    LetMeFly_request
}

