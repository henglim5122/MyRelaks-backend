import { defineStore } from "pinia";
import { useApi } from "@/composables/useApi";

interface User {
  // id?: number;
  first_name: string;
  last_name: string;
  username: string;
  password: string;
  email: string;
  gender: string;
  dob: string;
  phone_code: string;
  phone_number: string;
  city: string;
  country: string;
}

export const useUserStore = defineStore("userStore", {
  state: () => ({
    users: [] as User[],
    loggedInUser: null as User | null,
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

    // Registration function
    async registerUser(newUser: User): Promise<void> {
      try {
        const api = useApi();
        const response = await api.post("/register", newUser);
        // Assuming backend returns the created user data upon successful registration
        this.users.push(response.data); // Add new user to users list
        console.log("Registration successful:", response.data);
      } catch (err) {
        console.error("Error registering user:", err);
        throw err;
      }
    },

    // Login function
    async loginUser(username: string, password: string): Promise<void> {
      try {
        const api = useApi();
        const response = await api.post("/login", { username, password });
        // Assuming backend returns a user object and possibly a token
        this.loggedInUser = response.data.user; // Store the logged-in user
        // If you are using tokens, you could store the token locally
        localStorage.setItem("authToken", response.data.token);
        console.log("Login successful:", response.data);
      } catch (err) {
        console.error("Error logging in:", err);
        throw err;
      }
    },

    // Logout function to clear user session
    logoutUser(): void {
      this.loggedInUser = null;
      localStorage.removeItem("authToken");
      console.log("User logged out.");
    },
  },
});
