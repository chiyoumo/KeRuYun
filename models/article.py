from datetime import datetime

from routes import db
from sqlalchemy import Integer,String,BLOB,TIMESTAMP
from sqlalchemy.orm import Mapped,mapped_column

class Article(db.Model):
    __tablename__ = 'article'
    id:Mapped[int]=mapped_column(Integer,primary_key=True)
    title:Mapped[str]=mapped_column(String,unique=True,nullable=False)
    #__私有的
    __content:Mapped[bytes]=mapped_column(BLOB,name="content",nullable=False)
    create_time:Mapped[datetime]=mapped_column(TIMESTAMP,nullable=False)
    update_time:Mapped[datetime]=mapped_column(TIMESTAMP,nullable=False)
    #转化为字符串来送出去
    @property
    def content(self):
        return self.__content.decode('utf-8')