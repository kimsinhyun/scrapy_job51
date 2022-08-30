import re
import scrapy
import copy

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['51job.com']
    # start_urls = ['https://search.51job.com/list/000000,000000,0000,01%252c38%252c31%252c40%252c32,9,99,+,2,{i}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=' for i in range(1,2000)]
    start_urls = ['https://jobs.51job.com/nanjing-glq/142093252.html?s=sou_sou_soulb&t=0_0']

    def start_requests(self):
        
        yield scrapy.Request(self.start_urls[0])

    def parse(self, response):
        item = {}
        # print(response.body)
        job_posts_per_page=response.xpath("//div[@class='j_joblist']/div[@class='e']")
        print(len(job_posts_per_page))
        for entry in job_posts_per_page:
            url = entry.xpath(".//p[@class='t']/../@href").get()
            item['Url'] = url
            item['Job']=entry.xpath(".//p[@class='t']/span[1]/text()").get()
            item['Salary'] = entry.xpath(".//span[@class='sal']/text()").get()
            item['Address'] = entry.xpath(".//p[@class='info']/span[2]/text()").get().split('  |  ')[0]
            item['Experience'] = entry.xpath(".//p[@class='info']/span[2]/text()").get().split('  |  ')[1]
            item['Education'] = entry.xpath(".//p[@class='info']/span[2]/text()").get().split('  |  ')[2]
            item['Company']=entry.xpath(".//div[@class='er']/a/text()").get()
            item['Welfare']=entry.xpath(".//p[@class='tags']/@title").get()
            yield scrapy.Request(url,callback=self.parse_detail,meta={'item':copy.deepcopy(item)},dont_filter=True)

    def parse_detail(self,response):
        item = response.meta['item']
        content = response.xpath("//div[contains(@class,'job_msg')]").xpath("substring-before(.,'职能类别：')").xpath('string(.)').extract()
        desc=""
        for i in content:
            desc=desc.join(i.split())
        item['desc']=desc
        yield item
    