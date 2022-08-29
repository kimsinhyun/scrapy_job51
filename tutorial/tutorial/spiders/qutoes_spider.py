import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://search.51job.com/list/000000,000000,7500%252C0100%252C7700%252C7200%252C7300,00,9,99,%2B,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, encoding='utf-8')

    def parse(self,response):
        filename = f"quotes-test.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')