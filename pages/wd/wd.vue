<template>
	<view>
		<swiper class="swiperbox" :autoplay="true" :interval="3000" :duration="1000" :circular="true"
			previous-margin="50rpx" next-margin="25rpx">
			<swiper-item class="swiperitem" v-for="(item,index) in resd.banner" :key="index">
				<image class="swiperimg" :src="'https://wx.xu756.top/media/'+item.img"></image>
			</swiper-item>
		</swiper>
		<uni-notice-bar style="margin: 20rpx 0; " showIcon scrollable single text="《父母的羁绊》｜原生家庭的痛，只能由你自己来治愈">
		</uni-notice-bar>
		<view class="fl_box">
			<view class="card">
				<view class="p1">
					专家面对面
				</view>
				<view class="p2">
					专家定时为你解惑
				</view>
			</view>
			<view class="card">
				<view class="p1">
					问答精选
				</view>
				<view class="p2">
					各类问题的精选回答
				</view>
			</view>
		</view>

		<view class="dropdown">
			<ren-dropdown-filter :filterData='filterData' :defaultIndex='defaultIndex' @ed='ed'
				@dateChange='dateChange'></ren-dropdown-filter>
		</view>
		<listwd></listwd>
	</view>
</template>
<script>
	import RenDropdownFilter from '@/components/ren-dropdown-filter/ren-dropdown-filter.vue'
	import listwd from './list.vue'
	var that
	export default {
		components: {
			RenDropdownFilter,
			listwd
		},
		data() {
			return {
				resd: {},
				filterData: [
					[{
						text: '全部分类',
						value: ''
					}, {
						text: '家庭关系',
						value: 1
					}, {
						text: '爱情',
						value: 2
					}, {
						text: '友谊',
						value: 3
					}],
					[{
						text: '综合排序',
						value: ''
					}, {
						text: '按时间排序',
						value: 1
					}, {
						text: '按热度排序',
						value: 2
					}]
				],
				defaultIndex: [0, 0]
			}
		},
		onLoad() {
			that = this
			this.getdefault()
		},
		methods: {
			getdefault() {
				uni.request({
					url: "https://wx.xu756.top/app/getdefault?id=6",
					success(res) {
						that.resd = res.data
					}
				})
			},
			ed(res) {
				console.log(res)
			},
			dateChange(d) {
				uni.showToast({
					icon: 'none',
					title: d
				})
			}

		}
	}
</script>
<style lang="scss">
	.swiperbox {
		width: 750rpx;
		height: 300rpx;

		.swiperitem {

			.swiperimg {
				width: 650rpx;
				height: 100%;
				border-radius: 15rpx;
			}
		}

	}

	.fl_box {
		width: 100%;
		display: flex;
		justify-content: space-around;

		.card {
			width: 45%;
			height: 150rpx;
			background-color: #03A9F4;
			text-align: center;
			border-radius: 20rpx;

			.p1 {
				font-size: 40rpx;
				line-height: 85rpx;
				font-weight: 600;
				color: #FFFFFF;
			}

			.p2 {
				color: #B3E5FC;
			}

		}

	}

	.dropdown {
		width: 100%;
		height: 108rpx;
		float: left;
		
	}
</style>
