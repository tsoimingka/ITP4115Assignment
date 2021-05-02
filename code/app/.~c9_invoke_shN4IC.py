
from app import db
from app.models import User, Programme_Language, Subject, Course, Course_Type, Course_Difficulty

db.create_all()


u1 = User(
    "admin",
    "admin",
    "admin"
)


l1 = Programme_Language(
    'HTML & CSS',
    1,
    'HTML is the foundation of all web pages. It defines the structure of a page, while CSS defines its style. HTML and CSS are the beginning of everything you need to know to make your first web page! Learn both and start creating amazing websites.'
)
l2 = Programme_Language(
    'Python',
    2,
    'Python is a general-purpose, versatile, and powerful programming language. It’s a great first language because it’s concise and easy to read. Whatever you want to do, Python can do it. From web development to machine learning to data science, Python is the language for you.'
)
l3 = Programme_Language(
'JavaScript',
3,
'JavaScript is a fun and flexible programming language. It’s one of the core technologies of web development and can be used on both the front-end and the back-end.'
)
l4 = Programme_Language(
'Java',
4,
'Java is one of the most popular programming languages out there. Released in 1995 and still widely used today, Java has many applications, including software development, mobile applications, and large systems development. Knowing Java opens a lot of possibilities for you as a developer.'
)
l5 = Programme_Language(
'SQL',
5,
'SQL is the standard relational data management language. We live in a data-driven world, and there are many businesses that store their information inside large, relational databases. This makes SQL a great skill not only for data scientists and engineers, but for anyone wanting to be data-literate.'
)
l6 = Programme_Language(
'Bash/Shell',
6,
'We use a mouse or finger to click icons and access files, programs, and folders on our devices. But this is just one way for us to communicate with computers. The command line and the shell make up a quick, powerful, text-based interface developers use to more effectively and efficiently communicate with computers to accomplish a wider set of tasks.'
)
l7 = Programme_Language(
'Ruby',
7,
'Ruby is a dynamic, general-purpose programming language most commonly used for Web Development. Its key designer, Yukihiro Matsumoto, said that Ruby was designed for humans, not machines, making it a favorite of many developers and tech companies. Its most popular implementation is with the powerful Ruby on Rails web framework.'
)
l8 = Programme_Language(
'C++',
8,
'C++ is a very popular language for performance-critical applications that rely on speed and efficient memory management. It’s used in a wide range of industries including software and game development, VR, robotics, and scientific computing.'
)
l9 = Programme_Language(
'R',
9,
'R is a widely used statistical programming language that’s beloved by people in academia and the tech industry. But that makes it sound more intimidating than it actually is. R is a great first language for anyone interested in answering questions with data analysis, data visualization, and data science.'
)
l10 = Programme_Language(
'C#',
10,
'C# is one of the most popular programming languages. It can be used for a variety of things, including mobile applications, game development, and enterprise software. Knowing C# opens a great deal of doors for you as a developer.'
)
l11 = Programme_Language(
'PHP',
11,
'PHP is a general-purpose scripting language widely used as a server-side language for creating dynamic web pages. Though its reputation is mixed, PHP is still extremely popular and is used in over 75% of all websites where the server-side programming language is known.'
)
l12 = Programme_Language(
'Go',
12,
'Go, or Golang, is an open source programming language developed at Google. The designers of Go wanted developers to have a programming language that made it quick and easy to develop applications. Go is used on servers, web development, and even command line interafaces.'
)
l13 = Programme_Language(
'Swift',
13,
'Swift is a modern programming language developed by Apple. This general-purpose programming language is fast and powerful without sacrificing safety or readability. Swift is a great language to learn for those interested in iOS and MacOS development as well as anyone who is just starting to code.'
)
l14 = Programme_Language(
'Kotlin',
14,
'Kotlin is a modern, general-purpose programming language developed by JetBrains. Its full compatibility with Java and concise syntax makes it an appealing language for web development, Android development, and more.'
)
s1 = Subject('Web Development',1,'Web Development is the practice of developing websites and web apps that live on the internet. Whether you’re interested in front-end, back-end, or going full-stack, the content in our Web Development domain will help you get there.')
s2 = Subject(
'Data Science',
2,
'Data Scientists try to make sense of the data that’s all around us. Learning Data Science can help you make informed decisions, create beautiful visualizations, and even try to predict future events through Machine Learning. If you’re curious about what you can learn about the world using the data produced every day, then Data Science might be for you!'
)
s3 = Subject(
'Computer Science',
3,
'Computer Science, often referred to as “CS,” is a broad term that covers many sub-disciplines, including the worlds of software and hardware. It can be found in every piece of technology you use, from a smartphone or gaming console to a car or ATM. With so many applications for Computer Science, there’s a space for everyone!'
)
s4 = Subject(
'Developer Tools',
4,
'Writing code is as much about the tools at your disposal as it is about the actual code you write. These tools that allow you to run code locally on your computer and collaborate with others to publish programs. Talk to the computer through the command line and merge your first line of code on git.'
)
s5 = Subject(
'Machine Learning',
5,
'Machine Learning is an increasingly hot field of data science dedicated to enabling computers to learn from data. From spam filtering in social networks to computer vision for self-driving cars, the potential applications of Machine Learning are vast.'
)
s6 = Subject(
'Code Foundations',
6,
'Interested in learning how to code, but unsure where to start? Our Code Foundations domain provides an overview of the main applications of programming and teaches important concepts that you’ll find in every programming language. This content will prepare you to chart a course to a more technical career.'
)
s7 = Subject(
'Web Design',
7,
'Web Design is essential to bringing a website to life and creating the experience that you want for your end Users. The CCourse here will help you polish your HTML and CSS skills while learning about color design, navigation design, and more.'
)
s8 = Subject(
'Game Development',
8,
'There’s a gamer in all of us — whether you play on your phone, a console, a computer, or a virtual reality rig. And it takes people, either individually or in large teams, to bring these great experiences to life. Learn the foundations of Game Development and create your very own video game.'
)
s9 = Subject(
'Mobile Development',
9,
'Every year more and more people rely on mobile devices to meet their needs. Where websites used to be the gold-standard, people now rely on mobile apps. The technologies used to create these apps are expanding and improving quickly, so it’s an exciting time to start learning Mobile Development!'
)
s10 = Subject(
'Data Visualization',
10,
'Data Visualization is the process of communicating complex information with simple graphics and charts. Data Visualization has the power to tell data-driven stories while allowing people to see patterns and relationships found in data.'
)
s11 = Subject(
'Cybersecurity',
11,
'Cybersecurity is a fast-growing field that addresses the security risks of our increasingly connected digital world. Learn cybersecurity, and you will learn how Users, companies, and even governments protect themselves and recover from, cyber threats and attacks. Start defending yourself, or your organization, or let this be your first step to becoming a security professional!'
)

ct1 = Course_Type('Course')
ct2 = Course_Type('Skill Path')
ct3 = Course_Type('Career Path')

cd1 = Course_Difficulty('Beginner friendly')
cd2 = Course_Difficulty('Intermediate')

c1 = Course(
    "Learn HTML",
    1,
    1, 
    3838595,
    9
)

db.session.add(u1)
db.session.add_all([l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l11,l13,l14])
db.session.add_all([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11])
db.session.add_all([ct1,ct2,ct3])
db.session.add_all([cd1, cd2])
db.session.add_all([c1])

db.session.commit()