/*
 * @Author: LetMeFly
 * @Date: 2022-02-03 21:44:21
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-03-19 19:03:19
 */
// pages/myDiaries/myDiaries.js

import { LetMeFly_request } from "../../utils/util";

Page({

    /**
     * 页面的初始数据
     */
    data: {
        diaries: []
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        const _this = this;
        LetMeFly_request({
            url: 'https://diary.letmefly.xyz/GetAllDiaries/',
            success: function(msg) {
                const { diaries } = msg.data;
                _this.setData({
                    diaries: diaries.sort(function(a, b) {
                        return a.publishTime > b.publishTime ? -1 : 1;
                    })
                }); 
            }
        });
        // this.setData({diaries: ["4545", "6545"]})
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