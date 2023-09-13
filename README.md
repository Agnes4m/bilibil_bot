<!-- markdownlint-disable MD026 MD031 MD033 MD036 MD041 MD046 MD051 -->
<div align="center">
  <img src="https://raw.githubusercontent.com/Agnes4m/nonebot_plugin_l4d2_server/main/image/logo.png" width="180" height="180"  alt="AgnesDigitalLogo">


# bilibil_live(b站直播弹幕互动)

</div>

## 介绍

b站直播间弹幕获取，并且可用于

## 开发环境

系统: win10家庭版

python: 3.11.4

## 配置

当前文件夹下`config.yml`文件,填入相关参数

- SESSDATA: b站cookie中相应字段，在浏览器中登录后f12获取
- TEST_ROOM_IDS: list对象，为监听的直播间号（不是个人首页，是直播间号）

## 启动

> 使用`pdm install`或者`poetry install`安装依赖
>
> 双击bat文件

## 其他

- [blivecaht(直播弹幕的库)](https://github.com/xfgryujk/blivedm/) - 源代码来自这个项目
