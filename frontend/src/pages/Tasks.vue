<template>
  <div class="tasks-page">
    <AddTask />
    <TaskList />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import AddTask from '@/components/tasks/AddTask.vue';
import TaskList from '@/components/tasks/TaskList.vue';

export default defineComponent({
  name: 'Tasks',
  components: {
    AddTask,
    TaskList,
  },
});
</script>

<style scoped>
.tasks-page {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>
