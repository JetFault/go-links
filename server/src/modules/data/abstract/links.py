from datetime import datetime

from modules.data.abstract.base import BaseModel


class ShortLink(BaseModel):
  organization = str
  owner = str
  shortpath = str
  shortpath_prefix = str
  destination_url = str
  visits_count = int
  visits_count_last_updated = datetime

  # TODO: Eliminate the need for this duplication with a better base class.
  _properties = ['id', 'oid', 'created', 'modified',
                 'organization', 'owner', 'shortpath', 'shortpath_prefix',
                 'destination_url', 'visits_count', 'visits_count_last_updated']

  def __eq__(self, other):
    for property in self._properties:
      if getattr(self, property) != getattr(other, property):
        return False

    return True

  @staticmethod
  def get_by_id(id):
    raise NotImplementedError

  @staticmethod
  def get_by_prefix(organization, shortpath_prefix):
    raise NotImplementedError

  @staticmethod
  def get_by_full_path(organization, shortpath):
    raise NotImplementedError

  @staticmethod
  def get_by_organization(organization):
    raise NotImplementedError