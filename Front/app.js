/*
 * @Author: LetMeFly
 * @Date: 2022-01-23 09:53:58
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-02-13 17:28:15
 */
// app.js
import { LetMeFly_request } from "./utils/util";

const LetMeFly_realLogin = () => {
    wx.login({
        success(msg) {
            if (msg.code) {
                // 发起网络请求
                LetMeFly_request({
                    url: 'https://diary.letmefly.xyz/login/',
                    data: {
                        code: msg.code
                    },
                    success(msg) {
                        // function getSessionid() {
                        //     const datas = msg.cookies[0].split("; ");
                        //     for(let i = 0; i < datas.length; i++) {
                        //         const prefix = datas[i].split("=");
                        //         if (prefix[0] == "sessionid") {
                        //             return prefix[1];
                        //         }
                        //     }
                        // }
                        // console.log(getSessionid());
                        wx.setStorageSync("sessionid", msg.header["Set-Cookie"]);
                        console.log("登录成功！");
                    }
                });
            }
            else {
                console.log("登录失败！" + msg.errMsg);
            }
        }
    });
}

App({
    onLaunch() {
        // 展示本地存储能力
        const logs = wx.getStorageSync('logs') || []
        logs.unshift(Date.now())
        wx.setStorageSync('logs', logs)

        // 登录
        LetMeFly_realLogin();
    },
    globalData: {
        userInfo: null
    },
})
