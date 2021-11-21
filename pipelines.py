# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class AmazonPipeline:
    # def __init__(self) -> None:
    #     self.connection()
    #     self.create_table()

    # def connection(self):
    #     self.conn = sqlite3.connect('amazon.db')
    #     self.cur = self.conn.cursor()

    # def create_table(self):
    #     self.cur.execute("""DROP TABLE IF EXISTS mobile""")
    #     self.cur.execute("""create table mobile(
    #         name text,
    #         price text,
    #         image text
    #         )""")


    def process_item(self, item, spider):
        # self.store_data(item)
        return item

    # def store_data(self,item):
    #     print("Data: ",item)
    #     self.cur.execute("""insert into mobile values (?,?,?)""",(
    #         item['name'],
    #         item['price'],
    #         item['image']
    #     ))

    #     self.conn.commit()