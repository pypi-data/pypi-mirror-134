import datetime
from pymongoose.mongo_types import Types, Schema

class Notification (Schema):
	schema_name = "notifications"

	title = None
	body = None
	n_type = None

	def __init__ (self, **kwargs):
		self.schema = {
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions",
				"required": True
			},
			"division": {
				"type": Types.ObjectId,
				"ref": "divisions",
			},
			"workout": {
				"type": Types.ObjectId,
				"ref": "workouts",
			},
			"heat": {
				"type": Types.ObjectId,
				"ref": "heats",
			},

			"title": {
				"type": Types.String,
				"required": True
			},
			"body": {
				"type": Types.String,
				"required": True
			},

			"exp_date": {
				"type": Types.Date,
				"default": None
			},
			"n_type": {
				"type": Types.Number,
				"default": 0
			},

			"date": {
				"type": Types.Date,
				"default": datetime.datetime.utcnow ()
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Notification: {self.id}"
