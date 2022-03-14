/*
 * @Author: LetMeFly
 * @Date: 2022-01-26 20:05:20
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-02-14 21:53:29
 */
import { Subscribe1Reminder } from "../../utils/util";

Page({

    GotoAddDiaryPage(e) {
        wx.navigateTo({
            url: '/pages/addDiary/addDiary',
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