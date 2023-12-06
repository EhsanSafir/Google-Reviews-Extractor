from review_extractor import GoogleReviewExtractor

if __name__ == '__main__':
    url = (
        'https://www.google.com/search?q=kfc++in+hamburg&sca_esv=587928711&biw=1860&bih=930&tbm=lcl&ei=_vpvZZW4KsKC9u8PoMe-8A8&ved=0ahUKEwiVr4P9_vmCAxVCgf0HHaCjD_4Q4dUDCAg&uact=5&oq=kfc++in+hamburg&gs_lp=Eg1nd3Mtd2l6LWxvY2FsIg9rZmMgIGluIGhhbWJ1cmcyCBAAGAcYHhgTMgcQABiABBgTMgYQABgeGBMyBhAAGB4YEzIGEAAYHhgTMggQABgIGB4YEzIIEAAYCBgeGBNIkSxQ0w5YgSlwAngAkAEAmAHgAaAByRCqAQYwLjEyLjG4AQPIAQD4AQHCAgkQABgeGPEEGArCAgYQABgHGB7CAggQIRigARjDBIgGAQ&sclient=gws-wiz-local#rlfi=hd:;si:15333890487430281620,l,Cg9rZmMgIGluIGhhbWJ1cmciA4gBAUijpc_R7YCAgAhaIBAAGAAYAiIOa2ZjIGluIGhhbWJ1cmcqBAgCEAAyAmRlkgESY2hpY2tlbl9yZXN0YXVyYW50qgFAEAEqByIDa2ZjKAUyHxABIhuhQS1HT8RjveUEu_yQrORg_MKX_mbzXrQrXPAyEhACIg5rZmMgaW4gaGFtYnVyZw;mv:[[53.5837155,10.0934412],[53.464924599999996,9.9253211]]')
    scrapper = GoogleReviewExtractor(url)
    scrapper.start_scrapping()
