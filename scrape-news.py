import webscraper

news = input("Please enter the full URL including httpd:// for your favorite news site: \n")
webscraper.Scraper(news).scrape()

