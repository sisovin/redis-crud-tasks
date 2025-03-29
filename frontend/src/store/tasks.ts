import { defineStore } from 'pinia';
import { fetchTasks, createTask, updateTask, deleteTask } from '@/api/tasks';

export const useTasksStore = defineStore('tasks', {
  state: () => ({
    tasks: [],
  }),
  actions: {
    async fetchTasks() {
      this.tasks = await fetchTasks();
    },
    async createTask(title, description) {
      const newTask = await createTask(title, description);
      this.tasks.push(newTask);
    },
    async updateTask(id, title, description, completed) {
      const updatedTask = await updateTask(id, title, description, completed);
      const index = this.tasks.findIndex((task) => task.id === id);
      if (index !== -1) {
        this.tasks[index] = updatedTask;
      }
    },
    async deleteTask(id) {
      await deleteTask(id);
      this.tasks = this.tasks.filter((task) => task.id !== id);
    },
  },
});
