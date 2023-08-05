# SeleniumCommonSetting
## 常用的selenium-webdriver设置

## 更新
* 1.2.1
    * 修正在不添加Chromium_path参数时依然会使用Chromium的BUG。

* 1.2.0 2022/01/10
    * 增加添加user-agent功能
  
* 1.1.1 2021/12/28
    * 修正chromium拼写错误问题。
  
* 1.1.0 2021/12/28
    * 增加支持Chromnium。
    * 修改参数localdata_path默认值为'default'。
  
* 1.0.6 2021/11/21
    * 修改了名称为SeleniumCommonSetting，Class也修改为SeleniumCommonSetting。
  
* 1.0.5 2021/11/16
    * 对注释和部分参数名进行修改，减少使用时引用的参数错误。

## 介绍
常用的selenium webdriver chrome options配置项设置工具。

## 用例
```py

```

## 属性
* options: 根据设置的参数所返回的chrome_options。

## 参数
* localdata_path: 浏览器本地文件的地址，默认为None，可赋值'default'来导入本地文件的默认地址。
* extension_dir：存放浏览器插件的【文件夹地址】，默认为None，插件必须为打包好的crx格式，【不能】与无窗口模式同时使用。
* headless: 无窗口模式，默认为False。
* pic: 无图模式，默认为False。
* js: 不加载Javascript，默认为False。
* css：不加载CSS，默认为False。

