from django.shortcuts import render, redirect
from .models import Job
from faker import Faker
from decouple import config
import requests
from pprint import pprint

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')

def past_life(request):
    # 사용자로부터 이름 데이터를 받음.
    name = request.POST.get('name')
   
    # db 에 매칭되는 name 가져오기 
    # Job.objects.get(name=name)
    # get 이 더 간단하지만 해당 값이 없을 경우 에러가 발생하기 때문.
    # filter 한개던 0개던 상관없이 무조건 쿼리섹으로 가져옴.(리스트 형식)
    person = Job.objects.filter(name=name).first()

    # db 에 person 이 있는지 없는지 판단
    if person: # db 에 기존 이름이 있다면,
        past_job = person.past_job
    else: # db 에 기존 이름이 없다면(person 이 빈 쿼리셋(==False))
        faker = Faker()
        past_job = faker.job()
        person = Job(name=name, past_job=past_job) # 새로운 레코드를 추가한다.
        person.save()

    # GIPHY (past_job을 API에 요청을 보내서 응답을)
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}'
    data = requests.get(url).json()
    image = data.get('data')[0].get('images').get('original').get('url')


    context = {'person': person, 'image': image}
    return render(request, 'jobs/past_life.html', context)