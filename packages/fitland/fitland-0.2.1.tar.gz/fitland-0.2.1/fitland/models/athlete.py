import datetime
from pymongoose.mongo_types import Types, Schema

class Athlete (Schema):
	schema_name = "athletes"

	id = None
	user = None
	username = None
	email = None
	competition = None
	division = None

	def __init__ (self, **kwargs):
		self.schema = {
			"user": {
				"type": Types.ObjectId,
				"ref": "users",
				"required": True
			},
			"username": {
				"type": Types.String,
				"required": True
			},
			"email": {
				"type": Types.String,
				"required": True
			},
			"manager": {
				"type": Types.String,
				"default": None
			},
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions",
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
			"waiver": {
				"type": Types.String,
				"default": "no-waiver.pdf"
			},
			"benchmark_value": {
				"type": Types.Number,
				"default": -1
			},
			"tshirt_size": {
				"type": Types.Number,
				"default": 0
			},
			"fitcard": {
				"type": Types.ObjectId,
				"ref": "athletes.fitcards"
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Athlete: {self.id} - {self.registration_date}"
