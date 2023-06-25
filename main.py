import streamlit as st
from bs4 import BeautifulSoup
import lxml
import requests
from xlwt import *

st.set_page_config(layout='wide')
# st.sidebar.subheader("Amharic news recommendation system.")
# st.title('This is the web development using python.')

st.markdown('''
<style>
.font {
font-size: 15px;
font-family: 'Cooper Black';
color: #FFF;
background-color:#29465B;
border-style: none;
}
div.stButton > button:first-child {
background-color: blue;
color: #FFF;
font-size: 30px;
border-style: none;
}
</style>
''', unsafe_allow_html=True)

workbook = Workbook(encoding='utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'No')
table.write(0, 1, 'Title')
table.write(0, 2, 'Content')
table.write(0, 3, 'Urls')
table.write(0, 4, 'Category')
table.write(0, 5, 'Date')
table.write(0, 6, 'Number of Views')

line = 1
number = 0


def recommend_news(category='sport'):
    global line, number
    urls = f'http://www.ena.et/web/amh/{category}'
    pagination = True
    while pagination:
        html_text = requests.get(urls).text
        soup = BeautifulSoup(html_text, 'lxml')
        all_news = soup.find_all('div', class_="ena_display_item_text_container")
        for news in all_news:
            news_title = news.find('div', class_='ena_display_item_title').text.strip()
            news_content = news.find('div', class_='ena_display_item_content').text.strip()
            news_date = news.find('div', class_='ena_display_item_date').text.strip()
            number_views = news.find('span', class_='ena_display_item_viewcount').text.strip()
            links = news.find('a', class_='ena_display_item_content_link')['href']
            st.markdown(f'''
            <h4>{news_title} </h4>
            <p>{news_content[0:300]} .... </p>
            <a href="https://www.ena.et{links}"> https://www.ena.et{links}</a><br>
            <p>Posed on: <time datetime="{news_date}">{news_date}.</time></p>
            Number of views: <em>{number_views}</em><br><br>
            <button class = "font"> Read more...</button>
''', unsafe_allow_html=True)
            number = number + 1
            table.write(line, 0, number)
            table.write(line, 1, news_title)
            table.write(line, 2, news_content)
            table.write(line, 3, f'https://www.ena.et{links}')
            table.write(line, 4, category)
            table.write(line, 5, news_date)
            table.write(line, 6, number_views)
            line = line + 1
            workbook.save(f'{category}news.xls')

        if soup.find('ul', class_='pagination') is None:
            pagination = False
        urls = soup.find('ul', class_='pagination').find_all('li', class_='page-item')[1].find('a')['href']


st.sidebar.subheader('የሚቀጥለውን 👇 ፎርም ይሙሉ ✍️ /fill ✍️ the following  form')
st.sidebar.write('<style> div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
gender = st.sidebar.radio(
    'Sex/ጾታ', ('Male/ወንድ 👨‍🦰', 'Female/ሴት 👩‍🦰')
)
age = st.sidebar.selectbox('Age/እድሜ 👶🏿👦👴👩‍🦰👨‍🦰 ',
                           ('0 < 8 👼 ', '8 - 18 👶🏿', '18 - 30 👦', '30 - 40', '40 - 60 👴👴🏿', '> 60'))
education_level = st.sidebar.selectbox('Education Level/የትምህርት ደረጃ 👩‍🎓🧑🏿‍💻', (
    'Primary/የመጀምሪያ ደረጃ', '12 completed/12ኛ የጨረሰ', 'Deploma/ዲፕሎማ', 'Degree/የመጀመሪያ ዲግሪ', 'Masters/ማስተርስ ዲግሪ',
    "PhD/ዶክትሬት ዲግሪ"))
profession = st.sidebar.selectbox('User profession/ሙያ 👨‍🎓👩‍🎓', (
    'Sport/እስፖርት ⛷️🏋️‍♂️🤸', 'Politics/ፖለቲካ', 'Technology/ሳይንስና ቴክኖሎጂ', 'Environment/አካባቢ ጥበቃ',
    'Social/ማህበራዊ' 'world news/ዓለም አቀፍ ዜናዎች'))
recommend_me = st.sidebar.button('👩🏿‍💻 Recommend me...')

if recommend_me:
    news_category = ['politics', 'social', 'economy', 'technology', 'sport', 'environment', 'social', 'international']
    for category in news_category:
        recommend_news(category=category)
