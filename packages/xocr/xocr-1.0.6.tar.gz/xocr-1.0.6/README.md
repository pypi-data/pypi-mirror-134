[toc]

# 普通验证码

> 直接用ddddocr即可识别，如果有识别不了的可以提交

## 可支持

- 纯数字
- 英文+数字
- 数学运算

# 滑块验证码

> 从社区和群里了解目前只通过opencv就可以识别目标位置，特别是需要算出x距离，至于用户行为需要自己写

## 分类

### 淘宝滑块

> 可以通过js或者pymouse及pyautogui实现滑动

#### js代码

```javascript
event = document.createEvent('MouseEvents');
event.initEvent('mousedown', true, false);
document.querySelector("#nc_1_n1z").dispatchEvent(event);
event = document.createEvent('MouseEvents');
event.initEvent('mousemove', true, false);
Object.defineProperty(event, 'clientX', {
    get() {
        return 260;
    }
})
document.querySelector("#nc_1_n1z").dispatchEvent(event);
```

### 缺口滑块

```python
import hashlib

import cv2


def get_location(bg_file_path, fg_file_path=r'./files/images/aaa.png'):
    # 读取背景图片和缺口图片
    bg_img = cv2.imread(bg_file_path)  # 背景图片
    tp_img = cv2.imread(fg_file_path)  # 缺口图片
    # 识别图片边缘
    bg_edge = cv2.Canny(bg_img, 100, 200)
    tp_edge = cv2.Canny(tp_img, 100, 200)
    # 转换图片格式
    bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
    tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)
    # 缺口匹配
    res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
    # 绘制方框
    th, tw = tp_pic.shape[:2]
    tl = max_loc  # 左上角点的坐标
    br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
    cv2.rectangle(bg_img, tl, br, (0, 0, 255), 2)  # 绘制矩形
    hash_data = hashlib.md5((str(bg_file_path)).encode('utf8')).hexdigest()
    cv2.imwrite(f'../files/out_result/{hash_data}.jpg', bg_img)  # 保存在本地
    return max_loc
```

## 用户行为参考

### 慢->非常快->快->很慢