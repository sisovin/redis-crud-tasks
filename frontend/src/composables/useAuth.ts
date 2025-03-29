import { ref } from 'vue';
import { login, register, verifyOTP } from '@/api/auth';

export function useAuth() {
  const isAuthenticated = ref(false);
  const user = ref(null);

  const handleLogin = async (email: string, password: string) => {
    try {
      const response = await login(email, password);
      isAuthenticated.value = true;
      user.value = response.user;
      // Handle successful login (e.g., store tokens, redirect)
    } catch (error) {
      console.error('Login failed:', error);
      // Handle login error (e.g., show error message)
    }
  };

  const handleRegister = async (email: string, password: string, password2: string, firstName: string, lastName: string) => {
    try {
      const response = await register(email, password, password2, firstName, lastName);
      isAuthenticated.value = true;
      user.value = response.user;
      // Handle successful registration (e.g., store tokens, redirect)
    } catch (error) {
      console.error('Registration failed:', error);
      // Handle registration error (e.g., show error message)
    }
  };

  const handleVerifyOTP = async (otp: string) => {
    try {
      const response = await verifyOTP(otp);
      // Handle successful OTP verification (e.g., update state, redirect)
    } catch (error) {
      console.error('OTP verification failed:', error);
      // Handle OTP verification error (e.g., show error message)
    }
  };

  return {
    isAuthenticated,
    user,
    handleLogin,
    handleRegister,
    handleVerifyOTP,
  };
}
