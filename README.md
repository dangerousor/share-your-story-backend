# share-your-story-backend
时隔几个月，得个空闲。年前、年后都在忙着写公司的关于年会活动的抽奖项目，大家辛辛苦苦加班2个月完成的项目，领导们在年会上，临时决定不用了....虽然没觉得怎样，但写这篇博客，突然想到，就说了。


----------
回归正题：
	

**1. 为什么要做这个？**

答：女朋友即将毕业（计算机系），希望我帮忙写个网站，就是关于大学生二手交易平台的。由于我的体贴（不做怕被揍）、善良的心便答应了。刚好趁此机会，巩固一下毕业8个月来这个公司所学的知识。

**2. 平台的内容是什么？**

答： 其实也相当于需求啦，鉴于时间、空间、人力、物力等等各方面的因素，我们不可能真正的实地调研。于是靠着我和她两个人的大脑，完成了需求分析，俗话说三个臭皮匠顶个诸葛亮（虽然还差一个人-。-）。
网站主题呢，不在于二手交易，而是注重于物品的故事。“分享记忆”（之后简称“享忆”）这个平台面向的大学生，尤其是那些即将毕业的。他/她有许多东西带不走但是比较重要或者说围绕着这个东西，有许许多多开心或者是难过的故事。我们希望他/她能通过我们这个平台，把这件东西的故事分享给其他人。“享忆”不支持在线支付，所希望的就是交易双方通过线下的方式，大家找个相对安静的地方，好好聊聊，说不定能成为好朋友。“享忆”是区分学校的，意思就是，交易双方为同一所学校。
所以，“享忆”的主旨在于分享故事，结交朋友，二手物品出售只是其中的一项功能。

**3. 平台的完成度？实现了什么功能？**

答：只能说时间紧迫，用时两周，只完成了一个普通二手交易平台所具备的功能。包括（用户注册、用户登录、商品浏览、发布商品、收藏商品，上/下架商品， 搜索商品......），真正的主旨完全没有体现，希望之后能够一步步完善，最终达到我们的预期。

**4. 平台的表结构**

![这里写图片描述](https://img-blog.csdn.net/20180421144128283?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0lUVDEzMDIx/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**5. 使用**

使用PyCharm编辑器
pip install -r requirements.txt

**6. 遇到的问题**

1. 使用django的Token 

  1.1 需要在INSTALL_APP中添加'rest_framework.authtoken',
  1.2 执行migrate authtoken


2 django的Token Authentication使用需要配置在settings中

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
目的是为了告诉django我们使用token认证方案，这样在request.user就不会是匿名用户


3 继承django 的AbstractUser，username需要添加unique=True,不然会报错，但可以在settings中添加 SILENCED_SYSTEM_CHECKS = ["auth.W004"]，忽略该错误


4 在用postman去请求django rest api时，出现403 forbidden

  4.1 解决办法一，在settings中的MIDDLEWARE注释掉'django.middleware.csrf.CsrfViewMiddleware'
  
  4.2 解决办法二，发送请求的时候，获取cookie中的csrftoken,并将该值以key为X-CSRFToken,放在request的header中


5 django restframework 分页需要在REST_FRAMEWORK中配置
    自定义了分页规则
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPaginationEx',
    'PAGE_SIZE': 10,
