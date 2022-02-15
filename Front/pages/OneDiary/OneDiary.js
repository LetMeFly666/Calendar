/*
 * @Author: LetMeFly
 * @Date: 2022-02-15 22:44:24
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-02-15 23:53:55
 */
// pages/OneDiary/OneDiary.js
import { LetMeFly_request} from "../../utils/util";

Page({

    deleteThisDiary(e) {
        const _this = this;

        wx.showModal({
            title: "警告",
            content: "确认删除吗",
            success(result) {
                if (result.confirm) {
                    LetMeFly_request({
                        url: 'https://diary.letmefly.xyz/Del1Diary/',
                        data: {
                            diaryId: _this.data.id
                        },
                        dataType: 'json',
                        method: "POST",
                        success(msg) {
                            wx.showToast({title: "删除请求已发出"});
                            setTimeout(() => {
                                wx.navigateTo({
                                    url: '/pages/myDiaries/myDiaries'
                                });
                            }, 500);
                        }
                    });
                } else {
                    console.log("取消删除");
                }
            }
        })
    },

    /**
     * 页面的初始数据
     */
    data: {
        id: "",
        content: "",
        publishTime: "",
        remindTime: ""
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        this.setData({
            id: this.options.id
        });

        const _this = this;

        LetMeFly_request({
            url: 'https://diary.letmefly.xyz/Get1Diary/',
            data: {
                diaryId: _this.data.id
            },
            dataType: 'json',
            method: "POST",
            success: function(msg) {
                const data = msg.data;
                _this.setData({
                    content: data.diary.content,
                    publishTime: data.diary.publishTime.replace("T", " "),  // 我也不知道为啥是个T
                    remindTime: data.diary.remindTime ? data.diary.remindTime.replace("T", " ") : data.diary.remindTime
                });
            }
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