from rest_framework.serializers import ModelSerializer

from .models import MyUser, UserProfile


# Serializers for MyUser model
class MyUserSerializer(ModelSerializer):

    class Meta:
        model = MyUser
        fields = "__all__"


    def get_fields(self):
        this_model_name = 'MyUser'
        fields = super().get_fields()

        exclude_fields_dictionary = self.context.get('exclude_fields', [])

        if exclude_fields_dictionary:
            exclude_fields = exclude_fields_dictionary.get(this_model_name, [])
            for field in exclude_fields:
                fields.pop(field, default=None)
        return fields


class MyUserSafeSerializer(ModelSerializer):

    class Meta:
        model = MyUser
        exclude = ['password']


class MyUserCustomSerializer(ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'email', 'username', 'first_name', 'last_name']


# Serializers for UserProfile model
class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserProfileSafeSerializer(ModelSerializer):
    user = MyUserCustomSerializer()

    class Meta:
        model = UserProfile
        fields = "__all__"