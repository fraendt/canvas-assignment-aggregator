from hw_v2 import Profile
print('Imported program.')
import time
from datetime import datetime

with open('token.txt') as f:
    token = f.read()
with open('courses.csv') as f:
    courses = f.read().split(',')
with open('url.txt') as f:
    url = f.read()
    
p = Profile()
p.add_canvas(url,token)
print('Adding all courses.')
for course in courses:
    p.add_canvas_course(course)
print('Added all courses.')
print('Getting all homework.')
start = time.time()
homework = p.get_all_canvas_hw()
end = time.time()
print(f'Retrieved all homework, {end-start} seconds elapsed.')


head = '''
        <html>
        <head>
        <title>Upcoming Homework</title>
        <link rel="stylesheet" href="style.css">
        </head>
        <body>
        <table>
        <tr>
            <th>Class</th>
            <th>Assignment</th>
            <th>Content</th>
            <th>Due Date</th>
        </tr>
        '''


content = ''.join([f'<tr><td>{items[0]}</td><td>{items[1]}</td><td>{items[2]}</td><td>{str(datetime.strptime(items[3],"%Y-%m-%dT%H:%M:%SZ"))[5:]}</td></tr>' for items in homework])

tail = '''
        </table>
        </body>
        </html>
        '''
with open('all_homework.html','w') as f:
    f.write(head + content + tail)
