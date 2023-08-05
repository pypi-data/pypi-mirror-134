import datetime
from pymongoose.mongo_types import Types, Schema

class HeatSettings (Schema):
	schema_name = "heats.settings"

	def __init__ (self, **kwargs):
		self.schema = {
			"workout": {
				"type": Types.ObjectId,
				"ref": "workouts"
			},
			"division": {
				"type": Types.ObjectId,
				"ref": "divisions"
			},
			"initial_time": {
				"type": Types.Date,
				"default": datetime.datetime.utcnow ()
			},
			"n_rails": {
				"type": Types.Number,
				"required": True
			},
			"workout_time_cap": {
				"type": Types.Number,
				"required": True
			},
			"time_between_heats": {
				"type": Types.Number,
				"required": True
			},
			"time_between_divisions": {
				"type": Types.Number,
				"required": True
			},
			"area": {
				"type": Types.ObjectId,
				"ref": "areas"
			},
			"reps" : {
				"type": Types.String,
				"required": False
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def _str_ (self):
		return f"Settings: {self.id}"
