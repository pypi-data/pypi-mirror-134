# Redj Captcha
Django / Rest Framework captcha
Safe, flexible and easy to use

## Getting Started

> in `setting.py`:

```
INSTALLED_APPS = [
    ...
    'redjcaptcha',
]
```

in terminal `python manage.py migrate`

> in `urls.py` :

```
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('redjcaptcha.urls')),
]
```
and check check `http://localhost:8000/captcha`

> check Captcha (django):
```
from redjcaptcha.setup import checkCaptcha

check = checkCaptcha(captcha_key, captcha_value)
if check==False:
    return 'inValid'
```
or use `fullCheckCaptcha` for check `ip` and `User-agent`
```
from redjcaptcha.setup import fullCheckCaptcha

check = fullCheckCaptcha(request)
if check==False:
    return 'inValid'
```

> check Captcha (rest_framework):
```
from rest_framework import serializers
from redjcaptcha.setup import checkCaptcha

class CaptchaSerializer(serializers.Serializer):
    captcha_key = serializers.CharField()
    captcha_value = serializers.CharField()

    def validate(self, data):
        check = checkCaptcha(data['captcha_key'], data['captcha_value'])
        if check==False:
            print('\n=====> Captcha faild')
            raise Exception()

        print('\n=====> Captcha success')
        return check
```

>if use `Redj Log` pakeg:
```
from redjcaptcha import redjlog

redjlog.fullCheckCaptcha(request)
```

> change default setting:
```
from redjcaptcha.setup import init

init(
    size=6, => count of word
    debug=True, => disable captcha
    font_size=50, => font size
    timeout=6000, => expire captcha after 6000s
    type="str-int", => type of captcha : int | str | str-int
    image_height=70, => image height
    image_weight=180, => image weight
    text_color="random", => text color (defualt random)
    pre_request_inVmin= 10, => max request in 5 minits
    background_color="#fff" => background image or #00000040
)
```