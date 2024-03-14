import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Dashboard.vue";
import AddProject from "../views/AddProject.vue";
import EditProject from "../views/EditProject.vue";

const routes = [
  {
    path: "/",
    name: "Dashboard",
    component: Home,
  },
  {
    path: "/add",
    name: "AddProject",
    component: AddProject,
  },
  {
    path: "/tasks/:id",
    name: "EditProject",
    component: EditProject,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
