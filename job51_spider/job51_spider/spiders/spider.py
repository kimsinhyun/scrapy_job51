import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,01%252c38%252c31%252c40%252c32,9,99,+,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']

    def start_requests(self):
        
        yield scrapy.Request(self.start_urls[0])

    def parse(self, response):
        item = {}
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(response.body)
    