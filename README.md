#### python基于高德地图Api实现租房

* 最近翻翻github上自己以前的项目（大家觉得好的话，可以留下你们的star 嘿嘿），并分享出来和大家一起学习，当时学习分布式爬虫，并写了一个基于高德地图Api实现租房，项目年久失修，但是我刚测试了一下，大体功能还在，只是可能相应的库有些已经退休

* 运行spider_main()，暂且支持地名：(北京 天津 大连 石家庄 哈尔滨 沈阳 太原 长春 威海 潍坊 呼和浩特 包头 上海 杭州 苏州 南京 无锡 济南 青岛 昆山 宁波 南昌 福州 合肥 徐州 淄博 深圳 广州 佛山 长沙 三亚 惠州 东莞 海口 珠海 中山 厦门 南宁 泉州 柳州 成都 重庆 武汉 郑州 西安 昆明 贵阳 兰州 洛阳 )

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020022917051642.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDI0MTQz,size_16,color_FFFFFF,t_70)

* 点击csvfile下的zufang.html之后显示的初始页面：图中为输入石家庄，石家庄的返回结果

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200229170528500.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDI0MTQz,size_16,color_FFFFFF,t_70)
* 选择已经爬取的文件

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200229170540277.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDI0MTQz,size_16,color_FFFFFF,t_70)

* 深色区域为一小时以内的车程：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200229170558260.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDI0MTQz,size_16,color_FFFFFF,t_70)

* 选择analysisfile文件夹下的svg文件可以直观地看出房价高低趋势：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200229170607286.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM5NDI0MTQz,size_16,color_FFFFFF,t_70)


[项目地址](https://github.com/wangjianxiandev/python-spider)
