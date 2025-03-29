<template>
  <div class="task-item">
    <h3>{{ task.title }}</h3>
    <p>{{ task.description }}</p>
    <div>
      <button @click="editTask">Edit</button>
      <button @click="deleteTask">Delete</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from 'vue';
import { updateTask, deleteTask } from '@/api/tasks';

export default defineComponent({
  name: 'TaskItem',
  props: {
    task: {
      type: Object as PropType<{ id: number; title: string; description: string; completed: boolean }>,
      required: true,
    },
  },
  methods: {
    async editTask() {
      const updatedTask = await updateTask(this.task.id, this.task.title, this.task.description, !this.task.completed);
      this.$emit('update-task', updatedTask);
    },
    async deleteTask() {
      await deleteTask(this.task.id);
      this.$emit('delete-task', this.task.id);
    },
  },
});
</script>

<style scoped>
.task-item {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px 0;
}
</style>
