/*
 * @Author: LetMeFly
 * @Date: 2022-02-03 21:35:46
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-03-14 19:55:08
 */
// pages/addDiary/addDiary.js

import { LetMeFly_request, Subscribe1Reminder } from "../../utils/util";

Page({

    AddDiarys(e) {
        const getData = () => {
            const data = {
                "content": this.data.content
            };
            if (this.data.remindTime_Hour) {
                data["remindTime"] = this.data.remindTime + " " + this.data.remindTime_Hour;
            }
            return data;
        }

        if (!(this.data.content)) {
            wx.showToast({
              title: '请输入日记内容',
              icon: 'error'
            });
            return ;
        }

        function sendAndJump() {
            LetMeFly_request({
                url: 'https://diary.letmefly.xyz/AddADiary/',
                data: getData(),
                dataType: 'json',
                method: "POST",
                success: function(msg) {
                    wx.navigateTo({
                        url: '/pages/myDiaries/myDiaries',
                    });
                }
            });
        }

        if (this.data.remindTime_Hour) {
            Subscribe1Reminder(sendAndJump);
        } else {
            sendAndJump();
        }
    },

    fakeFunction(e) {
        
    },

    /**
     * 页面的初始数据
     */
    data: {
        content: "",
        remindTime: "2022-2-15",
        remindTime_Hour: ""
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        this.setData({
            remindTime: this.options.date
        });
    },

    /**
     * 生命周期函数--监听页面初次渲染完成
     */
    onReady: function () {

    },

    /**
     * 生命周期函数--监听页面显示
     */
    onShow: function () {
        this.setData({
            content: ""
        });
    },

    /**
     * 生命周期函数--监听页面隐藏
     */
    onHide: function () {

    },

    /**
     * 生命周期函数--监听页面卸载
     */
    onUnload: function () {

    },

    /**
     * 页面相关事件处理函数--监听用户下拉动作
     */
    onPullDownRefresh: function () {

    },

    /**
     * 页面上拉触底事件的处理函数
     */
    onReachBottom: function () {

    },

    /**
     * 用户点击右上角分享
     */
    onShareAppMessage: function () {

    }
})