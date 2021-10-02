from bs4 import  BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course = soup.find_all('div', class_='card')
    for c in course:
        course_name= c.h5.text
        course_price= c.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
        print(" ")