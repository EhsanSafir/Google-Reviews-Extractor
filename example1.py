from review_extractor import GoogleReviewExtractor

if __name__ == '__main__':
    url = 'https://www.google.com/search?q=kfc+hamburg&sca_esv=587928711&tbm=lcl&sxsrf=AM9HkKn0Q5eGJWwdIEBI7FxXKrZbfUcxYw%3A1701755199665&ei=P7luZcaXKI-L9u8Pp9qx0Ak&oq=kfc+&gs_lp=Eg1nd3Mtd2l6LWxvY2FsGgIYAyIEa2ZjICoCCAAyBBAjGCcyDRAAGIAEGIoFGEMYyQMyChAAGIAEGIoFGEMyDhAAGIAEGIoFGJECGIsDMg4QABiABBiKBRiSAxiLAzIOEAAYgAQYigUYkQIYiwMyCBAAGIAEGIsDMggQABiABBiLAzIIEAAYgAQYiwMyCBAAGIAEGIsDSP0OUABYgARwAHgAkAEAmAGmAqAB9wWqAQUwLjMuMbgBA8gBAPgBAcICDRAAGIAEGIoFGEMYiwPCAhAQABiABBiKBRhDGMkDGIsDwgILEAAYgAQYigUYkQKIBgE&sclient=gws-wiz-local#rlfi=hd:;si:8869887934153824414,a;mv:[[53.737915370502854,10.030817296191405],[53.592877829497176,9.777445103808592]]'
    scrapper = GoogleReviewExtractor(url)
    scrapper.start_scrapping()
