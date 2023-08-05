import datetime
from pymongoose.mongo_types import Types, Schema

class Team (Schema):
	schema_name = "teams"

	id = None
	name = None
	competition = None
	division = None

	def __init__ (self, **kwargs):
		self.schema = {
			"name": {
				"type": Types.String,
				"required": True
			},
			"athletes": [{
				"type": Types.ObjectId,
				"ref": "athletes"
			}],
			"competition": {
				"type": Types.ObjectId,
				"ref": "competition",
				"required": True
			},
			"division": {
				"type": Types.ObjectId,
				"ref": "divisions",
				"required": True
			},
			"registration_date": {
				"type": Types.Date,
				"default": datetime.datetime.utcnow ()
			},
			"status": {
				"type": Types.Number,
				"default": 1
			},
			"role": {
				"type": Types.Number,
				"default": 1
			},
			"fitcard": {
				"type": Types.ObjectId,
				"ref": "teams.fitcards"
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Team: {self.id} - {self.name}"
