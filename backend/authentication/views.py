from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, LoginSerializer, OTPSerializer, VerifyOTPSerializer
from .otp import generate_otp, verify_otp

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

class OTPView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OTPSerializer

    def post(self, request, *args, **kwargs):
        otp = generate_otp(request.user)
        # Send OTP to user via email or SMS
        return Response({'otp': otp}, status=status.HTTP_200_OK)

class VerifyOTPView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = VerifyOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = serializer.validated_data['otp']
        if verify_otp(request.user, otp):
            return Response({'detail': 'OTP verified successfully'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
