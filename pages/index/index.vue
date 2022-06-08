<template>
	<view class="mainbox">
		<view class="maintop" :style="'padding-top:'+h+'px;'">
			<uni-row>
				<uni-col :span="5">
					<view class="top_title">
						X心理
					</view>
				</uni-col>
				<uni-col :span="15">
					<uni-search-bar class="search" :focus="true" radius="20" @confirm="search" cancelButton="none">
					</uni-search-bar>
				</uni-col>
			</uni-row>
			<liuyuno-tabs :tabData="navlist" :defaultIndex="navactive" @tabClick='active_nav' />
			<view class="container_nav">
				<tj v-show="navactive==0"></tj>
				<gz v-show="navactive==1"></gz>
				<qq v-show="navactive==2"></qq>
				<zn v-show="navactive==3"></zn>
				<rjgx v-show="navactive==4"></rjgx>
			</view>
		</view>
		<view class="maincontainer">
		</view>

	</view>
</template>
<script>
	import liuyunoTabs from "@/components/liuyuno-tabs/liuyuno-tabs.vue";
	import tj from './tj.vue'
	import gz from './gz.vue'
	import qq from './qq.vue'
	import zn from './zn.vue'
	import rjgx from './rjgx.vue'
	export default {
		data() {
			return {
				MenuButton: {},
				name: 55,
				searchValue: '',
				navlist: [
					"推荐",
					"关注",
					"亲情",
					"子女",
					"人际关系"
				],
				navactive: 0,
				h: 50
			}
		},
		// 子组件
		components: {
			liuyunoTabs,
			tj,
			gz,
			qq,
			zn,
			rjgx

		},
		onReady() {
			// let h = uni.getMenuButtonBoundingClientRect().top - 10
			// this.h = h
		},
		methods: {
			// 搜索事件
			search(res) {
				console.log(res.value)
			},
			// 切换卡
			active_nav(index) {
				this.navactive = index

			},
			// 跳转页面
			NavTo(path) {
				uni.navigateTo({
					url: path
				})
			},
		}

	}
</script>

<style lang="scss">
	.mainbox {
		width: 750rpx;

		.maintop {
			height: 300rpx;
			background-image: linear-gradient(62deg, #8EC5FC 0%, #E0C3FC 100%);
			border-bottom-left-radius: 17%;
			border-bottom-right-radius: 17%;

			.top_title {
				padding: 10rpx 0;
				text-align: center;
				font-size: 48rpx;
				line-height: 95rpx;
				color: #007fdb;
			}

			.container_nav {
				width: 100%;

			}
		}

		.maincontainer {
			height: 300rpx;
		}
	}
</style>
