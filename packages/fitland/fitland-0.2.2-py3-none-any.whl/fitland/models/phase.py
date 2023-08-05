from pymongoose.mongo_types import Types, Schema

REGISTRATION_PHASE_TYPE_NONE = 0
REGISTRATION_PHASE_TYPE_ALL = 1
REGISTRATION_PHASE_TYPE_SELECTED = 2

REGISTRATION_PHASE_STATUS_NONE = 0
REGISTRATION_PHASE_STATUS_PUBLISHED = 1
REGISTRATION_PHASE_STATUS_AVAILABLE = 2
REGISTRATION_PHASE_STATUS_SOLD_OUT = 3
REGISTRATION_PHASE_STATUS_ENDED = 4

class RegistrationPhase (Schema):
	schema_name = "registrations.phases"

	competition = None

	name = None
	description = None

	status = REGISTRATION_PHASE_STATUS_NONE

	price = None
	currency = None

	start_date = None
	end_date = None

	available = None
	sold = None

	def __init__ (self, **kwargs):
		self.schema = {
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions",
				"required": True
			},
			"name": {
				"type": Types.String,
				"required": True
			},
			"description": {
				"type": Types.String,
				"required": True
			},

			"phase_type": {
				"typer": Types.Number,
				"default": REGISTRATION_PHASE_TYPE_NONE
			},
			"status": {
				"typer": Types.Number,
				"default": REGISTRATION_PHASE_STATUS_NONE
			},

			"price": {
				"type": Types.Number,
				"required": True
			},
			"currency": {
				"type": Types.ObjectId,
				"ref": "currencies",
				"required": True
			},

			"start_date": {
				"type": Types.Date,
				"required": True
			},
			"end_date": {
				"type": Types.Date,
				"required": True
			},

			"available": {
				"type": Types.Number,
				"required": True
			},
			"sold": {
				"typer": Types.Number,
				"default": 0
			},

			"divisions": [
				{
					"type": Types.ObjectId,
					"ref": "divisions"
				}
			]
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"RegistrationPhase: {self.id}"
