<script>
export default {
  name: "FullscreenBackground",
};
</script>

<template>
  <div class="fullscreen-background"></div>
</template>

<style scoped>
/* 确保背景填满整个视口 */
.fullscreen-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("/img/natsumeai_20250909_004320.jpg");
  background-size: cover; /* 确保背景图片覆盖整个屏幕 */
  background-position: center center;
  background-repeat: no-repeat;
  z-index: -1; /* 保证背景在最底层 */
}
.content {
  position: relative;
  z-index: 1; /* 保证内容在背景之上 */
  color: white;
  text-align: center;
  padding: 20px;
}
</style>
