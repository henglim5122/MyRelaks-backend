import { defineStore } from "pinia";
import { useApi } from "@/composables/useApi";

interface User {
  id?: number;
  first_name: string;
  last_name: string;
  username: string;
  password: string;
  email: string;
  gender: string;
  dob: Date;
  phone_code: string;
  phone_number: string;
  city: string;
  country: string;
}

export const useUserStore = defineStore("userStore", {
  state: () => ({
    users: [] as User[],
  }),

  actions: {
    async fetchUsers(): Promise<User[]> {
      try {
        const api = useApi();
        const response = await api.get("/user");
        this.users = response.data;
        return this.users;
      } catch (err) {
        console.error("Error fetching users:", err);
        throw err;
      }
    },
  },
});
