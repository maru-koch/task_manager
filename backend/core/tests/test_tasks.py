from rest_framework.test import APITestCase
from rest_framework import status
from core.account.models import CustomUser
from core.models import Task
from django.urls import reverse

class TaskTestCase(APITestCase):

    def setUp(self):
        self.ordinary_user = CustomUser.objects.create_user(
            first_name="first",
            last_name="last",
            email="user@gmail.com",
            password="password01",)
        self.admin_user = CustomUser.objects.create_user(
            first_name="first",
            last_name="last",
            email="user2@gmail.com",
            password="password01",
            is_superuser=True)
    
    def test_create_task(self):
        """Tests the create task endpoint."""
        self.client.force_login(self.ordinary_user)
        response = self.client.post(reverse('tasks'), {
            "title":"task1",
            "description":"task1 description",
            "user":self.ordinary_user.id
        })
        assert(response.status_code == status.HTTP_201_CREATED)

    def test_list_tasks(self):
        """Tests the list tasks endpoint."""
        self.client.force_login(self.ordinary_user)
        for i in range(50):
            Task.objects.create(
                title=f"task{i}",
                description=f"task{i} description",
                user=self.ordinary_user)
        response = self.client.get(reverse('tasks'))
        assert(response.status_code == status.HTTP_200_OK)

    def test_retrieve_task(self):
        """Tests the retrieve task endpoint."""
        self.client.force_login(self.ordinary_user)
        task = Task.objects.create(
            title="task1",
            description="task1 description",
            user=self.ordinary_user)
        task = self.client.get(reverse('task-detail', args=[task.id]))
        assert(task.status_code == status.HTTP_200_OK)

    def test_complete_task(self):
        """test update tasks"""
        self.client.force_login(self.ordinary_user)
        task = Task.objects.create(
            title="task1",
            description="task1 description",
            user=self.ordinary_user)
        response = self.client.patch(reverse('task-detail', args=[task.id]), {
            "status":"completed",
            "completed":True
        })
        assert(response.status_code == status.HTTP_200_OK)
        assert(response.data['status'] == 'completed')

    def test_pagination(self):
        """Tests the pagination of the tasks."""
        self.client.force_login(self.ordinary_user)
        for i in range(50):
            Task.objects.create(
                title=f"task{i}",
                description=f"task{i} description",
                user=self.ordinary_user)
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.data['count'], 50)
        self.assertEqual(len(response.data['results']), 10)
        self.assertEqual(response.data['next'], 'http://testserver/api/v1/tasks?page=2')
        self.assertEqual(response.data['previous'], None)

    def test_analytics(self):
        """Tests the tasks analytics endpoint."""
        #Authenticate the user
        self.client.force_login(self.admin_user)

        #Create 50 tasks
        for i in range(50):
            Task.objects.create(
                title=f"task{i}",
                description=f"task{i} description",
                user=self.ordinary_user)
        
        #Complete 10 tasks
        tasks = self.client.get(reverse('tasks'))
        for task in tasks.data['results']:
            self.client.patch(reverse('task-detail', args=[task['id']]), {
                "status":"completed",
                "completed":True
            })

        response = self.client.get(reverse('tasks-analytics'))
        assert(response.data['completed_tasks'] == 10)
        assert(response.data['pending_tasks'] == 40)

    def tearDown(self) -> None:
        pass