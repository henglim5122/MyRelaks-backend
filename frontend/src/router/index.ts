/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from "vue-router/auto";
import { setupLayouts } from "virtual:generated-layouts";
import { routes } from "vue-router/auto-routes";
// import LandingMap from "@/components/LandingMap.vue"; // Adjust the path to your component
// import FunctionPage from "@/pages/FunctionPage.vue";
// import Index from "@/pages/index.vue";

// const routes = [
//   {
//     path: "/",
//     name: "IndexPage",
//     component: Index, // Component for /index route
//   },
//   {
//     path: "/FunctionPage",
//     name: "FunctionPage",
//     component: FunctionPage,
//   },
// ];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: setupLayouts(routes),
});

// router.beforeEach(async (to, from) => {
//   const isAuthenticated = () => {
//     const token = localStorage.getItem("authToken");
//     return token && token.length > 0;
//   };

//   const getUserRole = () => {
//     return localStorage.getItem("roles");
//   };

//   if (to.path.startsWith("/admin") && getUserRole() !== "admin") {
//     return { path: "/" };
//   } else if (to.path.startsWith("/user") && getUserRole() !== "user") {
//     return { path: "/" };
//   }

//   if (to.path.startsWith("/loggedin") && !isAuthenticated()) {
//     return { path: "/login" };
//   } else if (to.path.startsWith("/login") && isAuthenticated()) {
//     return { path: "/loggedin" };
//   }

//   if (
//     to.path.startsWith("/resetpassword") &&
//     (!isAuthenticated() || isAuthenticated())
//   ) {
//     return { path: "/" };
//   }

//   // if (to.path.startsWith("/userprofile") && !isAuthenticated()) {
//   //   return { path: "/" };
//   // }
// });

// Workaround for https://github.com/vitejs/vite/issues/11804
router.onError((err, to) => {
  if (err?.message?.includes?.("Failed to fetch dynamically imported module")) {
    if (!localStorage.getItem("vuetify:dynamic-reload")) {
      console.log("Reloading page to fix dynamic import error");
      localStorage.setItem("vuetify:dynamic-reload", "true");
      location.assign(to.fullPath);
    } else {
      console.error("Dynamic import error, reloading page did not fix it", err);
    }
  } else {
    console.error(err);
  }
});

router.isReady().then(() => {
  localStorage.removeItem("vuetify:dynamic-reload");
});

export default router;
