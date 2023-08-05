from pymongoose.mongo_types import Types, Schema

class Permissions (Schema):
	schema_name = "permissions"

	def __init__ (self, **kwargs):
		self.schema = {
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions",
				"required": True
			},
			"user": {
				"type": Types.ObjectId,
				"ref": "users",
				"required": True
			},
			"actions": [{
				"type": Types.String
			}]
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Permissions: {self.id}"
