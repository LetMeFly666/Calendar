/*
 * @Author: LetMeFly
 * @Date: 2022-02-03 21:35:46
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-02-03 22:27:09
 */
// pages/addDiary/addDiary.js

import { LetMeFly_request } from "../../utils/util";

Page({

    AddDiarys(e) {

        LetMeFly_request({
            url: 'https://diary.letmefly.xyz/AddADiary/',
            data: {
                "content": this.data.content
            },
            dataType: 'json',
            method: "POST",
            success: function() {
                wx.navigateTo({
                    url: '/pages/myDiaries/myDiaries',
                });
            }
        });
    },

    fakeFunction(e) {
        
    },

    /**
     * 页面的初始数据
     */
    data: {
        content: ""
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {

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