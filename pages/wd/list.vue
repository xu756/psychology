<template>
	<view>
		<view class="box">
			<image class="user" src="https://ossimg.xinli001.com/20220410/18714a9d8f86143a257741bd2bfa17c5.png!80"
				mode="">
			</image>
			<view class="t1">
				匿名用户
			</view>
			<view class="t2">
				18小时前
			</view>
			<view class="p1">
				我觉得我们高于友情却不低于爱情，男女之间有纯友谊吗
			</view>
			<view class="p2">
				我和他是异性之间的闺蜜，我对他好像有好感，但是他有自己喜欢的人。前天（5月20日）他找我要礼物，说要杯子，我开始没有答应，就问他为什么要杯子不要别的？他说杯子-辈子，我们俩要一辈子。我听完说真的有点触动了但还是没有答应，他磨了我好久，我最终还是答应。我不知道他喜不喜欢我，但是他在细节方面我有时感觉他喜欢我，有时又觉得只是友情。他曾说过至死不渝的友情胜过敷衍的爱情。我觉得我们的感情高于友情却不低于爱情。我还能继续喜欢他吗？
			</view>
			<view class="p3">
				4个回答
			</view>
		</view>
		<view class="box">
			<image class="user" src="https://ossimg.xinli001.com/20220410/18714a9d8f86143a257741bd2bfa17c5.png!80"
				mode="">
			</image>
			<view class="t1">
				匿名用户
			</view>
			<view class="t2">
				18小时前
			</view>
			<view class="p1">
				我觉得我们高于友情却不低于爱情，男女之间有纯友谊吗
			</view>
			<view class="p2">
				我和他是异性之间的闺蜜，我对他好像有好感，但是他有自己喜欢的人。前天（5月20日）他找我要礼物，说要杯子，我开始没有答应，就问他为什么要杯子不要别的？他说杯子-辈子，我们俩要一辈子。我听完说真的有点触动了但还是没有答应，他磨了我好久，我最终还是答应。我不知道他喜不喜欢我，但是他在细节方面我有时感觉他喜欢我，有时又觉得只是友情。他曾说过至死不渝的友情胜过敷衍的爱情。我觉得我们的感情高于友情却不低于爱情。我还能继续喜欢他吗？
			</view>
			<view class="p3">
				4个回答
			</view>
		</view>
	</view>
</template>
<script>
	export default {
		data() {
			return {

			}
		},

	}
</script>
<style lang="scss">
	.box {
		float: left;
		margin: 18rpx;
		width: 714rpx;
		position: relative;
		height: 520rpx;
		border-radius: 15rpx;
		background-color: #fff;
		box-shadow:
			inset 0 -3em 3em rgba(0, 0, 0, 0.1),
			0 0 0 2px rgb(255, 255, 255),
			0.3em 0.3em 1em rgba(0, 0, 0, 0.3);


		.user {
			position: absolute;
			left: 20rpx;
			width: 80rpx;
			height: 80rpx;
			border-radius: 50%;
		}

		.t1 {
			position: absolute;
			left: 120rpx;
			top: 20rpx;
			font-size: 30rpx;
		}

		.t2 {
			position: absolute;
			right: 30rpx;
			top: 20rpx;
			font-size: 26rpx;
		}

		.p1 {
			position: absolute;
			left: 10rpx;
			top: 90rpx;
			font-size: 35rpx;
			line-height: 60rpx;
			font-weight: bold;
		}

		.p2 {
			position: absolute;
			left: 10rpx;
			right: 10rpx;
			top: 220rpx;
			display: -webkit-box;
			-webkit-box-orient: vertical;
			-webkit-line-clamp: 5;
			overflow: hidden;
		}

		.p3 {
			position: absolute;
			right: 10rpx;
			top: 460rpx;
			color: #00BCD4;
		}
	}
</style>
