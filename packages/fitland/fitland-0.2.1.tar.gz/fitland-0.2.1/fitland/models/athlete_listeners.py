from pymongoose.mongo_types import Types, Schema

class AthleteListeners (Schema):
	schema_name = "athletes.listeners"

	def __init__ (self, **kwargs):
		self.schema = {
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions",
				"required": True
			},
			"athlete": {
				"type": Types.ObjectId,
				"ref": "athletes",
				"required": True
			},
			"users": [{
				"type": Types.ObjectId,
				"ref": "users"
			}]
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f""
