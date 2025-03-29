<template>
  <div class="dashboard">
    <h1>Welcome, {{ user.firstName }}!</h1>
    <p>Your email: {{ user.email }}</p>
    <p>Account created on: {{ user.dateJoined }}</p>
    <button @click="logout">Logout</button>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useAuthStore } from '@/store/auth';

export default defineComponent({
  name: 'Dashboard',
  setup() {
    const authStore = useAuthStore();
    const user = authStore.user;

    const logout = () => {
      authStore.logout();
    };

    return {
      user,
      logout,
    };
  },
});
</script>

<style scoped>
.dashboard {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
