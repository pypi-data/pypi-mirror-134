import datetime
from pymongoose.mongo_types import Types, Schema

STAFF_TYPE_NONE = 0
STAFF_TYPE_GENERAL = 1

STAFF_STATUS_NONE = 0
STAFF_STATUS_ACTIVE = 1
STAFF_STATUS_INACTIVE = 2

class Staff (Schema):
	schema_name = "staffs"

	user = None
	competition = None
	staff_type = STAFF_TYPE_NONE
	status = STAFF_STATUS_NONE

	def __init__ (self, **kwargs):
		self.schema = {
			"user": {
				"type": Types.ObjectId,
				"ref": "users",
				"required": True
			},
			
			"competition": {
				"type": Types.ObjectId,
				"ref": "competitions",
				"required": True
			},

			"staff_type": {
				"type": Types.Number,
				"default": STAFF_TYPE_NONE
			},

			"status": {
				"type": Types.Number,
				"default": STAFF_STATUS_NONE
			},

			"registration_date": {
				"type": Types.Date,
				"default": datetime.datetime.utcnow ()
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Staff: {self.id} - {self.user} - {self.competition}"
