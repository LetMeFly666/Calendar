/*
 * @Author: LetMeFly
 * @Date: 2022-01-23 09:53:58
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-02-15 22:40:59
 */
const formatTime = date => {
    const year = date.getFullYear()
    const month = date.getMonth() + 1
    const day = date.getDate()
    const hour = date.getHours()
    const minute = date.getMinutes()
    const second = date.getSeconds()

    const formatNumber = n => {
        n = n.toString()
        return n[1] ? n : `0${n}`
    }

    return `${[year, month, day].map(formatNumber).join('-')} ${[hour, minute, second].map(formatNumber).join(':')}`
}

const LetMeFly_request = (parameter) => {
    /* 为request请求自动带上session */
    if (!parameter.header) {
        parameter.header = {};
    }
    parameter.header['cookie'] = wx.getStorageSync("sessionid");
    wx.request(parameter);
}

const Subscribe1Reminder = (then=null) => {
    /* 让用户订阅一个消息提醒 */
    const tmplIds = ["WQZmYqg7ZVhDXD5gZyC0VEMtuP2fDVgwcVrScV2mxu0"];
    wx.requestSubscribeMessage({
        tmplIds: tmplIds,
        success(msg) {
            console.log(msg);
            if (msg[tmplIds[0]] == "accept") {
                wx.showToast({
                    title: "订阅成功！",
                    icon: "success"
                });
            } else {
                wx.showToast({
                    title: "订阅失败",
                    icon: "error"
                });
            }
            if (then) {
                then();
            }
        },
        fail(msg) {
            wx.showToast({
              title: '订阅失败',
              icon: "error"
            });
        }
    });
}

module.exports = {
    formatTime,
    LetMeFly_request,
    Subscribe1Reminder
}

