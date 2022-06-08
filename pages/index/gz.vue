<template>
	<view>
		<swiper class="swiperbox" :autoplay="true" :interval="3000" :duration="1000" :circular="true">
			<swiper-item class="swiperitem" v-for="(item,index) in resdata.banner" :key="index">
				<image class="swiperimg" :src="'https://wx.xu756.top/media/'+item.img"></image>
			</swiper-item>
		</swiper>
		<view class="fl_box">
			<view class="fl_c">
				<image src="../../static/icon/article.png"></image>
				<view class="text">
					文章
				</view>
			</view>
			<view class="fl_c">
				<image src="../../static/icon/cs.png"></image>
				<view class="text">
					测试
				</view>
			</view>
			<view class="fl_c">
				<image src="../../static/icon/kc.png"></image>
				<view class="text">
					课程
				</view>
			</view>
			<view class="fl_c">
				<image src="../../static/icon/fm.png"></image>
				<view class="text">
					FM
				</view>
			</view>
		</view>
		<view class="zj">
			<view class="zj_c">
				<image src="/static/icon/zj.png"></image>
				<view class="text">
					预约专家
				</view>
				<view class="m">
					深度解决你的问题
				</view>
			</view>
			<view class="zj_c">
				<image src="/static/icon/hone.png"></image>
				<view class="text">
					即时倾述
				</view>
				<view class="m">
					马上倾述你的烦恼
				</view>
			</view>
		</view>
		<view class="list">
			<view class="box" v-for="(item,index) in resdata.article" :key="index">
				<image class="img" :src="'https://wx.xu756.top/media/'+item.img"></image>
				<view class="right">
					<view class="title">
						{{item.title}}
					</view>
					<view class="note">
						{{item.note}}
					</view>
				</view>
			</view>
		</view>
	</view>
</template>
<script>
	var that
	export default {
		data() {
			return {
				resdata: {}
			}
		},
		created() {
			that=this
			uni.request({
				url: "https://wx.xu756.top/app/getdefault?id=1",
				success(res) {
					that.resdata = res.data

				}

			})

		},

	}
</script>

<style lang="scss">
	.swiperbox {
		padding-top: 20rpx;
		width: 100%;
		height: 300rpx;

		.swiperitem {
			width: 100%;
			height: 100%;

			.swiperimg {
				width: 680rpx;
				height: 100%;
				margin: 0 35rpx;
			}
		}
	}

	.fl_box {
		padding-top: 20rpx;
		width: 100%;
		display: flex;
		justify-content: space-around;
		align-items: center;

		.fl_c {
			width: 158rpx;
			background-color: aliceblue;
			height: 170rpx;

			image {
				width: 90rpx;
				height: 80rpx;
				margin: 15rpx 34rpx;
			}

			.text {
				text-align: center;
				font-size: 28rpx;
				font-weight: bold;
			}

		}


	}

	.zj {
		margin-top: 20rpx;
		display: flex;
		justify-content: space-around;

		.zj_c {
			width: 310rpx;
			padding: 20rpx;
			background-color: #ffffff;
			border-radius: 15rpx;

			image {
				float: right;
				width: 105rpx;
				height: 105rpx;
			}

			.text {
				font-size: 40rpx;
				font-weight: bold;
				text-align: center;
			}

			.m {
				font-size: 10rpx;
				padding-top: 5rpx;
				text-align: center;

			}

		}
	}

	.list {

		padding: 20rpx;
		float: left;

		.box {
			float: left;
			width: 100%;
			height: 200rpx;
		}

		.img {
			width: 180rpx;
			height: 160rpx;
			border-radius: 15rpx;
			float: left;
			margin-top: 1rpx
		}

		.right {
			width: 520rpx;
			height: 170rpx;
			float: right;

			.title {
				font-size: 30rpx;
				line-height: 35rpx;
				font-weight: bold;
				height: 70rpx;
				display: -webkit-box;
				-webkit-box-orient: vertical;
				-webkit-line-clamp: 2;
				overflow: hidden;
			}

			.note {
				margin-top: 10rpx;
				font-size: 18rpx;
				line-height: 30rpx;
				height: 90rpx;
				display: -webkit-box;
				-webkit-box-orient: vertical;
				-webkit-line-clamp: 3;
				overflow: hidden;
			}
		}

	}
</style>
