import scrapy

class myspider(scrapy.Spider):
    name="quote"
    start_urls=['http://quotes.toscrape.com/random']

    def parse(self,response):
        yield{
        'text':response.css('span.text::text').get(),
        'author':response.css('small.author::text').get(),
        'tags':response.css('a.tag::text').extract_first(),
        }
    
    
