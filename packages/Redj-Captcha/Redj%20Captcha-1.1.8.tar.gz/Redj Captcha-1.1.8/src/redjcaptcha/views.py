from .models import RedjCaptchaModel
from .management.setting import Base
from django.http import JsonResponse
from .management.helper import generateImage


def getCaptcha(request):
    model = RedjCaptchaModel.create(request)
    if model == None:
        return JsonResponse({
            "status": 500,
            "data": None,
            "message": f"Up to {Base.pre_request_inVmin} requests in 5 minutes"
        }, status=500)

    image = generateImage(model.text)
    return JsonResponse({
        "status": 200,
        "data": {
            "key": model.id,
            "timeout": Base.timeout,
            "created_at": model.created_at,
            "image": image,
        }
    })


def checkCaptcha(key, value, request=None):
    if Base.debug == True:
        return True
    return RedjCaptchaModel.checkCaptcha(key, value, request)


def fullCheckCaptcha(request):
    if Base.debug == True:
        return True
    key = None
    value = None
    if request.method == 'GET':
        key = request.GET.get('captcha_key')
        value = request.GET.get('captcha_value')
    elif request.method == 'POST':
        key = request.POST.get('captcha_key')
        value = request.POST.get('captcha_value')

    if key == None or value == None:
        return False
    return RedjCaptchaModel.checkCaptcha(key, value, request)
