#-*- coding: utf-8 -*-
{
    'name': 'To-Do Application',
    'description': 'Manage your personal Tasks with this module. ',
    'author': 'Daniel Reis',
    'depends': ['mail'],
    'data':[
        'views/todo_view.xml',
        'views/view_form_todo_task.xml',
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml'],
    'application': True,
}
