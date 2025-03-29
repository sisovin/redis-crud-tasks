import { ref } from 'vue';
import { fetchTasks, createTask, updateTask, deleteTask } from '@/api/tasks';

export function useTasks() {
  const tasks = ref([]);

  const getTasks = async () => {
    tasks.value = await fetchTasks();
  };

  const addTask = async (title, description) => {
    const newTask = await createTask(title, description);
    tasks.value.push(newTask);
  };

  const editTask = async (id, title, description, completed) => {
    const updatedTask = await updateTask(id, title, description, completed);
    const index = tasks.value.findIndex((task) => task.id === id);
    if (index !== -1) {
      tasks.value[index] = updatedTask;
    }
  };

  const removeTask = async (id) => {
    await deleteTask(id);
    tasks.value = tasks.value.filter((task) => task.id !== id);
  };

  return {
    tasks,
    getTasks,
    addTask,
    editTask,
    removeTask,
  };
}
