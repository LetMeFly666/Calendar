/*
 * @Author: LetMeFly
 * @Date: 2022-01-26 20:05:20
 * @LastEditors: LetMeFly
 * @LastEditTime: 2022-03-14 19:39:50
 */
import { Subscribe1Reminder } from "../../utils/util";

Page({
    data: {
        dayStyle: [
          {month: 'current', day: new Date().getDate(), color: 'red', background: '#00CDCD'},
          { month: 'current', day: new Date().getDate(), color: 'white', background: '#00CDCD' }
        ],
      },
      
     
      //给点击的日期设置一个背景颜色
      dayClick:
  
        /*wx.setNavigationBarColor({
          backgroundColor: 'backgroundColor',
          frontColor: 'frontColor',
        }),*/
  
        function (event) {
            const year = event.detail.year;
            const month = event.detail.month;
            const day = event.detail.day;
            const changeBgColor = `dayStyle[0].color`;
            const changeBg = `dayStyle[0].background`;
            const changeDay = `dayStyle[1].day`;
            const changeEndBg = `dayStyle[1].background`;
        
            this.setData({
                [changeDay]: day,
                [changeBg]:"rgba(255,255,255,0)",
                [changeBgColor]:"red",
                [changeEndBg]: "#00CDCD"
            })

            wx.navigateTo({
                url: '/pages/date_detail/date_detail?date=' + year + '-' + month + '-' + day,
            })
  
        },
  
    onLoad: function () { },

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