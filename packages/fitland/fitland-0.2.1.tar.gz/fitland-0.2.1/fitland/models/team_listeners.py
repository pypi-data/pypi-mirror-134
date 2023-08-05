from pymongoose.mongo_types import Types, Schema

class TeamListeners (Schema):
	schema_name = "teams.listeners"

	def __init__ (self, **kwargs):
		self.schema = {
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions",
				"required": True
			},
			"team": {
				"type": Types.ObjectId,
				"ref": "teams",
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
