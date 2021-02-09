

Read an Image through matplotlib

```bash
import matplotlib.pyplot as plt
```



```bash

from scipy import misc,ndimage
face = misc.face()
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=5)#Results
plt.imshow(<image to be displayed>)


```



Adapted from https://towardsdatascience.com/image-manipulation-tools-for-python-6eb0908ed61f
