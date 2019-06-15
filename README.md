# 光伏组件短路 & 明暗片检测

## 需求背景

- 太阳能电池片是以半导体材料为基础的具有能量转换功能的半导体器件，是太阳能光伏发电最核心的器件，按照原材料结构分为硅电池片（单晶/多晶）、薄膜电池片、化合物电池片；多个单体太阳能电池片互联封装后成为组件。

- 生产过程中通过电致发光生成EL图像可以有效发现电池片、串联、焊接等环节存在的问题，目前组件的EL缺陷检测主要由人工目视完成，费时费力。

- **短路**：组件单串进行焊接时出现短路，在EL图像上呈现**电池片或电池串为黑色**

  ![短路](https://github.com/dc-ley/guangfudl/blob/master/figures/11812110500912.jpg)

- **明暗片**：同一组件的电池片之间存在明暗差异不一致的现象

  ![明暗片](https://github.com/dc-ley/guangfudl/blob/master/figures/441402I1321688.jpg)

- PERC 电池以按照**灰度尺**（国家标准灰度尺）

  ![灰度尺](https://github.com/dc-ley/guangfudl/blob/dev/figures/灰度尺.png)

  

## 数据

一张组件的分段图片

![分段1](https://github.com/dc-ley/guangfudl/blob/master/figures/sample1.jpg)

![分段2](https://github.com/dc-ley/guangfudl/blob/master/figures/sample2.jpg)

![分段3](https://github.com/dc-ley/guangfudl/blob/master/figures/sample3.jpg)

## 算法思路

### 明暗片

1. 将图片进行切割，然后对每一块电池片进行操作，取该电池片的像素中位数来代表该电池片的灰度等级。
2. 依次得到每段图的结果，再合在一起分析，取整个组件电池片的中位数，然后与中位数差值大于某个阈值（作为一个参数，可调节）的认为是暗片，将其标记出来。

### 短路

思路基本和明暗片相同，也是切割后统计电池片灰度，然后设定一个灰度阈值，大于这个阈值的认为是黑色（短路），将其标记出来。
