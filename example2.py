from review_extractor import GoogleReviewExtractor

if __name__ == '__main__':
    url = (
        'https://www.google.com/search?sca_esv=587928711&sxsrf=AM9HkKn9ZSTemku4jCrw4QniU6rePNk8PA:1701756520577&q=kfc+hamburg&sa=X&ved=2ahUKEwjNwJyH0feCAxXwgf0HHZI-DloQuzF6BAgOEAI&biw=1488&bih=755&dpr=1.25#ip=1&lkt=LocalPoiReviews&rlimm=15333890487430281620')
    scrapper = GoogleReviewExtractor(url)
    scrapper.start_scrapping()
