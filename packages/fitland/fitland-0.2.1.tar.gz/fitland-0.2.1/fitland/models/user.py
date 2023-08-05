import datetime
from pymongoose.mongo_types import Types, Schema

class User (Schema):
	schema_name = "users"

	id = None
	iat = None
	name = None
	surname = None
	username = None
	email = None
	password = None
	member_since = None
	birth_date = None
	box = None
	gender = None
	role = None

	def __init__ (self, **kwargs):
		self.schema = {
			"name": {
				"type": Types.String,
				"required": True
			},
			"surname": {
				"type": Types.String,
				"required": True
			},
			"username": {
				"type": Types.String,
				"required": True
			},
			"email": {
				"type": Types.String,
				"required": True
			},
			"password": {
				"type": Types.String,
				"required": True
			},
			"member_since": {
				"type": Types.Date,
				"default": datetime.datetime.utcnow ()
			},
			"birth_date": {
				"type": Types.Date,
				"required": True
			},
			"role": {
				"type": Types.ObjectId,
				"ref": "roles"
			},
			"box": {
				"type": Types.String,
				"default": "None"
			},

			# 0 -> None
			# 1 -> Male
			# 2 -> Female
			# 3 -> Other
			"gender": {
				"type": Types.Number,
				"default": 0
			},

			"firebase": {
				"type": Types.String,
				"default": None
			},

			"logged_out": {
				"type": Types.Date,
				"default": None
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Name: {self.name}\nUsername: {self.username}\nEmail: {self.email}"
