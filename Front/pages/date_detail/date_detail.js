/*
 * @Author: LetMeFly
 * @Date: 2022-01-26 20:05:20
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-03-14 19:45:33
 */
import { Subscribe1Reminder } from "../../utils/util";

Page({

    data: {
        date: ""
    },

    onLoad: function (options) {
        this.setData({
            date: this.options.date
        });
    },

    GotoAddDiaryPage(e) {
        wx.navigateTo({
            url: '/pages/addDiary/addDiary?date=' + this.data.date,
        })
    },

    GotoMyDiariesPage(e) {
        wx.navigateTo({
            url: '/pages/myDiaries/myDiaries',
        })
    },

    SubscribeAReminder(e) {
        Subscribe1Reminder();
    }
})