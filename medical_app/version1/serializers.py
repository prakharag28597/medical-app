from rest_framework import serializers

# -------------------- Serializer & Type ----------------------------
# regarding user registration--------------------------------->>>>>>
class UserDetailType(object):
    def __init__(self, email, password, name,
                    gender, date_of_birth, contact_number,  **kwargs):
        self.email = email
        self.password = password
        self.name = name
        self.gender = gender
        self.date_of_birth=date_of_birth
        self.contact_number=contact_number

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class UserDetailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=25)
    password = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=35)
    contact_number = serializers.IntegerField()
    gender = serializers.CharField()
    date_of_birth = serializers.DateTimeField()

    def create(self, validated_data):
        return UserDetailType(**validated_data)

# -------------------- Response Serializer & Type Class----------------------------
# -------------------- regarding user id
class UserIdType(object): # Type class
    def __init__(self, id,  **kwargs):
        self.id = id

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class UserIdSerializer(serializers.Serializer): # Serializer
    id = serializers.IntegerField()

    def create(self, validated_data):
        return UserIdType(**validated_data)

# regarding user login------------------------------------>>>>

class LoginDetailType(object):
    def __init__(self, email, password, **kwargs):
        self.email = email
        self.password = password

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __getitem__(self, item):
        return getattr(self, item)


class LoginDetailSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=25)
    password = serializers.CharField(max_length=10)

    def create(self, validated_data):
        return UserDetailType(**validated_data)



