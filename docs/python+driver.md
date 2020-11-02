# python + driver的集成环境部署


> 完整教程
* https://blog.csdn.net/weixin_39318540/article/details/80790680

> 本地Chrome Version  
* 83.0.4103.97

> Chrome Driver 下载地址:
 * http://npm.taobao.org/mirrors/chromedriver/(淘宝源)
 * http://chromedriver.storage.googleapis.com/index.html

> selenium之 chromedriver与chrome版本映射表：
 * https://blog.csdn.net/huilan_same/article/details/51896672




## 报错处理

* 1、ModuleNotFoundError: No module named 'selenium'

    → pip install selenium

    × 安装报错

    WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)'))': /simple/selenium/

    ? 解决方案推荐 

    https://blog.csdn.net/lsf_007/article/details/87931823

    核心命令
    ```
    pip install selenium -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
    ```


    √ 安装成功

* 2、selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. 

    ＋ 将chromedriver.exe拷贝至谷歌浏览器目录（如 C:\Program Files\Google\Chrome\Application）
以及python根目录（C:\Python27）

    ＋ 将谷歌浏览器环境变量添加到path（C:\Users\HD003\AppData\Local\Google\Chrome\Application）

    →  参考方案地址

    https://blog.csdn.net/weixin_41990913/article/details/90936149

    √ 解决
