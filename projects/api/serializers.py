from rest_framework import serializers

class DeviceDataSerializer(serializers.Serializer):
    userId = serializers.CharField()
    spid = serializers.CharField()

class DataSerializer(serializers.Serializer):
    externalTxId = serializers.CharField()
    device = DeviceDataSerializer()
    otp = serializers.CharField()

class TransactionDataSerializer(serializers.Serializer):
    externalTxId = serializers.CharField()
    device = DeviceDataSerializer()
    otp = serializers.CharField()