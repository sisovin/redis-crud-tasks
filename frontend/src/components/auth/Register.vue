<template>
  <div class="register-container">
    <h2>Register</h2>
    <form @submit.prevent="handleRegister">
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" v-model="password" required />
      </div>
      <div class="form-group">
        <label for="password2">Confirm Password</label>
        <input type="password" v-model="password2" required />
      </div>
      <div class="form-group">
        <label for="firstName">First Name</label>
        <input type="text" v-model="firstName" required />
      </div>
      <div class="form-group">
        <label for="lastName">Last Name</label>
        <input type="text" v-model="lastName" required />
      </div>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { register } from '@/api/auth';

export default defineComponent({
  name: 'Register',
  setup() {
    const email = ref('');
    const password = ref('');
    const password2 = ref('');
    const firstName = ref('');
    const lastName = ref('');

    const handleRegister = async () => {
      try {
        const response = await register(email.value, password.value, password2.value, firstName.value, lastName.value);
        console.log('Registration successful:', response);
        // Handle successful registration (e.g., redirect to login page)
      } catch (error) {
        console.error('Registration failed:', error);
        // Handle registration error (e.g., show error message)
      }
    };

    return {
      email,
      password,
      password2,
      firstName,
      lastName,
      handleRegister,
    };
  },
});
</script>

<style scoped>
.register-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
