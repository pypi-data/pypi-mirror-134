import datetime
from pymongoose.mongo_types import Types, Schema

class AthleteScore (Schema):
	schema_name = "athletes.scores"

	athlete = None
	heat = None
	score = None

	def __init__ (self, **kwargs):
		self.schema = {
			"workout": {
				"type": Types.ObjectId,
				"ref": "workouts",
				"required": True
			},
			"division": {
				"type": Types.ObjectId,
				"ref": "divisions",
				"required": True
			},
			"heat": {
				"type": Types.ObjectId,
				"ref": "heats",
				"required": True
			},
			"athlete": {
				"type": Types.ObjectId,
				"ref": "athletes",
				"required": True
			},
			"date": {
				"type": Types.Date,
				"default": datetime.datetime.utcnow ()
			},
			"score": {
				"type": Types.String,
				"required": True
			},
			"tie_break": {
				"type": Types.String,
				"default": "0"
			},
			"withdrawn": {
				"type": Types.Boolean,
				"default": False
			},
			"cap": {
				"type": Types.Boolean,
				"default": False
			},
			"observations": {
				"type": Types.String,
				"default": None
			},
			"last": {
				"type": Types.Boolean,
				"default": True
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f""
