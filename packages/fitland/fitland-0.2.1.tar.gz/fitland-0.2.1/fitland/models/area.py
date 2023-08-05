from pymongoose.mongo_types import Types, Schema

class Area (Schema):
	schema_name = "areas"

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
			"n_rails": {
				"type": Types.Number,
				"required": True
			},
			"n_participants": {
				"type": Types.Number,
				"required": True
			},
			"status": {
				"type": Types.Number,
				"default": 1
			},
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions"
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f""
