import scrapy


class TcSpider(scrapy.Spider):
    name = "tc"
    allowed_domains = ["xa.58.com"]
    start_urls = ["https://xa.58.com/quanzhizhaopin/?key=python%E7%88%AC%E8%99%AB&cmcskey=python%E7%88%AC%E8%99%AB&final=1&jump=1&specialtype=gls&classpolicy=LBGguide_B%2Cmain_B%2Cjob_B%2Chitword_false%2Cuuid_ADweyRw7MEdJmDM8ccbD6htKWn7RcHJX%2Cdisplocalid_483%2Cfrom_main%2Cto_jump%2Ctradeline_job%2Cclassify_B%2Cwhitelist_strategy_A&search_uuid=ADweyRw7MEdJmDM8ccbD6htKWn7RcHJX&search_type=suggest"]

    def parse(self, response):
        print('山东菏泽招聘信息')
