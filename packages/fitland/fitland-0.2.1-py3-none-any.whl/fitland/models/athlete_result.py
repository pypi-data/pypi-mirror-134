from pymongoose.mongo_types import Types, Schema

class AthleteResult (Schema):
	schema_name = "athletes.results"

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
				"required": True
			},
			"user": {
				"type": Types.ObjectId,
				"ref": "users",
				"required": True
			},
			"username": {
				"type": Types.String,
				"required": True
			},
			"athlete": {
				"type": Types.ObjectId,
				"ref": "athletes",
				"required": True
			},
			"scores": [
				{
					# reference to each workout
					"workout": {
						"type": Types.ObjectId,
						"ref": "workouts",
						"required": True
					},
					# the actual workout score
					"score": {
						"type": Types.String,
						"required": True
					},
					# the position based on workout score
					"pos": {
						"type": Types.String,
						"required": True
					},
					# how ties are handled
					"tie_break": {
						"type": Types.String,
						"required": True
					},
					# points based on score
					"points": {
						"type": Types.String,
						"required": True
					}
				}
			],
			# the total points from all workouts
			"total": {
				"type": Types.Number,
				"default": 0
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f""
