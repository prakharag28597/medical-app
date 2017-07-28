from rest_framework.decorators import api_view
from rest_framework.response import Response

# --------------------------------------Sign up API---------------------------------------------

@api_view(['POST'])
def create_user(request):
    # get user_type object
    from .serializers import UserDetailSerializer
    # validations
    user_detail_serializer = UserDetailSerializer(data=request.data)
    if not user_detail_serializer.is_valid():
        return Response(status=400, data=user_detail_serializer.errors)

    # user detail object is created once save() is called
    user_type_object = user_detail_serializer.save()
    # check if that email already exists or not if yes return status 401
    from version1.models import UserDetail
    try:
        UserDetail.objects.get(email=user_type_object.email)
        return Response(status=401)
    except:
        pass

    # store user_obj in db

    from version1.models import UserDetail
    new_user_object = UserDetail.objects.create(
        email=user_type_object.email,
        password=user_type_object.password,
        name=user_type_object.name,
        date_of_birth=user_type_object.date_of_birth,
        gender =user_type_object.gender,
        contact_number=user_type_object.contact_number
    )

    # return user_id object

    from .serializers import UserIdType
    user_id = UserIdType(id=new_user_object.id)
    from .serializers import UserIdSerializer
    user_id_serializer = UserIdSerializer(user_id)
    return Response(status=200,data=user_id_serializer.data)


# -----------------------------------Login API--------------------------------------

@api_view(['POST'])
def login_user(request):
    # call the serializers to validate the input data
    from .serializers import LoginDetailSerializer
    #validation
    login_detail_serializer=LoginDetailSerializer(data=request)
    if not login_detail_serializer.is_valid():
        return Response(status=400, data=login_detail_serializer.errors)

    # if the data is valid call save() method to get the login type python object to process data
    login_type_object=login_detail_serializer.save()
    email=login_type_object.email
    password=login_type_object.password

    try:
        from version1.models import UserDetail
        # vlidating email and password from database
        user_object=UserDetail.objects.get(email=email,password=password)
        # on success return response 200 and user id
        from .serializers import UserIdType
        user_id = UserIdType(id=user_object.id)
        from .serializers import UserIdSerializer
        user_id_serializer = UserIdSerializer(user_id)
        return Response(status=200, data=user_id_serializer.data)
    except:
        return Response(status=403)



