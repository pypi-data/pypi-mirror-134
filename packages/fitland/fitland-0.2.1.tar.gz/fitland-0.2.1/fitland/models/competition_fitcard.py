import datetime
from pymongoose.mongo_types import Types, Schema

class CompetitionFitcard (Schema):
	schema_name = "competitions.fitcards"

	id = None
	competition = None
	front = None
	back = None

	def __init__ (self, **kwargs):
		self.schema = {
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions",
				"required": True
			},
			"front": {
				"type": Types.String,
				"required": True
			},
			"back": {
				"type": Types.String,
				"required": True
			},
			"created": {
				"type": Types.Date,
				"default": datetime.datetime.utcnow ()
			},
			"updated": {
				"type": Types.Date,
				"default": None
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Competition Fitcard: {self.id} - {self.date}"
