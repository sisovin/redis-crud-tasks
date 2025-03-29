<template>
  <div class="add-task">
    <form @submit.prevent="handleSubmit">
      <div>
        <label for="title">Title</label>
        <input type="text" id="title" v-model="title" required />
      </div>
      <div>
        <label for="description">Description</label>
        <textarea id="description" v-model="description" required></textarea>
      </div>
      <button type="submit">Add Task</button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { createTask } from '@/api/tasks';

export default defineComponent({
  name: 'AddTask',
  setup() {
    const title = ref('');
    const description = ref('');

    const handleSubmit = async () => {
      if (title.value && description.value) {
        await createTask(title.value, description.value);
        title.value = '';
        description.value = '';
      }
    };

    return {
      title,
      description,
      handleSubmit,
    };
  },
});
</script>

<style scoped>
.add-task {
  display: flex;
  flex-direction: column;
}
</style>
