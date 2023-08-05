from pymongoose.mongo_types import Types, Schema

class Heat (Schema):
	schema_name = "heats"

	def __init__ (self, **kwargs):
		self.schema = {
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions"
			},
			"workout": {
				"type": Types.ObjectId,
				"ref": "workouts"
			},
			"division": {
				"type": Types.ObjectId,
				"ref": "divisions"
			},
			"start_time": {
				"type": Types.Date,
				"required": True
			},
			"end_time": {
				"type": Types.Date,
				"required": True
			},
			"athletes": [
				{
					"athlete": {
						"type": Types.ObjectId,
						"ref": "athletes"
					},
					"rail": {
						"type": Types.Number,
						"default": -1
					},
				}
			],
			"teams": [
				{
					"team": {
						"type": Types.ObjectId,
						"ref": "teams"
					},
					"rail": {
						"type": Types.Number,
						"default": -1
					}
				}
			]
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)
