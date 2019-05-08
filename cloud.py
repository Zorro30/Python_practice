from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

text = "Hello Gaurang Engg want to learn coding and do something great with it numpy share lists fork thread ML AI Logic \
        BeautifulSoup Cool Python3"

our_mask = np.array(Image.open('twitter.png'))

cloud = WordCloud(background_color="white", mask=our_mask).generate(text)

plt.imshow(cloud)
plt.axis('off')
plt.show()  