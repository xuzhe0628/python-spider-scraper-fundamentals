import scrapy
from ..items import MovieItem # import the item we defined

class MovieSpider(scrapy.Spider):
    # this is the name of the spider,
    # it will be used when we want to start the cralwer
    name = "Movie" 
    start_urls = [
        'https://www.themoviedb.org/movie',
    ]

    def parse(self, response):
        # use css selector to locate the elements containing movie information
        # populate the item with data we got
        for movie in response.css('div.info'):
            mItem = MovieItem()
            mItem['_id'] = ('https://www.themoviedb.org' + 
                movie.css('p.flex a::attr("href")').extract_first())
            mItem['movie'] = movie.css('p.flex a::text').extract_first()
            mItem['rating'] = movie.css('span.vote_average::text').extract_first()
            mItem['release_date'] = movie.css('span.release_date::text').extract_first()
            mItem['genres'] = movie.css ('span.genres::text').extract_first()
            mItem['overview'] = movie.css ('p.overview::text').extract_first()
            yield mItem
        
        # return the url of next page
        next_page = response.css('p.right.pagination a::attr("href")').extract()
        if len(next_page) > 1:
            next_page = next_page[1]
        else:
            next_page = next_page[0]
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            
            
