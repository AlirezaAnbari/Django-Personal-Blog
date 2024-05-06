from django.shortcuts import render

from datetime import date


all_posts = [
    {
        'slug': 'hike-in-the-mountains',
        'image': 'alone.jpg',
        'author': 'Alireza',
        'date': date(2024, 4, 1),
        'title': 'Backend Development',
        "excerpt": 'Backend Lorem ipsum dolor sit amet, con sectetur adipiscing elit,\
        sed do eiusmod tempor inc tempor inc et precedence    ea elements',
        "content": '''
        lorem ipsum dolor sit amet, consectetur adip iscing elit, sed do eius mod tempor inc tempor inc et precedence
        aenelements ea commodo consequat n dictionnary existent. Excepteur sint occaecat cupid id du */', 
        self.__class__class a sfdf gfgfgf h ffhfgfgf
        '''
    },
    {
        'slug': 'hike-in-the-vscode',
        'image': 'Code.jpg',
        'author': 'Hassan',
        'date': date(2024, 5, 1),
        'title': 'Frontend Development',
        "excerpt": 'Frontend Lorem ipsum dolor sit amet, con sectetur adipiscing elit,\
        sed do eiusmod tempor inc tempor inc et precedence    ea elements',
        "content": '''
        lorem ipsum dolor sit amet, consectetur adip iscing elit, sed do eius mod tempor inc tempor inc et precedence
        aenelements ea commodo consequat n dictionnary existent. Excepteur sint occaecat cupid id du */', 
        self.__class__class a sfdf gfgfgf h ffhfgfgf
        '''
    },
    {
        'slug': 'ML',
        'image': 'coding-setup.jpg',
        'author': 'Alireza',
        'date': date(2024, 6, 1),
        'title': 'ML',
        "excerpt": 'Backend Lorem ipsum dolor sit amet, con sectetur adipiscing elit,\
        sed do eiusmod tempor inc tempor inc et precedence    ea elements',
        "content": '''
        lorem ipsum dolor sit amet, consectetur adip iscing elit, sed do eius mod tempor inc tempor inc et precedence
        aenelements ea commodo consequat n dictionnary existent. Excepteur sint occaecat cupid id du */', 
        self.__class__class a sfdf gfgfgf h ffhfgfgf
        '''
    },
    {
        'slug': 'DL',
        'image': 'profile.png',
        'author': 'Hassan',
        'date': date(2024, 7, 1),
        'title': 'DL',
        "excerpt": 'Frontend Lorem ipsum dolor sit amet, con sectetur adipiscing elit,\
        sed do eiusmod tempor inc tempor inc et precedence    ea elements',
        "content": '''
        lorem ipsum dolor sit amet, consectetur adip iscing elit, sed do eius mod tempor inc tempor inc et precedence
        aenelements ea commodo consequat n dictionnary existent. Excepteur sint occaecat cupid id du */', 
        self.__class__class a sfdf gfgfgf h ffhfgfgf
        '''
    },
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    
    context = {
        'posts': latest_posts,
    }
    
    return render(request, 'blog/index.html', context)


def posts(request):
    context = {
        'all_posts': all_posts,
    }
    
    return render(request, 'blog/all-posts.html', context)


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    
    context = {
        'post': identified_post,
    }
    
    return render(request, 'blog/post-detail.html', context)