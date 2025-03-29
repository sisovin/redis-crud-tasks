import { defineStore } from 'pinia';
import { login, register, verifyOTP } from '@/api/auth';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    isAuthenticated: false,
  }),
  actions: {
    async login(email: string, password: string) {
      try {
        const response = await login(email, password);
        this.user = response.user;
        this.isAuthenticated = true;
      } catch (error) {
        console.error('Login failed:', error);
      }
    },
    async register(email: string, password: string, password2: string, firstName: string, lastName: string) {
      try {
        const response = await register(email, password, password2, firstName, lastName);
        this.user = response.user;
        this.isAuthenticated = true;
      } catch (error) {
        console.error('Registration failed:', error);
      }
    },
    async verifyOTP(otp: string) {
      try {
        const response = await verifyOTP(otp);
        // Handle successful OTP verification
      } catch (error) {
        console.error('OTP verification failed:', error);
      }
    },
  },
});
