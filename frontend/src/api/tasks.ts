import axios from 'axios';

const API_URL = 'http://localhost:8000/api/tasks/';

export const fetchTasks = async () => {
  const response = await axios.get(API_URL);
  return response.data;
};

export const createTask = async (title: string, description: string) => {
  const response = await axios.post(API_URL, { title, description });
  return response.data;
};

export const updateTask = async (id: number, title: string, description: string, completed: boolean) => {
  const response = await axios.put(`${API_URL}${id}/`, { title, description, completed });
  return response.data;
};

export const deleteTask = async (id: number) => {
  const response = await axios.delete(`${API_URL}${id}/`);
  return response.data;
};
