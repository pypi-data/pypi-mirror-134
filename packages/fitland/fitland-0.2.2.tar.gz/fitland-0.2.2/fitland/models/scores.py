from pymongoose.mongo_types import Types, Schema

class Scores (Schema):
	schema_name = "scores"

	def __init__ (self, **kwargs):
		self.schema = {
			"name": {
				"type": Types.String,
				"required": True
			},
			"description": {
				"type": Types.String,
				"required": True
			},
			"n_athletes": {
				"type": Types.Number,
				"required": True
			},
			"values": [{
				"type": Types.Number
			}],
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions"
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f""
