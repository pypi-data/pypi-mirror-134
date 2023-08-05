import datetime
from pymongoose.mongo_types import Types, Schema

class Currency (Schema):
	schema_name = "currencies"

	name = None
	code = None
	description = None

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
			"code": {
				"type": Types.String,
				"required": True
			},

			"registration_date": {
				"type": Types.Date,
				"default": datetime.datetime.utcnow ()
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Currency: {self.id} - {self.code}"
