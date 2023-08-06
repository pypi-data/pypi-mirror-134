import uuid
from django.db import models
from datetime import timedelta
from django.utils import timezone
from .management.setting import Base
from .management.helper import randomString


class RedjCaptchaModel(models.Model):
    id = models.UUIDField(
        unique=True,
        editable=False,
        primary_key=True,
        default=uuid.uuid4,
    )
    text = models.CharField(max_length=12)
    request_ip = models.CharField(null=True, max_length=40)
    user_agent = models.CharField(null=True, max_length=250)
    created_by = models.UUIDField(null=True, editable=False)
    request_host = models.CharField(null=True, max_length=250)
    deleted_at = models.DateTimeField(null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-created_at']
        db_table = "redj_captchas"

    def __str__(self):
        return str(self.id)

    def create(request):
        set_int = True
        set_str = True
        if Base.type == "str":
            set_str = True
            set_int = False
        if Base.type == "int":
            set_int = True
            set_str = False

        user_agent = request.headers.get('User-Agent', "empty")
        expier_at = timezone.now() - timedelta(minutes=5)
        chack_count = RedjCaptchaModel.objects.filter(
            user_agent=user_agent,
            created_at__gte=expier_at,
            request_ip=request.META['REMOTE_ADDR'],
            request_host=request.META['HTTP_HOST'],
        ).count()
        if chack_count > Base.pre_request_inVmin:
            return None

        text = randomString(Base.size, set_int=set_int, set_str=set_str)
        model = RedjCaptchaModel.objects.create(
            text=text,
            user_agent=user_agent,
            request_ip=request.META['REMOTE_ADDR'],
            request_host=request.META['HTTP_HOST']
        )
        return model

    def checkCaptcha(key, value, request=None):
        try:
            expier_at = timezone.now() - timedelta(seconds=int(Base.timeout))
            filter = {
                "id": key,
                "text": value,
                "deleted_at": None,
                "created_at__gte": expier_at
            }
            if request != None:
                user_agent = request.headers.get('User-Agent', "empty")
                filter["user_agent"] = user_agent
                filter["request_ip"] = request.META['REMOTE_ADDR']
                filter["request_host"] = request.META['HTTP_HOST']
            model = RedjCaptchaModel.objects.filter(**filter)
            if len(model) > 0:
                RedjCaptchaModel.objects.filter(
                    **filter
                ).update(deleted_at=timezone.now())
                return True
        except:
            pass

        return False
