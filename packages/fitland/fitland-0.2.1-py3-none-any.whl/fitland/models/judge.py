import datetime
from pymongoose.mongo_types import Types, Schema

JUDGE_STATUS_NONE = 0
JUDGE_STATUS_ACTIVE = 1
JUDGE_STATUS_INACTIVE = 2

class Judge (Schema):
	schema_name = "judges"

	user = None
	status = JUDGE_STATUS_NONE

	def __init__ (self, **kwargs):
		self.schema = {
			"user": {
				"type": Types.ObjectId,
				"ref": "users",
				"required": True
			},

			"status": {
				"type": Types.Number,
				"default": JUDGE_STATUS_NONE
			},

			"registration_date": {
				"type": Types.Date,
				"default": datetime.datetime.utcnow ()
			}
		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Judge: {self.id} - {self.user}"
