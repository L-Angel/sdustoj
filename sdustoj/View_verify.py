from DjangoCaptcha import Captcha
import random
def code(request):
    ca=Captcha(request)
    figures = [2,3,4,5,6,7,8,9]
    ca.words = [''.join(str(random.sample(figures,1)[0]) for i in range(0,4))]
    ca.type= 'word'
    ca.img_height = 30
    ca.img_width = 100
    return ca.display()