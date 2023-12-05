from review_extractor import GoogleReviewExtractor

if __name__ == '__main__':
    url = ('https://www.google.com/search?q=Mac+Donalds+in+Haburg&oq=Mac+Donalds+in+Haburg&gs_lcrp'
           '=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgNGIAEMgkIAhAAGA0YgAQyCQgDEAAYDRiABDIKCAQQABgFGA0YHjIKCAUQABgIGA0YHtIBCDY4OTlqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8#ip=1&rlimm=12450635171165457325')
    scrapper = GoogleReviewExtractor(url)
    scrapper.start_scrapping()
