try:
    import redjlog
    from .management.setting import Base
    from .models import RedjCaptchaModel

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
            raise redjlog.OtherException("Captcha inValid")
        checkModel= RedjCaptchaModel.checkCaptcha(key, value, request)
        if checkModel:
            return True
        raise redjlog.OtherException("Captcha inValid")
except:
    pass