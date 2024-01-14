from rest_framework import serializers


# from rest_framework_simplejwt.serializers import

class _PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs) -> None:
        kwargs.setdefault("style", {})

        kwargs["style"]["input_type"] = "password"
        kwargs["write_only"] = True

        super().__init__(*args, **kwargs)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = _PasswordField()
    device_id = serializers.CharField()
