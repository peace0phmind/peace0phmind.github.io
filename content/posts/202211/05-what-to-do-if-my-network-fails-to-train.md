---
title: "What to Do if My Network Fails to Train"
description: "05-what-to-do-if-my-network-fails-to-train"
keywords: "fails,train"

date: 2022-11-20T11:22:00+08:00
lastmod: 2022-11-20T11:22:00+08:00

author: peace0phmind
url: "posts/202211/05-what-to-do-if-my-network-fails-to-train"

draft: true

categories:
  -
tags:
  - fails
  - train

---

## 机器学习的一般步骤

```markmap
---
markmap:
  maxWidth: 300
  colorFreezeLevel: 3
  initialExpandLevel: 4
---

# loss on training data

## large
- model bias
  - make your model complex
- optimization

## small
- loss on testing data
  - large
    - overfitting
      - more training data
      - data augmentation
      - make your model simpler
    - mismatch
  - small :blush:
  
## model complex trade-off(权衡)
- Split your training data into training set and validation set for model selection

```

## Reference Video


{{< youtube WeHM2xpYQpw >}}
{{< youtube QW6uINn7uGk >}}
{{< youtube zzbr1h9sF54 >}}
{{< youtube HYUXEeh3kwY >}}
{{< youtube O2VkP8dJ5FE >}}

{{< youtube _j9MVVcvyZI >}}

{{< youtube 1_HBTJyWgNA >}}
{{< youtube 4pUmZ8hXlHM >}}
{{< youtube e03YKGHXnL8 >}}