
from rest_framework import status, viewsets, mixins, generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import *

# Create your views here.
class VerifyIAM(generics.GenericAPIView):
    serializer_class = TransactionDataSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"code": "0000",
                    "message": "success",
                    "device": {
                    "userId": "userId",
                    "tokenId": "TCBXNLDG1V",
                    "model": "iPhone,14.2",
                    "secondFAMethod": "QR",
                    "spid": "IAM"}}, status=status.HTTP_200_OK)

class VerifyOTP(generics.GenericAPIView):
    serializer_class = TransactionDataSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"code": "0000",
                        "message": "success"
                       }, status=status.HTTP_200_OK)


class RegisterIAMToken(generics.GenericAPIView):
    serializer_class = DataSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"code": "0000",
                        "message": "success",
                        "tokenId": "9WULFTZ4B4",
                        "apin":
                        "Buek9L+Ov/IvpRsp03BHd9VN1qD1hVsRdaHRL0g1XnntvgCOlULTJSZq9jx0FhiPpWBdag9+TOdyj7+nATSFQg=="}, status=status.HTTP_200_OK)