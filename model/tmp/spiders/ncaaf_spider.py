import scrapy

class NbaSpider(scrapy.Spider):
  name = "espn"
  start_urls = [
    "https://www.espn.com/college-football/lines",
  ]

  def parse(self, response):
      for table in response.xpath('//tbody[@class="Table__TBODY"]'):
        for team in table.xpath('.//tr[@class="Table__TR Table__TR--sm Table__even"]'):
          yield {
            "team": team.xpath('.//text()').get(),
            "ml": team.xpath('.//td[4]/text()').get(),
            "bpi":team.xpath('.//td[5]/text()').get(),
          }
