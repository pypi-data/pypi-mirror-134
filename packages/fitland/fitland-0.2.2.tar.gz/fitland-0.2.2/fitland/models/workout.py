from pymongoose.mongo_types import Types, Schema

scoring = {
	"0": None,
	"1": "Reps",
	"2": "Round + Reps",
	"3": "Time",
	"4": "Weight - lb",
	"5": "Weight - Kg",
	"6": "Distance - Imperial",
	"7": "Distance - Metric"
}

ranking = {
	"0": None,
	"1": "Lowest is Better",
	"2": "Highest is Better"
}

tie_breaker = {
	"0": None,
	"1": "Ties Stand",
	"2": "Reps",
	"3": "Round + Reps",
	"4": "Time",
	"5": "Weight - lb",
	"6": "Weight - Kg",
	"7": "Distance - Imperial",
	"8": "Distance - Metric"
}

class Workout (Schema):
	schema_name = "workouts"

	id = None
	name = None

	def __init__ (self, **kwargs):
		self.schema = {
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions"
			},
			"name": {
				"type": Types.String,
				"required": True
			},
			"description": {
				"type": Types.String,
				"required": False
			},
			"scoring": {
				"type": Types.Number,
				"required": True
			},
			"ranking": {
				"type": Types.Number,
				"required": True
			},
			"tie_breaker": {
				"type": Types.Number,
				"required": False
			},
			"tie_ranking": {
				"type": Types.Number,
				"required": False
			},
			"tie_description": {
				"type": Types.String,
				"default": ""
			},
			"email": {
				"type": Types.Boolean,
				"default": False
			},
			"publish": {
				"type": Types.Boolean,
				"default": False
			},
			"publish_date": {
				"type": Types.Date,
				"required": True
			},
			"active_divisions": [{
				"type": Types.ObjectId,
				"ref": "divisions"
			}],
			"heats": [{
				"type": Types.ObjectId,
				"ref": "heats"
			}],
			"workout": {
				"type": Types.String,
				"required": False
			},
			"scores": {
				"type": Types.ObjectId,
				"ref": "scores"
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Workout: {self.id} - {self.name}"
