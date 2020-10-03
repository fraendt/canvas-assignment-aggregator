import requests
from canvasapi import Canvas
from datetime import datetime
import re

class Profile:
    def __init__(self,auth=[]):
        if len(auth)==2:
            self.canvas = Canvas(auth[0],auth[1])
        else:
            self.canvas = ""
        self.courses = []
        self.other = []
        self.get_all_canvas_hw = self.get_all_homework

    def add_canvas(self, url, token):
        '''
        Get Canvas access token in user settings
        '''
        self.canvas = Canvas(url,token)

    def add_canvas_course(self, num):
        '''
        At this point, all classes are "Assignments" based
        '''
        if self.canvas == "":
            raise Exception("No Canvas account added to profile.")
        
        if str(num).isnumeric():
            self.courses.append(num)
            
    def get_canvas_hw(self,course):
        if self.canvas == "":
            raise Exception("No Canvas account added to profile.")
        
        homework = []
        c = self.canvas.get_course(course)
        assignments = c.get_assignments()
        for assignment in assignments:
            if assignment.due_at == None:
                continue
            dueDate = datetime.strptime(assignment.due_at[:10],"%Y-%m-%d")
            today = datetime.today()
            if dueDate >= today:
                m = re.findall("(?<=\<p>)(.*?)(?=\</p>)",str(assignment.description))
                content = "\n".join(m)
                homework.append([c.name, assignment.name, content, assignment.due_at])
                    
        return homework

    def get_all_homework(self):
        res = []
        for course in self.courses:
            res += self.get_canvas_hw(course)
        return res

    '''def get_all_canvas_hw(self):
        return self.get_all_homework(self)
'''
