from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/',views.home,name='home'),
    path('/dashboard',views.dashboard,name=  'dashboard'),
    path('/keyboard',views.keyboard,name='keyboard'),
    path('/levels',views.levels,name='levels'),
    path('/practice',views.levels,name='practice'),
    path('/profile',views.profile,name='profile'),
    path('/level_1_tutorial',views.tut1,name='tut1'),
    path('/level_2_tutorial',views.tut2,name='tut2'),
    path('/level_3_tutorial',views.tut3,name='tut3'),
    path('/level_4_tutorial',views.tut4,name='tut4'),
    path('/level_5_tutorial',views.tut5,name='tut5'),
    path('/level_6_tutorial',views.tut6,name='tut6'),
    path('/level_7_tutorial',views.tut7,name='tut7'),
    path('/level_8_tutorial',views.tut8,name='tut8'),
    path('/level_9_tutorial',views.tut9,name='tut9'),
    path('/level_10_tutorial',views.tut10,name='tut10'),
    path('/level_11_tutorial',views.tut11,name='tut11'),
    path('/level_12_tutorial',views.tut12,name='tut12'),
    path('/level_13_tutorial',views.tut13,name='tut13'),
    path('/level_14_tutorial',views.tut14,name='tut14'),
    path('/level_15_tutorial',views.tut15,name='tut15'),
    path('/level_1',views.level1,name='level1'),
    path('/level_2',views.level2,name='level2'),
    path('/level_3',views.level3,name='level3'),
    path('/level_4',views.level4,name='level4'),
    path('/level_5',views.level5,name='level5'),
    path('/level_6',views.level6,name='level6'),
    path('/level_7',views.level7,name='level7'),
    path('/level_8',views.level8,name='level8'),
    path('/level_9',views.level9,name='level9'),
    path('/level_10',views.level10,name='level10'),
    path('/level_11',views.level11,name='level11'),
    path('/level_12',views.level12,name='level12'),
    path('/level_13',views.level13,name='level13'),
    path('/level_14',views.level14,name='level14'),
    path('/level_15',views.level15,name='level15'),
    path('/level_16',views.level16,name='level16'),
]

