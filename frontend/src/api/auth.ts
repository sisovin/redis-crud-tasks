import axios from 'axios';

const API_URL = 'http://localhost:8000/api/auth/';

export const login = async (email: string, password: string) => {
  const response = await axios.post(`${API_URL}login/`, { email, password });
  return response.data;
};

export const register = async (email: string, password: string, password2: string, firstName: string, lastName: string) => {
  const response = await axios.post(`${API_URL}register/`, { email, password, password2, first_name: firstName, last_name: lastName });
  return response.data;
};

export const verifyOTP = async (otp: string) => {
  const response = await axios.post(`${API_URL}verify-otp/`, { otp });
  return response.data;
};
