# from django.test import TestCase
# from .models import Project 
# from django.contrib.auth.models import User

# # Create your tests here.
# class ProjectTestClass(TestCase):
#     def setUp(self):
#         self.user=User(username='chichi')
#         self.user.save()
#         self.project=Project()   

#     def tearDown(self):
#         Project.objects.all().delete()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.project, Project))

#     def test_saveProject(self):
#         self.project.save_project()
#         project_saved = Project.objects.all()
#         self.assertTrue(len(project_saved) > 0)