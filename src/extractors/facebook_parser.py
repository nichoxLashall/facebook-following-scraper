thonimport requests
from bs4 import BeautifulSoup

class FacebookParser:
    def __init__(self, profile_url, max_items):
        self.profile_url = profile_url
        self.max_items = max_items

    def scrape_following_data(self):
        data = []
        page = requests.get(self.profile_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        followers_section = soup.find('div', {'class': 'followers'})
        followers = followers_section.find_all('div', {'class': 'follower-item'})

        for follower in followers[:self.max_items]:
            follower_data = {
                'id': follower.get('data-id'),
                'image': follower.find('img')['src'],
                'title': follower.find('h3').text,
                'subtitle_text': follower.find('p').text if follower.find('p') else '',
                'url': follower.find('a')['href']
            }
            data.append(follower_data)

        return data