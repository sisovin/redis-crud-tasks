<template>
  <div class="task-list">
    <TaskItem
      v-for="task in tasks"
      :key="task.id"
      :task="task"
      @update-task="updateTask"
      @delete-task="deleteTask"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { fetchTasks } from '@/api/tasks';
import TaskItem from './TaskItem.vue';

export default defineComponent({
  name: 'TaskList',
  components: {
    TaskItem,
  },
  setup() {
    const tasks = ref([]);

    const getTasks = async () => {
      tasks.value = await fetchTasks();
    };

    const updateTask = (updatedTask) => {
      const index = tasks.value.findIndex((task) => task.id === updatedTask.id);
      if (index !== -1) {
        tasks.value[index] = updatedTask;
      }
    };

    const deleteTask = (taskId) => {
      tasks.value = tasks.value.filter((task) => task.id !== taskId);
    };

    onMounted(() => {
      getTasks();
    });

    return {
      tasks,
      updateTask,
      deleteTask,
    };
  },
});
</script>

<style scoped>
.task-list {
  display: flex;
  flex-direction: column;
}
</style>
