from rest_framework.response import Response
from rest_framework.views import APIView

from users.selectors import user_list
from users.serializers import FilterSerializer, UserOutputSerializer


class UserListApi(APIView):
    def get(self, request):
        filters_serializer = FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        users = user_list(filters=filters_serializer.validated_data)

        data = UserOutputSerializer(users, many=True).data

        return Response(data)
