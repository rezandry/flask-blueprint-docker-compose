from web_app.modules import db
from sqlalchemy import Integer, Column, String


class Courses(db.Model):
    __tablename__ = 'course'
    id = Column(Integer, primary_key= True)
    title = Column(String)
    url = Column(String)
    description = Column(String)

    def to_dict(self):
        data = {}
        data['id'] = self.id
        data['title'] = self.title
        data['url'] = self.url
        data['description'] = self.description
        return data