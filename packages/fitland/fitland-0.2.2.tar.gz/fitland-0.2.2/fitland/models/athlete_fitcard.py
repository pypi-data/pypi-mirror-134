import datetime
from pymongoose.mongo_types import Types, Schema

class AthleteFitcard (Schema):
	schema_name = "athletes.fitcards"

	id = None
	athlete = None
	competition = None
	front = None
	back = None

	def __init__ (self, **kwargs):
		self.schema = {
			"athlete": {
				"type": Types.ObjectId,
				"ref": "athletes",
				"required": True
			},
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
			"date": {
				"type": Types.Date,
				"default": datetime.datetime.utcnow ()
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Athlete Fitcard: {self.id} - {self.date}"
