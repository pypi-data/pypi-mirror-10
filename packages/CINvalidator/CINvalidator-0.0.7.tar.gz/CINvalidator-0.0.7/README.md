# CIN-validator
China Citizen Identification (CIN) Number Validator

## Install

```
apt-get install -y python-pip
pip install CINvalidator
```

## Usage

```python
import CINvalidator

if CINvalidator.CINvalidator(441234197001011111):
    pass # Actions when the CIN is true.
else:
    pass # Actions when the CIN is false.

```

## References

- [最年长者 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B9%B4%E9%95%B7%E8%80%85)
- [GB 11643-1999 公民身份号码 - 维基文库，自由的图书馆](https://zh.wikisource.org/wiki/GB_11643-1999_%E5%85%AC%E6%B0%91%E8%BA%AB%E4%BB%BD%E5%8F%B7%E7%A0%81)
- [最新县及县以上行政区划代码（截止2014年10月31日）](http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201504/t20150415_712722.html)

## Contribution

- [Issue](https://github.com/imlonghao/CIN-validator/issues)
- [Pull Request](https://github.com/imlonghao/CIN-validator/pulls)

## License

Licensed under the Apache License, Version 2.0
