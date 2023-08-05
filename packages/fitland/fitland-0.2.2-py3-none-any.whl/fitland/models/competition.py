from pymongoose.mongo_types import Types, Schema

COMPETITION_STATUS_NONE	= 0
COMPETITION_STATUS_PUBLISHED = 1
COMPETITION_STATUS_AVAILABLE = 2
COMPETITION_STATUS_PROGRESS = 3
COMPETITION_STATUS_ENDED = 4

class Competition (Schema):
	schema_name = "competitions"

	id = None
	name = None
	address = None
	description = None
	start_date = None
	end_date = None
	logo = None
	cover = None
	waiver = None

	def __init__ (self, **kwargs):
		self.schema = {
			"status": {
				"type": Types.Number,
				"default": COMPETITION_STATUS_NONE
			},
			"name": {
				"type": Types.String,
				"required": True
			},
			"venue_name": {
				"type": Types.String,
				"required": True
			},
			"address": {
				"text": {
					"type": Types.String,
					"required": True
				},
				"lat": {
					"type": Types.Number,
					"required": True
				},
				"lon": {
					"type": Types.Number,
					"required": True
				}
			},
			"description": {
				"type": Types.String,
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
			"logo": {
				"type": Types.String,
				"required": True
			},
			"cover": {
				"type": Types.String,
				"required": True
			},
			"hashtags": [
				{
					"type": Types.String,
				}
			],
			"url": {
				"type": Types.String
			},
			"social_media": {
				"facebook": {
					"type": Types.String
				},
				"instagram": {
					"type": Types.String
				},
				"twitter": {
					"type": Types.String
				}
			},
			"waiver": {
				"type": Types.String,
				"required": True
			},

			"organizers": [
				{
					"type": Types.ObjectId,
					"ref": "organizers"
				}
			],
			"divisions": [
				{
					"type": Types.ObjectId,
					"ref": "divisions"
				}
			],
			"workouts": [
				{
					"type": Types.ObjectId,
					"ref": "workouts"
				}
			],
			"athletes": [
				{
					"type": Types.ObjectId,
					"ref": "athletes"
				}
			]

		}

		super ().__init__ (self.schema_name, self.schema, kwargs)

	def __str__ (self):
		return f"Competition: {self.name} - {self.id}"
