/*
 * @Author: LetMeFly
 * @Date: 2022-01-26 20:05:20
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-02-14 20:50:21
 */
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
        wx.requestSubscribeMessage({
            tmplIds: ["WQZmYqg7ZVhDXD5gZyC0VEMtuP2fDVgwcVrScV2mxu0"],
            success(msg) {
                console.log(msg);
            },
            fail(msg) {
                wx.showToast({
                  title: '订阅失败',
                  icon: "error"
                })
            }
        });
    }
})


// Page({

//     /**
//      * 页面的初始数据
//      */
//     data: {

//     },

//     /**
//      * 生命周期函数--监听页面加载
//      */
//     onLoad: function (options) {

//     },

//     /**
//      * 生命周期函数--监听页面初次渲染完成
//      */
//     onReady: function () {

//     },

//     /**
//      * 生命周期函数--监听页面显示
//      */
//     onShow: function () {

//     },

//     /**
//      * 生命周期函数--监听页面隐藏
//      */
//     onHide: function () {

//     },

//     /**
//      * 生命周期函数--监听页面卸载
//      */
//     onUnload: function () {

//     },

//     /**
//      * 页面相关事件处理函数--监听用户下拉动作
//      */
//     onPullDownRefresh: function () {

//     },

//     /**
//      * 页面上拉触底事件的处理函数
//      */
//     onReachBottom: function () {

//     },

//     /**
//      * 用户点击右上角分享
//      */
//     onShareAppMessage: function () {

//     }
// })