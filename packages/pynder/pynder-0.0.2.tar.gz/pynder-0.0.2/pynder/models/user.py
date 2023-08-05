import dateutil.parser
from datetime import date
from .. import constants
from .me import Profile
from .message import Message

class User(object):
 def __init__(self,data,session):
  self.id = data['_id']
  try:
   self.distance = data['distance_mi']
  except KeyError:
   self.distance = data['distance_km']
  self.common_friends = data['common_friends']  
  self.common_likes = data['common_likes']  
  self.bio=data['bio']
  self._session = session
  self.gender = constants.GENDER_MAP[int(data['gender'])]
  self.birth_date=data['birth_date']
  self.photos = map(lambda photo: str(photo['url']), data['photos'])
  self.ping_time = data['ping_time']
  self.name=data['name']
  today=date.today()
  self.birth_date=dateutil.parser.parse(self.birth_date)
  self.age=today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
 def __repr__(self):
  return self.name
 def __repr__(self):
  return self.name
 def report(self,cause):
  return self._session._api.report(self.id,cause)

class Hopeful(User):
 def like(self):
  return self._session._api.like(self.id)['match']
 def dislike(self):
  return self._session._api.dislike(self.id)['match']

class Match(User):
 def __init__(self, match, _session):
  user_data = _session._api.user_info(match['person']['_id'])['results']
  user_data['_id'] = match['person']['_id']
  super(Match,self).__init__(user_data, _session)
  self.messages=map(lambda message: Message(message, user=self), match['messages'])
 def message(self,body):
  return self._session._api.message(self.id,body)['_id']

